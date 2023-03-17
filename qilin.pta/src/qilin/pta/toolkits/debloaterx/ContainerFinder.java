package qilin.pta.toolkits.debloaterx;

import qilin.core.PTA;
import qilin.core.pag.AllocNode;
import qilin.core.pag.ArrayElement;
import qilin.core.pag.LocalVarNode;
import qilin.core.pag.PAG;
import qilin.util.PTAUtils;
import qilin.util.Stopwatch;
import soot.*;
import soot.jimple.IntConstant;
import soot.jimple.internal.JNewArrayExpr;
import soot.jimple.spark.pag.SparkField;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.stream.Collectors;

public class ContainerFinder {
    protected final PTA pta;
    protected final PAG pag;
    private final Set<AllocNode> primContainers = new HashSet<>();
    private final Set<AllocNode> notcontainers = ConcurrentHashMap.newKeySet();
    private final Map<AllocNode, Set<SparkField>> containers = new ConcurrentHashMap<>();

    private final XUtility utility;

    public ContainerFinder(PTA pta, XUtility utility) {
        this.pta = pta;
        this.pag = pta.getPag();
        this.utility = utility;
    }

    /*
     * classify objects into primitive containers, normal containers and notcontainers.
     * */
    public void run() {
        Stopwatch s1 = Stopwatch.newAndStart("pre-containerFinder");
        Set<AllocNode> remainObjs = new HashSet<>();
        for (AllocNode heap : pag.getAllocNodes()) {
            Type type = heap.getType();
            if (type instanceof ArrayType at) {
                if (!PTAUtils.isPrimitiveArrayType(type)) {
                    JNewArrayExpr nae = (JNewArrayExpr) heap.getNewExpr();
                    Value vl = nae.getSize();
                    if (vl instanceof IntConstant ic && ic.value == 0) {
                        notcontainers.add(heap);
                    } else if (!utility.isCoarseType(at.getElementType())) {
                        notcontainers.add(heap);
                    } else {
                        containers.computeIfAbsent(heap, k -> new HashSet<>()).add(ArrayElement.v());
                    }
                } else {
                    primContainers.add(heap);
                }
            } else if (type instanceof RefType refType) {
                if (heap.getMethod() == null) {
                    /* from definition, these heaps may be containers
                     * but put them into notcontainers does not affect later analysis.
                     * For optimization purpose, we just put them into notcontainers to avoid further checking.
                     * */
                    notcontainers.add(heap);
                } else if (utility.isCoarseType(refType)) {
                    remainObjs.add(heap);
                } else {
                    notcontainers.add(heap);
                }
            } else {
                throw new RuntimeException("invalid type for " + heap);
            }
        }
        s1.stop();
        System.out.println(s1);
        Stopwatch s2 = Stopwatch.newAndStart("mid-containerFinder");
        remainObjs.parallelStream().forEach(utility::getHCQ);
        s2.stop();
        System.out.println(s2);
        Stopwatch s3 = Stopwatch.newAndStart("remain-containerFinder");
        remainObjs.parallelStream().forEach(heap -> {
            Set<SparkField> fields = utility.getFields(heap);
            fields = fields.stream().filter(f -> {
                if (PTAUtils.isPrimitiveArrayType(f.getType())) {
                    return false;
                }
                Type ft = f.getType();
                if (ft instanceof ArrayType fat) {
                    ft = fat.getElementType();
                }
                return utility.isCoarseType(ft);
            }).collect(Collectors.toSet());
            if (fields.isEmpty()) {
                primContainers.add(heap);
            } else {
                HeapContainerQuery hcq = utility.getHCQ(heap);
                for (SparkField field : fields) {
                    // check in
                    boolean hasIn = hasNonThisStoreOnField(heap, field, hcq);
                    if (!hasIn) {
                        continue;
                    }
                    // check out
                    boolean hasOut = hasNonThisLoadFromField(heap, field, hcq);
                    if (hasOut) {
                        containers.computeIfAbsent(heap, k -> new HashSet<>()).add(field);
                    }
                }
                if (!containers.containsKey(heap)) {
                    notcontainers.add(heap);
                }
            }
        });
        s3.stop();
        System.out.println(s3);
        System.out.println("#PrimitiveObjects:" + primContainers.size());
        System.out.println("#ObjectsNotAContainer:" + notcontainers.size());
        System.out.println("#Container:" + containers.size());
    }

    private boolean hasNonThisStoreOnField(AllocNode heap, SparkField field, HeapContainerQuery hcq) {
        if (utility.hasNonThisStoreOnField(heap, field)) {
            return true;
        }
        Set<LocalVarNode> params = hcq.getParamsStoredInto(field);
        Set<SootMethod> nonthisInMs = utility.getInvokedMethods(heap);
        for (LocalVarNode param : params) {
            if (nonthisInMs.contains(param.getMethod())) {
                return true;
            }
        }
        return false;
    }

    private boolean hasNonThisLoadFromField(AllocNode heap, SparkField field, HeapContainerQuery hcq) {
        if (utility.hasNonThisLoadFromField(heap, field)) {
            return true;
        }
        Set<SootMethod> outMs = hcq.getOutMethodsWithRetOrParamValueFrom(field);
        Set<SootMethod> invokedMs = utility.getInvokedMethods(heap);
        for (SootMethod sm : outMs) {
            if (invokedMs.contains(sm)) {
                return true;
            }
        }
        return false;
    }

    public Set<AllocNode> getContainers() {
        return this.containers.keySet();
    }

    public boolean isAContainer(AllocNode heap) {
        if (this.containers.containsKey(heap)) {
            return true;
        } else if (heap.getMethod().getSignature().startsWith("<java.util.Arrays: java.lang.Object[] copyOf(java.lang.Object[],int,java.lang.Class)>")) {
            return true;
        }
        return false;
    }
}

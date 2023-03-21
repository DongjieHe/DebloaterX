package qilin.pta.toolkits.debloaterx;

import com.google.common.collect.Sets;
import qilin.core.PTA;
import qilin.core.builder.MethodNodeFactory;
import qilin.core.pag.*;
import qilin.core.sets.PointsToSet;
import qilin.util.PTAUtils;
import soot.*;
import soot.jimple.InstanceInvokeExpr;
import soot.jimple.InvokeExpr;
import soot.jimple.NullConstant;
import soot.jimple.Stmt;
import soot.jimple.spark.pag.SparkField;
import soot.util.NumberedString;
import soot.util.queue.QueueReader;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/*
 * A container usage pattern-based approach to identifying context-independent objects for context debloating.
 * */
public class DebloaterX {
    private final PTA pta;
    private final PAG pag;
    private final ContainerFinder containerFinder;
    private final XUtility utility;

    public DebloaterX(PTA pta) {
        this.pta = pta;
        this.pag = pta.getPag();
        this.utility = new XUtility(pta);
        this.containerFinder = new ContainerFinder(pta, utility);
        this.containerFinder.run();
    }

    private boolean isAFactoryCreatedContainer(AllocNode heap, IntraFlowAnalysis mpag) {
        SootMethod method = heap.getMethod();
        if (method.isStatic()) {
            Type type = method.getReturnType();
            if (!(type instanceof RefLikeType)) {
                return false;
            }
            MethodPAG methodPag = pag.getMethodPAG(method);
            VarNode mRet = methodPag.nodeFactory().caseRet();
            if (pta.reachingObjects(mRet).toCIPointsToSet().toCollection().contains(heap)) {
                return mpag.isDirectlyReturnedHeap(heap);
            }
        }
        return false;
    }

    private boolean isAContainerWrapper(AllocNode heap, IntraFlowAnalysis mpag) {
        SootMethod method = heap.getMethod();
        if (method.isStatic()) {
            return false;
        }
        Type type = method.getReturnType();
        if (!(type instanceof RefLikeType)) {
            return false;
        }
        MethodPAG methodPag = pag.getMethodPAG(method);
        VarNode mRet = methodPag.nodeFactory().caseRet();
        PointsToSet pts = pta.reachingObjects(mRet);
        Collection<AllocNode> ptsSet = pts.toCIPointsToSet().toCollection();
        if (ptsSet.contains(heap)) {
            if (mpag.isDirectlyReturnedHeap(heap)) {
                Type heapType = heap.getType();
                if (heapType instanceof RefType) {
                    Set<Node> args = collectParamInArguments(heap, mpag);
                    if (!args.isEmpty()) {
                        return mpag.isParamInFromParam(args);
                    }
                } else {
                    return mpag.isArrayContentFromParam(heap);
                }
            }
        }
        return false;
    }

    private boolean isAnInnerContainer(AllocNode heap, IntraFlowAnalysis mpag) {
        SootMethod method = heap.getMethod();
        if (method.isStatic()) {
            return false;
        } else {
            Set<SparkField> fields = mpag.retrieveStoreFields(heap);
            if (fields.isEmpty()) {
                return false;
            } else {
                Set<AllocNode> objects = this.utility.getReceiverObjects(method);
                for (AllocNode revobj : objects) {
                    if (revobj.getType() instanceof RefType) {
                        HeapContainerQuery hcq = this.utility.getHCQ(revobj);
                        for (SparkField field : fields) {
                            if (hcq.isCSField(field)) {
                                return true;
                            }
                        }
                    }
                }
                return false;
            }
        }
    }

    private boolean isPolyCallRelevant(AllocNode heap) {
        SootMethod method = heap.getMethod();
        Set<String> polysigs = Stream.of(
                // (1) objects are container. used by sub-classes.
                "<javax.swing.JComponent: void <init>()>",
                "<java.beans.PropertyChangeSupport: void firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)>",
                "<org.eclipse.jdt.internal.compiler.parser.AbstractCommentParser: void <init>(org.eclipse.jdt.internal.compiler.parser.Parser)>",
                "<org.eclipse.jdt.internal.compiler.parser.AbstractCommentParser: void pushOnAstStack(java.lang.Object,boolean)>",
                // (2) objects are not containers. values from parameters to some fields of the objects and later used to call some methods.
                // under different calling context, the calls maybe different, affect the polycall and call edges.
                "<EDU.purdue.cs.bloat.tree.PrintVisitor: void <init>(java.io.Writer)>",
                "<java.util.zip.ZipInputStream: void <init>(java.io.InputStream)>",
                "<sun.nio.cs.StreamEncoder: sun.nio.cs.StreamEncoder forOutputStreamWriter(java.io.OutputStream,java.lang.Object,java.lang.String)>",
                "<sun.nio.cs.StreamDecoder: sun.nio.cs.StreamDecoder forInputStreamReader(java.io.InputStream,java.lang.Object,java.lang.String)>",
                // (3) not containers. values from paramters to the field of the objects. null ptr relevant precision losses.
                "<java.awt.geom.Rectangle2D: java.awt.geom.PathIterator getPathIterator(java.awt.geom.AffineTransform)>"
        ).collect(Collectors.toSet());
        return polysigs.contains(method.getSignature());
    }

    protected final Set<AllocNode> ctxDepHeaps = ConcurrentHashMap.newKeySet();
    protected final Set<AllocNode> containerFactory = ConcurrentHashMap.newKeySet();
    protected final Set<AllocNode> containerWrapper = ConcurrentHashMap.newKeySet();
    protected final Set<AllocNode> innerContainer = ConcurrentHashMap.newKeySet();
//    private final Set<AllocNode> special = ConcurrentHashMap.newKeySet();

    public void run() {
        Map<SootMethod, Set<AllocNode>> m2o = new HashMap<>();
        for (AllocNode heap : pag.getAllocNodes()) {
            SootMethod method = heap.getMethod();
            if (method == null || method.isStaticInitializer()) {
                continue;
            }
            m2o.computeIfAbsent(method, k -> new HashSet<>()).add(heap);
        }
        m2o.keySet().parallelStream().forEach(method -> {
            IntraFlowAnalysis ifa = new IntraFlowAnalysis(utility, method);
            for (AllocNode heap : m2o.get(method)) {
                if (!this.containerFinder.isAContainer(heap)) {
                    continue;
                }
                if (isAFactoryCreatedContainer(heap, ifa)) {
                    containerFactory.add(heap);
                    ctxDepHeaps.add(heap);
                }
                if (isAContainerWrapper(heap, ifa)) {
                    containerWrapper.add(heap);
                    ctxDepHeaps.add(heap);
                }
                if (isAnInnerContainer(heap, ifa)) {
                    innerContainer.add(heap);
                    ctxDepHeaps.add(heap);
                }
//                if (isPolyCallRelevant(heap)) {
//                    special.add(heap);
//                    ctxDepHeaps.add(heap);
//                }
            }
        });
        System.out.println("#OBJECTS:" + pag.getAllocNodes().size());
        System.out.println("#CS:" + ctxDepHeaps.size());
        System.out.println("#CI:" + (pag.getAllocNodes().size() - ctxDepHeaps.size()));
        System.out.println("#ContainerFactory:" + containerFactory.size());
        System.out.println("#ContainerWrapper:" + containerWrapper.size());
        System.out.println("#InnerContainer:" + innerContainer.size());
        {
            // for drawn venn3 figure.
            int onlyInFactory = Sets.difference(Sets.difference(containerFactory, containerWrapper), innerContainer).size();
            int onlyInWrapper = Sets.difference(Sets.difference(containerWrapper, containerFactory), innerContainer).size();
            int onlyInInner = Sets.difference(Sets.difference(innerContainer, containerWrapper), containerFactory).size();
            int inAll = Sets.intersection(Sets.intersection(innerContainer, containerWrapper), containerFactory).size();
            int onlyInFactoryAndWrapper = Sets.difference(Sets.intersection(containerFactory, containerWrapper), innerContainer).size();
            int onlyInFactoryAndInner = Sets.difference(Sets.intersection(containerFactory, innerContainer), containerWrapper).size();
            int onlyInWrapperAndInner = Sets.difference(Sets.intersection(containerWrapper, innerContainer), containerFactory).size();
            System.out.println("#onlyInFactory:" + onlyInFactory);
            System.out.println("#onlyInWrapper:" + onlyInWrapper);
            System.out.println("#onlyInInner:" + onlyInInner);
            System.out.println("#inAll:" + inAll);
            System.out.println("#onlyInFactoryAndWrapper:" + onlyInFactoryAndWrapper);
            System.out.println("#onlyInFactoryAndInner:" + onlyInFactoryAndInner);
            System.out.println("#onlyInWrapperAndInner:" + onlyInWrapperAndInner);
            System.out.println("#SUM:" + (onlyInFactory + onlyInWrapper + onlyInInner + inAll + onlyInFactoryAndWrapper + onlyInFactoryAndInner + onlyInWrapperAndInner));
            System.out.println("venn3(subsets = (" + onlyInFactory + "," + onlyInWrapper + "," + onlyInFactoryAndWrapper + "," + onlyInInner + ","
                    + onlyInFactoryAndInner + "," + onlyInWrapperAndInner + ", " + inAll + "))");
        }
//        System.out.println("#PolycallRelevant:" + special.size());
//        new Validator(pag, this).validate();
    }

    public Set<AllocNode> getCtxDepHeaps() {
        return ctxDepHeaps;
    }

    private Set<Node> collectParamInArguments(AllocNode heap, IntraFlowAnalysis mpag) {
        RefType type = (RefType) heap.getType();
        SootMethod method = heap.getMethod();
        Set<Node> x = mpag.epsilon(heap);
        Set<Node> ret = new HashSet<>();
        HeapContainerQuery hcq = this.utility.getHCQ(heap);
        Set<LocalVarNode> inParams = hcq.getInParamsToCSFields();
        MethodPAG srcmpag = pag.getMethodPAG(method);
        for (final Unit u : srcmpag.getInvokeStmts()) {
            final Stmt s = (Stmt) u;
            InvokeExpr ie = s.getInvokeExpr();
            if (!(ie instanceof InstanceInvokeExpr iie)) {
                continue;
            }
            LocalVarNode receiver = pag.findLocalVarNode(iie.getBase());
            if (!x.contains(receiver)) {
                continue;
            }
            int numArgs = ie.getArgCount();
            Value[] args = new Value[numArgs];
            for (int i = 0; i < numArgs; i++) {
                Value arg = ie.getArg(i);
                if (!(arg.getType() instanceof RefLikeType) || arg instanceof NullConstant) {
                    continue;
                }
                args[i] = arg;
            }
            NumberedString subSig = iie.getMethodRef().getSubSignature();
            VirtualCallSite virtualCallSite = new VirtualCallSite(receiver, s, method, iie, subSig, soot.jimple.toolkits.callgraph.Edge.ieToKind(iie));
            QueueReader<SootMethod> targets = PTAUtils.dispatch(type, virtualCallSite);
            while (targets.hasNext()) {
                SootMethod target = targets.next();
                MethodPAG tgtmpag = pag.getMethodPAG(target);
                MethodNodeFactory tgtnf = tgtmpag.nodeFactory();
                int numParms = target.getParameterCount();
                if (numParms != numArgs) {
                    System.out.println(target);
                }
                for (int i = 0; i < numParms; i++) {
                    if (target.getParameterType(i) instanceof RefLikeType) {
                        if (args[i] != null) {
                            ValNode argNode = pag.findValNode(args[i]);
                            if (argNode instanceof LocalVarNode lvn) {
                                LocalVarNode param = (LocalVarNode) tgtnf.caseParm(i);
                                if (inParams.contains(param)) {
                                    ret.add(lvn);
                                }
                            }
                        }
                    }
                }
            }
        }
        return ret;
    }
}

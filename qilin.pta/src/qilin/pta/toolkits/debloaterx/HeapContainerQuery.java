package qilin.pta.toolkits.debloaterx;

import qilin.core.builder.MethodNodeFactory;
import qilin.core.pag.*;
import qilin.util.PTAUtils;
import soot.*;
import soot.jimple.spark.pag.SparkField;

import java.util.*;
import java.util.stream.Collectors;

public class HeapContainerQuery {
    private final PAG pag;
    private final XUtility utility;
    private final Set<SootMethod> invokedMs;
    private final Set<LocalVarNode> params;
    private final InterFlowAnalysis interfa;
    private final AllocNode heap;


    public HeapContainerQuery(XUtility utility, AllocNode heap) {
        this.utility = utility;
        this.pag = utility.getPta().getPag();
        this.heap = heap;
        this.invokedMs = utility.getInvokedMethods(heap);
        this.interfa = utility.getInterFlowAnalysis();
        this.params = getParameters();
    }

    /* computes input parameters for the class of refType */
    private Set<LocalVarNode> getParameters() {
        Set<LocalVarNode> ret = new HashSet<>();
        for (SootMethod m : invokedMs) {
            MethodNodeFactory mthdNF = pag.getMethodPAG(m).nodeFactory();
            for (int i = 0; i < m.getParameterCount(); ++i) {
                if (m.getParameterType(i) instanceof RefLikeType && !PTAUtils.isPrimitiveArrayType(m.getParameterType(i))) {
                    LocalVarNode param = (LocalVarNode) mthdNF.caseParm(i);
                    ret.add(param);
                }
            }
            ret.add((LocalVarNode) mthdNF.caseThis());
        }
        return ret;
    }

    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    /* APIs for query */
    public Set<LocalVarNode> getParamsStoredInto(SparkField field) {
        Set<LocalVarNode> tmp = interfa.getParamsStoredInto(field);
        tmp = tmp.stream().filter(this.params::contains).collect(Collectors.toSet());
        return tmp;
    }

    public Set<LocalVarNode> getInParams() {
        Set<LocalVarNode> tmp = interfa.getInParams();
        tmp = tmp.stream().filter(this.params::contains).collect(Collectors.toSet());
        return tmp;
    }

    public Set<SootMethod> getOutMethodsWithRetOrParamValueFrom(SparkField field) {
        Set<SootMethod> tmp = interfa.getOutMethodsWithRetOrParamValueFrom(field);
        tmp = tmp.stream().filter(this.invokedMs::contains).collect(Collectors.toSet());
        return tmp;
    }

    public boolean isCSField(SparkField field) {
        boolean hasIn = utility.hasNonThisStoreOnField(this.heap, field) || !getParamsStoredInto(field).isEmpty();
        boolean hasOut = utility.hasNonThisLoadFromField(this.heap, field) || !getOutMethodsWithRetOrParamValueFrom(field).isEmpty();
        return hasIn && hasOut;
    }
}

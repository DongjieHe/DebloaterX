#!/usr/bin/env python3
import util.Util as Util
import util.benchmark as bm
import util.dacapobach as db
from util.debloaterX.xmaintable import genDebloaterXClientTable
from util.debloaterX.xmaintable import genDebloaterXMainClientTable

# analysisList = ['insens', '2o', 'E-2o', 'Z-2o', '2o+D', '2o+DX', '3o', 'E-3o', 'Z-3o', '3o+D', '3o+DX']

# Main table for dacapo 2006
dacapo2006out='output/run1/'
# allPtaOutputs = Util.loadPtaOutputs(analysisList, bm.BENCHMARKS, dacapo2006out)
# genDebloaterXClientTable(allPtaOutputs, "dacapo2006.tex", bm.BENCHMARKS, analysisList, "Main results for \\texttt{DaCapo 2006}.")

# Main table for dacapo-bach-9.12
dacapobachout = 'output-bach/run1/'
# allPtaOutputs = Util.loadPtaOutputs(analysisList, db.BENCHMARKS, dacapobachout)
# genDebloaterXClientTable(allPtaOutputs, "dacapobach.tex", db.BENCHMARKS, analysisList, "Main results for \\texttt{DaCapo-9.12}.")

# Main table for paper
analysisList = ['insens', '2o', 'Z-2o', '2o+D', '2o+DX', '3o', 'Z-3o', '3o+D', '3o+DX']
bench06 = ['antlr', 'bloat', 'eclipse', 'fop', 'hsqldb']
thirdApps = ['checkstyle', 'JPC']
ptaouts1 = Util.loadPtaOutputs(analysisList, bench06 + thirdApps, dacapo2006out)
bench09 = ['avrora', 'pmd', 'sunflow', 'tradebeans', 'xalan']
ptaouts2 = Util.loadPtaOutputs(analysisList, bench09, dacapobachout)
benchmarks = ['antlr', 'bloat', 'eclipse', 'fop', 'hsqldb', 'checkstyle', 'JPC', 'avrora', 'pmd', 'sunflow', 'tradebeans', 'xalan']
allPtaOutputs = ptaouts1 + ptaouts2
genDebloaterXMainClientTable(allPtaOutputs, "maintable.tex", bench06, thirdApps, bench09, analysisList, "Main results.")
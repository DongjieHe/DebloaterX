#!/usr/bin/env python3
import util.Util as Util
import util.benchmark as bm
from util.debloaterX.xmaintable import genGeneralClientTable

OUTPUT='output/run1/'
analysisList = ['insens', '2o', 'E-2o', 'Z-2o', '2o+D', '2o+DX', '3o', 'E-3o', 'Z-3o', '3o+D', '3o+DX']
allPtaOutputs = Util.loadPtaOutputs(analysisList, bm.BENCHMARKS, OUTPUT)

genGeneralClientTable(allPtaOutputs, "dacapo2006.tex", bm.BENCHMARKS, analysisList)
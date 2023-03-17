#!/usr/bin/env python3

from util.benchmark import BENCHMARKS
from util.generalClient import genGeneralClientTable
import util.Util as Util

analysisList = ['2o', '2o+D', '2o+DX', '3o', '3o+D', '3o+DX']
allPtaOutputs = Util.loadPtaOutputs(analysisList, BENCHMARKS, 'output/qilin/run1/')
genGeneralClientTable(allPtaOutputs, 'tableX.tex', BENCHMARKS, analysisList)

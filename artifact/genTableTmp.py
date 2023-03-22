#!/usr/bin/env python3

# from util.benchmark import BENCHMARKS
# OUTPUT='output/run1/'
# FILENAME='tableX.tex'
from util.dacapobach import BENCHMARKS
OUTPUT = 'output-bach/run1/'
FILENAME ='table-bach.tex'
from util.generalClient import genGeneralClientTable
import util.Util as Util

analysisList = ['2o', 'E-2o', 'Z-2o', '2o+D', '2o+DX', '3o', 'E-3o', 'Z-3o', '3o+D', '3o+DX']
allPtaOutputs = Util.loadPtaOutputs(analysisList, BENCHMARKS, OUTPUT)
genGeneralClientTable(allPtaOutputs, FILENAME, BENCHMARKS, analysisList)

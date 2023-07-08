#!/usr/bin/env python3
import sys
import util.Util as Util
from util.debloaterX.xmaintable import genDebloaterXMainClientTable
from util.debloaterX.xspeedups import drawTwoObjSpeedupBars
from util.debloaterX.xprecision import dumpprecisionLossData
from util.debloaterX.xpretimetable import genDebloaterXPretimeTable
from util.debloaterX.xobjbars import loadXinfos
from util.debloaterX.xobjbars import drawDifferentObjsRatioBar
from util.debloaterX.xobjbars import drawConainerPatternBar
from util.debloaterX.xreductions import computeDebloaterXReductions

'''
The grammar for running this script:
cmd := ./debloaterx.py [-sample]
'''
useSample = False
if __name__ == '__main__':
    if "-sample" in sys.argv:
        useSample = True
    if useSample:
        dacapo2006out='sample/output/run1/'
        dacapobachout='sample/output-bach/run1/'
    else:
        dacapo2006out='output/run1/'
        dacapobachout = 'output-bach/run1/'

    # Main table for paper
    # analysisList = ['insens', '2o', 'Z-2o', '2o+DC', '2o+D', '2o+DX', '3o', 'Z-3o', '3o+DC', '3o+D', '3o+DX']
    analysisList = ['insens', '2o', 'Z-2o', '2o+D', '2o+DX', '3o', 'Z-3o', '3o+D', '3o+DX']
    bench06 = ['antlr', 'bloat', 'eclipse', 'fop', 'hsqldb']
    thirdApps = ['checkstyle', 'JPC']
    bench09 = ['avrora', 'pmd', 'sunflow', 'tradebeans', 'xalan']
    benchmarks = bench06 + thirdApps + bench09

    ptaouts1 = Util.loadPtaOutputs(analysisList, bench06 + thirdApps, dacapo2006out)
    ptaouts2 = Util.loadPtaOutputs(analysisList, bench09, dacapobachout)
    allPtaOutputs = ptaouts1 + ptaouts2
    genDebloaterXMainClientTable(allPtaOutputs, "maintable.tex", bench06, thirdApps, bench09, analysisList, "Main results.")
    drawTwoObjSpeedupBars(allPtaOutputs, benchmarks)
    dumpprecisionLossData(allPtaOutputs, benchmarks)
    # gen-pretime table
    genDebloaterXPretimeTable(allPtaOutputs, "pretimeTable.tex", benchmarks)
    # drawDiffObjectRatioBars
    xinfos1 = loadXinfos(bench06 + thirdApps, dacapo2006out)
    xinfos2 = loadXinfos(bench09, dacapobachout)
    drawDifferentObjsRatioBar(xinfos1 + xinfos2, benchmarks)
    # drawConainerPatternBar
    drawConainerPatternBar(xinfos1 + xinfos2, benchmarks)
    # compute some reduction ratios.
    computeDebloaterXReductions(allPtaOutputs, benchmarks)

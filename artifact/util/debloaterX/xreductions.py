#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import util.Util as Util
import scipy.stats

def reduction(x, y):
    return (x - y) * 1.0 / x

def computeDebloaterXReductions(allPtaOutputs, benchmarks):
    app2tool2outs = Util.buildApp2Tool2PtaOutputMap(allPtaOutputs)
    avgctxratio = []
    csptsratio = []
    oagedgeratio = []
    for app in benchmarks:
        tool2outs = app2tool2outs[app]
        twoobj = tool2outs['2o']
        xtwoobj = tool2outs['2o+DX']
        avgctxratio.append(reduction(twoobj.avgctx, xtwoobj.avgctx))
        csptsratio.append(reduction(twoobj.csGPts + twoobj.csLPts + twoobj.csFPts, xtwoobj.csGPts + xtwoobj.csLPts + xtwoobj.csFPts))
        oagedgeratio.append(reduction(xtwoobj.oagedgenum, xtwoobj.xoagedgenum))
    print(avgctxratio)
    print(csptsratio)
    print(oagedgeratio)
    # dump data
    print()
    print(Util.genTexDataCommand("gmeanAvgCtxReductionRatio", "{:.1f}\%".format(scipy.stats.gmean(avgctxratio) * 100)))
    print(Util.genTexDataCommand("gmeancsptsReductionRatio", "{:.1f}\%".format(scipy.stats.gmean(csptsratio) * 100)))
    print(Util.genTexDataCommand("gmeanoagedgeReductionRatio", "{:.1f}\%".format(scipy.stats.gmean(oagedgeratio) * 100)))
    # draw the bar
    indp1 = np.array([0.0, 1.2, 2.4, 3.6, 4.8, 6.0, 7.2, 8.4, 9.6, 10.8, 12.0, 13.2])
    indp2 = np.array([0.3, 1.5, 2.7, 3.9, 5.1, 6.3, 7.5, 8.7, 9.9, 11.1, 12.3, 13.5])
    indp3 = np.array([0.6, 1.8, 3.0, 4.2, 5.4, 6.6, 7.8, 9.0, 10.2, 11.4, 12.6, 13.8])
    xtickInd = np.array([0.3, 1.5, 2.7, 3.9, 5.1, 6.3, 7.5, 8.7, 9.9, 11.1, 12.3, 13.5])
    width = 0.30  # the width of the bars: can also be len(x) sequence

    plt.figure(figsize=(11, 2.2))
    x1 = plt.bar(indp1, oagedgeratio, width, color='azure', edgecolor='black')
    x2 = plt.bar(indp2, avgctxratio, width, color= 'silver', edgecolor='black')
    x3 = plt.bar(indp3, csptsratio, width, color='lightgreen', edgecolor='black')

    plt.yticks(np.arange(0, 1.08, 0.1), weight='bold')
    plt.xticks(xtickInd, benchmarks, rotation=0, weight='bold')
    plt.tick_params(axis='x', labelsize=8)
    plt.tick_params(axis='y', labelsize=8)
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1, decimals=0))
    plt.ylabel('Reduction Ratio', fontsize=9, weight='bold')
    font = {'size': 6}
    for i in range(len(benchmarks)):
        plt.text(indp1[i] - 0.18, oagedgeratio[i] + 0.015, "{:.0f}%".format(oagedgeratio[i]* 100.0), rotation = 0, fontdict = font)
    for i in range(len(benchmarks)):
        plt.text(indp2[i] - 0.08, avgctxratio[i] + 0.015, "{:.0f}%".format(avgctxratio[i] * 100.0), rotation = 90, fontdict = font)
    for i in range(len(benchmarks)):
        plt.text(indp3[i] - 0.18, csptsratio[i] + 0.012, "{:.0f}%".format(csptsratio[i] * 100.0), rotation = 0, fontdict = font)
    plt.legend((x1[0], x2[0], x3[0]), (r'OAG Edges', r'Average Context Per Method', r'Points-to Relations'), loc='upper center', bbox_to_anchor=(0.5, 1.17), ncol=3, prop={'size': 8, 'weight': 'bold'})
    plt.savefig("reductionratiobars.pdf")
# plt.show()
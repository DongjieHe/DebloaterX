#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from brokenaxes import brokenaxes


import util.Util as Util

# analysisList = ['insens', '2o', 'Z-2o', '2o+D', '2o+DX', '3o', 'Z-3o', '3o+D', '3o+DX']
def produceSpeedupData(allPtaOutputs):
    # compute app2tool2speedups.
    app2tool2outs = Util.buildApp2Tool2PtaOutputMap(allPtaOutputs)
    app2tool2speedups = {}
    for app in app2tool2outs:
        app2tool2speedups[app] = {}
        tool2outs = app2tool2outs[app]
        ci = tool2outs['insens']
        twoobj = tool2outs['2o']
        ztwoobj = tool2outs['Z-2o']
        ctwoobj = tool2outs['2o+D']
        xtwoobj = tool2outs['2o+DX']
        threeobj = tool2outs['3o']
        zthreeobj = tool2outs['Z-3o']
        cthreeobj = tool2outs['3o+D']
        xthreeobj = tool2outs['3o+DX']
        print([app, ci.analysisTime, twoobj.analysisTime, ztwoobj.analysisTime, ctwoobj.analysisTime, xtwoobj.analysisTime, threeobj.analysisTime, zthreeobj.analysisTime, cthreeobj.analysisTime, xthreeobj.analysisTime])
        if twoobj.analysisCompleted():
            ztwoSpeedups = twoobj.analysisTime * 1.0 / ztwoobj.analysisTime
            ctwoSpeedups = twoobj.analysisTime * 1.0 / ctwoobj.analysisTime
            xtwoSpeedups = twoobj.analysisTime * 1.0 / xtwoobj.analysisTime
            print([app, 'k=2', ztwoSpeedups, ctwoSpeedups, xtwoSpeedups])
            app2tool2speedups[app]['Z-2o'] = ztwoSpeedups
            app2tool2speedups[app]['2o+D'] = ctwoSpeedups
            app2tool2speedups[app]['2o+DX'] = xtwoSpeedups
        if threeobj.analysisCompleted():
            zthreeSpeedups = threeobj.analysisTime * 1.0 / zthreeobj.analysisTime
            cthreeSpeedups = threeobj.analysisTime * 1.0 / cthreeobj.analysisTime
            xthreeSpeedups = threeobj.analysisTime * 1.0 / xthreeobj.analysisTime
            print([app, 'k=3', zthreeSpeedups, cthreeSpeedups, xthreeSpeedups])
            app2tool2speedups[app]['Z-3o'] = zthreeSpeedups
            app2tool2speedups[app]['3o+D'] = cthreeSpeedups
            app2tool2speedups[app]['3o+DX'] = xthreeSpeedups
    return app2tool2speedups

def drawTwoObjSpeedupBars(allPtaOutputs, benchmarks):
    app2tool2speedups = produceSpeedupData(allPtaOutputs)
    z2s = []
    for app in benchmarks:
        z2s.append(app2tool2speedups[app]['Z-2o'])
    c2s = []
    for app in benchmarks:
        c2s.append(app2tool2speedups[app]['2o+D'])
    x2s = []
    for app in benchmarks:
        x2s.append(app2tool2speedups[app]['2o+DX'])
    indp1 = np.array([0.0, 1.2, 2.4, 3.6, 4.8, 6.0, 7.2, 8.4, 9.6, 10.8, 12.0, 13.2])
    indp2 = np.array([0.3, 1.5, 2.7, 3.9, 5.1, 6.3, 7.5, 8.7, 9.9, 11.1, 12.3, 13.5])
    indp3 = np.array([0.6, 1.8, 3.0, 4.2, 5.4, 6.6, 7.8, 9.0, 10.2, 11.4, 12.6, 13.8])
    xtickInd = np.array([0.3, 1.5, 2.7, 3.9, 5.1, 6.3, 7.5, 8.7, 9.9, 11.1, 12.3, 13.5])
    width = 0.30  # the width of the bars: can also be len(x) sequence

    plt.figure(figsize=(11, 4.2))
    bax = brokenaxes(ylims=((0.0, 90.0), (270.0, 300.0)), wspace=0.05, hspace=0.05)
    print(len(indp1))
    print(len(x2s))
    x1 = bax.bar(indp1, x2s, width, color= 'lightgray', edgecolor='black')
    x2 = bax.bar(indp2, c2s, width, color='mistyrose', edgecolor='black')
    x3 = bax.bar(indp3, z2s, width, color='lightsteelblue', edgecolor='black')

    bax.axs[1].set_xticks(xtickInd)
    bax.axs[1].set_xticklabels(benchmarks, rotation=10, weight='bold')
    # plt.xticks(xtickInd, benchmarks, rotation=10, weight='bold')
    for i in range(len(benchmarks)):
        bax.text(indp1[i] - 0.08, x2s[i] + 1.5, "{:.1f}".format(x2s[i]) + r'$\times$', rotation = 90)
    for i in range(len(benchmarks)):
        bax.text(indp2[i] - 0.08, c2s[i] + 1.5, "{:.1f}".format(c2s[i]) + r'$\times$', rotation = 90)
    for i in range(len(benchmarks)):
        bax.text(indp3[i] - 0.08, z2s[i] + 1.5, "{:.1f}".format(z2s[i]) + r'$\times$', rotation = 90)
    bax.legend((x1[0], x2[0], x3[0]), (r'X-2obj', r'C-2obj', r'Z-2obj'), loc='upper right',  ncol=1, prop={'weight': 'bold'})
    plt.savefig("speeduptwo.pdf")
    # plt.show()

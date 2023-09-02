#!/usr/bin/env python3

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from brokenaxes import brokenaxes
import scipy.stats

import util.Util as Util

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

# analysisList = ['insens', '2o', 'Z-2o', '2o+D', '2o+DX', '3o', 'Z-3o', '3o+D', '3o+DX']
def produceSpeedupData(allPtaOutputs):
    # compute app2tool2speedups.
    app2tool2outs = Util.buildApp2Tool2PtaOutputMap(allPtaOutputs)
    app2tool2speedups = {}
    slowdownsOverSpark = []
    speedupsOverConchThree = []
    for app in app2tool2outs:
        app2tool2speedups[app] = {}
        tool2outs = app2tool2outs[app]
        ci = tool2outs['insens']
        twoobj = tool2outs['2o']
        ztwoobj = tool2outs['Z-2o']
        ctwoobj = tool2outs['2o+D']
        xtwoobj = tool2outs['2o+DX']
        stwoobj = tool2outs['2o+DC']
        threeobj = tool2outs['3o']
        zthreeobj = tool2outs['Z-3o']
        cthreeobj = tool2outs['3o+D']
        xthreeobj = tool2outs['3o+DX']
        sthreeobj = tool2outs['3o+DC']
        print([app, ci.analysisTime, twoobj.analysisTime, ztwoobj.analysisTime, stwoobj.analysisTime, ctwoobj.analysisTime, xtwoobj.analysisTime, threeobj.analysisTime, zthreeobj.analysisTime, sthreeobj.analysisTime, cthreeobj.analysisTime, xthreeobj.analysisTime])
        if twoobj.analysisCompleted():
            ztwoSpeedups = twoobj.analysisTime * 1.0 / ztwoobj.analysisTime
            ctwoSpeedups = twoobj.analysisTime * 1.0 / ctwoobj.analysisTime
            xtwoSpeedups = twoobj.analysisTime * 1.0 / xtwoobj.analysisTime
            stwoSpeedups = twoobj.analysisTime * 1.0 / stwoobj.analysisTime
            print([app, 'k=2', ztwoSpeedups, stwoSpeedups, ctwoSpeedups, xtwoSpeedups])
            app2tool2speedups[app]['Z-2o'] = ztwoSpeedups
            app2tool2speedups[app]['2o+D'] = ctwoSpeedups
            app2tool2speedups[app]['2o+DX'] = xtwoSpeedups
            app2tool2speedups[app]['2o+DC'] = stwoSpeedups
        if threeobj.analysisCompleted():
            zthreeSpeedups = threeobj.analysisTime * 1.0 / zthreeobj.analysisTime
            cthreeSpeedups = threeobj.analysisTime * 1.0 / cthreeobj.analysisTime
            xthreeSpeedups = threeobj.analysisTime * 1.0 / xthreeobj.analysisTime
            sthreeSpeedups = threeobj.analysisTime * 1.0 / sthreeobj.analysisTime
            print([app, 'k=3', zthreeSpeedups, sthreeSpeedups, cthreeSpeedups, xthreeSpeedups])
            app2tool2speedups[app]['Z-3o'] = zthreeSpeedups
            app2tool2speedups[app]['3o+D'] = cthreeSpeedups
            app2tool2speedups[app]['3o+DX'] = xthreeSpeedups
            app2tool2speedups[app]['3o+DC'] = sthreeSpeedups
        if xtwoobj.analysisCompleted():
            twoSpeedupOverSpark = xtwoobj.analysisTime * 1.0 / ci.analysisTime
            slowdownsOverSpark.append(twoSpeedupOverSpark)
        if xthreeobj.analysisCompleted():
            threeSpeedupOverSpark = xthreeobj.analysisTime * 1.0 / ci.analysisTime
            slowdownsOverSpark.append(threeSpeedupOverSpark)
        if cthreeobj.analysisCompleted():
            threeSpeedupOverConch = cthreeobj.analysisTime * 1.0 / xthreeobj.analysisTime
            print([app, threeSpeedupOverConch])
            speedupsOverConchThree.append(threeSpeedupOverConch)
    print()
    print(slowdownsOverSpark)
    print(Util.genTexDataCommand("xavgslowdownsoverspark", "{:.1f}".format(scipy.stats.gmean(slowdownsOverSpark)) + r'$\times$'))
    print()
    print("3o+DX vs. 3o+D")
    print(speedupsOverConchThree)
    print(Util.genTexDataCommand("xthreeminspeedupoverconch", "{:.1f}".format(min(speedupsOverConchThree)) + r'$\times$'))
    print(Util.genTexDataCommand("xthreegmeanspeedupoverconch", "{:.1f}".format(scipy.stats.gmean(speedupsOverConchThree)) + r'$\times$'))
    print(Util.genTexDataCommand("xthreemaxspeedupoverconch", "{:.1f}".format(max(speedupsOverConchThree)) + r'$\times$'))
    print()
    return app2tool2speedups

def dumpSpeedUpsData(app2tool2speedups, benchmarks):
    z2s = []
    for app in benchmarks:
        z2s.append(app2tool2speedups[app]['Z-2o'])
    print(Util.genTexDataCommand("zippertwoobjminspeedups", "{:.1f}".format(min(z2s)) + r'$\times$'))
    print(Util.genTexDataCommand("zippertwoobjmaxspeedups", "{:.1f}".format(max(z2s)) + r'$\times$'))
    print(Util.genTexDataCommand("zippertwoobjgmeanspeedups", "{:.1f}".format(scipy.stats.gmean(z2s)) + r'$\times$'))
    for app in benchmarks:
        if app2tool2speedups[app]['Z-2o'] == min(z2s):
            print(Util.genTexDataCommand("zippertwoobjminspeedupapp", "\\texttt{"+ app + r'}'))
        if app2tool2speedups[app]['Z-2o'] == max(z2s):
            print(Util.genTexDataCommand("zippertwoobjmaxspeedupapp", "\\texttt{"+ app + r'}'))

    c2s = []
    for app in benchmarks:
        c2s.append(app2tool2speedups[app]['2o+D'])
    print(Util.genTexDataCommand("conchtwoobjminspeedups", "{:.1f}".format(min(c2s)) + r'$\times$'))
    print(Util.genTexDataCommand("conchtwoobjmaxspeedups", "{:.1f}".format(max(c2s)) + r'$\times$'))
    print(Util.genTexDataCommand("conchtwoobjgmeanspeedups", "{:.1f}".format(scipy.stats.gmean(c2s)) + r'$\times$'))
    for app in benchmarks:
        if app2tool2speedups[app]['2o+D'] == min(c2s):
            print(Util.genTexDataCommand("conchtwoobjminspeedupapp", "\\texttt{"+ app + r'}'))
        if app2tool2speedups[app]['2o+D'] == max(c2s):
            print(Util.genTexDataCommand("conchtwoobjmaxspeedupapp", "\\texttt{"+ app + r'}'))

    x2s = []
    for app in benchmarks:
        x2s.append(app2tool2speedups[app]['2o+DX'])
    print(Util.genTexDataCommand("debloaterxtwoobjminspeedups", "{:.1f}".format(min(x2s)) + r'$\times$'))
    print(Util.genTexDataCommand("debloaterxtwoobjmaxspeedups", "{:.1f}".format(max(x2s)) + r'$\times$'))
    print(Util.genTexDataCommand("debloaterxtwoobjgmeanspeedups", "{:.1f}".format(scipy.stats.gmean(x2s)) + r'$\times$'))
    for app in benchmarks:
        if app2tool2speedups[app]['2o+DX'] == min(x2s):
            print(Util.genTexDataCommand("debloaterxtwoobjminspeedupapp", "\\texttt{"+ app + r'}'))
        if app2tool2speedups[app]['2o+DX'] == max(x2s):
            print(Util.genTexDataCommand("debloaterxtwoobjmaxspeedupapp", "\\texttt{"+ app + r'}'))

    s2s = []
    for app in benchmarks:
        s2s.append(app2tool2speedups[app]['2o+DC'])
    print(Util.genTexDataCommand("collectiontwoobjminspeedups", "{:.1f}".format(min(s2s)) + r'$\times$'))
    print(Util.genTexDataCommand("collectiontwoobjmaxspeedups", "{:.1f}".format(max(s2s)) + r'$\times$'))
    print(Util.genTexDataCommand("collectiontwoobjgmeanspeedups", "{:.1f}".format(scipy.stats.gmean(s2s)) + r'$\times$'))
    for app in benchmarks:
        if app2tool2speedups[app]['2o+DC'] == min(s2s):
            print(Util.genTexDataCommand("collectiontwoobjminspeedupapp", "\\texttt{"+ app + r'}'))
        if app2tool2speedups[app]['2o+DC'] == max(s2s):
            print(Util.genTexDataCommand("collectiontwoobjmaxspeedupapp", "\\texttt{"+ app + r'}'))

    # average speedups in each group.
    print()
    d1 = x2s[0:5]
    d2 = x2s[5:7]
    d3 = x2s[-5:]
    print("Speedups in each group:")
    print(d1)
    print(d2)
    print(d3)
    print(Util.genTexDataCommand("xtwogmSpeedupsondacaposix", "{:.1f}".format(scipy.stats.gmean(d1)) + r'$\times$'))
    print(Util.genTexDataCommand("xtwogmSpeedupsonthirdapp", "{:.1f}".format(scipy.stats.gmean(d2)) + r'$\times$'))
    print(Util.genTexDataCommand("xtwogmSpeedupsondacaponine", "{:.1f}".format(scipy.stats.gmean(d3)) + r'$\times$'))
    print()

    z3s = []
    for app in benchmarks:
        if app in app2tool2speedups and 'Z-3o' in app2tool2speedups[app]:
            z3s.append(app2tool2speedups[app]['Z-3o'])
    print(Util.genTexDataCommand("zipperthreeobjminspeedups", "{:.1f}".format(min(z3s)) + r'$\times$'))
    print(Util.genTexDataCommand("zipperthreeobjmaxspeedups", "{:.1f}".format(max(z3s)) + r'$\times$'))
    print(Util.genTexDataCommand("zipperthreeobjgmeanspeedups", "{:.1f}".format(scipy.stats.gmean(z3s)) + r'$\times$'))
    for app in benchmarks:
        if app not in app2tool2speedups or 'Z-3o' not in app2tool2speedups[app]:
            continue
        if app2tool2speedups[app]['Z-3o'] == min(z3s):
            print(Util.genTexDataCommand("zipperthreeobjminspeedupapp", "\\texttt{"+ app + r'}'))
        if app2tool2speedups[app]['Z-3o'] == max(z3s):
            print(Util.genTexDataCommand("zipperthreeobjmaxspeedupapp", "\\texttt{"+ app + r'}'))

    c3s = []
    for app in benchmarks:
        if app in app2tool2speedups and '3o+D' in app2tool2speedups[app]:
            c3s.append(app2tool2speedups[app]['3o+D'])
    print(Util.genTexDataCommand("conchthreeobjminspeedups", "{:.1f}".format(min(c3s)) + r'$\times$'))
    print(Util.genTexDataCommand("conchthreeobjmaxspeedups", "{:.1f}".format(max(c3s)) + r'$\times$'))
    print(Util.genTexDataCommand("conchthreeobjgmeanspeedups", "{:.1f}".format(scipy.stats.gmean(c3s)) + r'$\times$'))
    for app in benchmarks:
        if app not in app2tool2speedups or '3o+D' not in app2tool2speedups[app]:
            continue
        if app2tool2speedups[app]['3o+D'] == min(c3s):
            print(Util.genTexDataCommand("conchthreeobjminspeedupapp", "\\texttt{"+ app + r'}'))
        if app2tool2speedups[app]['3o+D'] == max(c3s):
            print(Util.genTexDataCommand("conchthreeobjmaxspeedupapp", "\\texttt{"+ app + r'}'))

    x3s = []
    for app in benchmarks:
        if app in app2tool2speedups and '3o+DX' in app2tool2speedups[app]:
            x3s.append(app2tool2speedups[app]['3o+DX'])
    print(Util.genTexDataCommand("debloaterxthreeobjminspeedups", "{:.1f}".format(min(x3s)) + r'$\times$'))
    print(Util.genTexDataCommand("debloaterxthreeobjmaxspeedups", "{:.1f}".format(max(x3s)) + r'$\times$'))
    print(Util.genTexDataCommand("debloaterxthreeobjgmeanspeedups", "{:.1f}".format(scipy.stats.gmean(x3s)) + r'$\times$'))
    for app in benchmarks:
        if app not in app2tool2speedups or '3o+DX' not in app2tool2speedups[app]:
            continue
        if app2tool2speedups[app]['3o+DX'] == min(x3s):
            print(Util.genTexDataCommand("debloaterxthreeobjminspeedupapp", "\\texttt{"+ app + r'}'))
        if app2tool2speedups[app]['3o+DX'] == max(x3s):
            print(Util.genTexDataCommand("debloaterxthreeobjmaxspeedupapp", "\\texttt{"+ app + r'}'))

    s3s = []
    for app in benchmarks:
        if app in app2tool2speedups and '3o+DC' in app2tool2speedups[app]:
            s3s.append(app2tool2speedups[app]['3o+DC'])
    print(Util.genTexDataCommand("collectionthreeobjminspeedups", "{:.1f}".format(min(s3s)) + r'$\times$'))
    print(Util.genTexDataCommand("collectionthreeobjmaxspeedups", "{:.1f}".format(max(s3s)) + r'$\times$'))
    print(Util.genTexDataCommand("collectionthreeobjgmeanspeedups", "{:.1f}".format(scipy.stats.gmean(s3s)) + r'$\times$'))
    for app in benchmarks:
        if app not in app2tool2speedups or '3o+DC' not in app2tool2speedups[app]:
            continue
        if app2tool2speedups[app]['3o+DC'] == min(s3s):
            print(Util.genTexDataCommand("collectionthreeobjminspeedupapp", "\\texttt{"+ app + r'}'))
        if app2tool2speedups[app]['3o+DC'] == max(s3s):
            print(Util.genTexDataCommand("collectionthreeobjmaxspeedupapp", "\\texttt{"+ app + r'}'))

def drawTwoObjSpeedupBars(allPtaOutputs, benchmarks):
    app2tool2speedups = produceSpeedupData(allPtaOutputs)
    dumpSpeedUpsData(app2tool2speedups, benchmarks)
    z2s = []
    for app in benchmarks:
        z2s.append(app2tool2speedups[app]['Z-2o'])
    c2s = []
    for app in benchmarks:
        c2s.append(app2tool2speedups[app]['2o+D'])
    x2s = []
    for app in benchmarks:
        x2s.append(app2tool2speedups[app]['2o+DX'])
    s2s = []
    for app in benchmarks:
        s2s.append(app2tool2speedups[app]['2o+DC'])
    indp1 = np.array([0.0, 1.2, 2.4, 3.6, 4.8, 6.0, 7.2, 8.4, 9.6, 10.8, 12.0, 13.2])
    indp2 = np.array([0.25, 1.45, 2.65, 3.85, 5.05, 6.25, 7.45, 8.65, 9.85, 11.05, 12.25, 13.45])
    indp3 = np.array([0.5, 1.7, 2.9, 4.1, 5.3, 6.5, 7.7, 8.9, 10.1, 11.3, 12.5, 13.7])
    indp4 = np.array([0.75, 1.95, 3.15, 4.35, 5.55, 6.75, 7.95, 9.15, 10.35, 11.55, 12.75, 13.95])
    xtickInd = np.array([0.375, 1.575, 2.775, 3.975, 5.175, 6.375, 7.575, 8.775, 9.975, 11.175, 12.375, 13.575])
    width = 0.25  # the width of the bars: can also be len(x) sequence

    plt.figure(figsize=(11, 4.2))
    bax = brokenaxes(ylims=((0.0, 90.0), (270.0, 300.0)), wspace=0.05, hspace=0.05)
    x1 = bax.bar(indp1, x2s, width, color= 'lightgray', edgecolor='black')
    x2 = bax.bar(indp2, c2s, width, color='mistyrose', edgecolor='black')
    x3 = bax.bar(indp3, z2s, width, color='lightsteelblue', edgecolor='black')
    x4 = bax.bar(indp4, s2s, width, color='wheat', edgecolor='black')

    bax.axs[1].set_xticks(xtickInd)
    bax.axs[1].set_xticklabels(benchmarks, weight='bold', fontsize = 8)
    bax.axs[1].tick_params(axis='y', labelsize=8)
    bax.axs[0].tick_params(axis='y', labelsize=8)
    font = {'size': 6, 'weight':'bold'}
    # plt.xticks(xtickInd, benchmarks, rotation=10, weight='bold')
    for i in range(len(benchmarks)):
        bax.text(indp1[i] - 0.08, x2s[i] + 1.9, "{:.1f}".format(x2s[i]) + r'$\times$', rotation = 90, fontdict = font)
    for i in range(len(benchmarks)):
        bax.text(indp2[i] - 0.08, c2s[i] + 1.9, "{:.1f}".format(c2s[i]) + r'$\times$', rotation = 90, fontdict = font)
    for i in range(len(benchmarks)):
        bax.text(indp3[i] - 0.08, z2s[i] + 1.9, "{:.1f}".format(z2s[i]) + r'$\times$', rotation = 90, fontdict = font)
    for i in range(len(benchmarks)):
        bax.text(indp4[i] - 0.08, s2s[i] + 1.9, "{:.1f}".format(s2s[i]) + r'$\times$', rotation = 90, fontdict = font)
    bax.legend((x1[0], x2[0], x3[0], x4[0]), (r'X-2obj', r'C-2obj', r'Z-2obj', r'S-2obj'), loc='upper right', ncol=1, prop={'size': 8, 'weight': 'bold'})
    plt.savefig("speeduptwo.pdf")
    # plt.show()

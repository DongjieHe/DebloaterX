#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import util.Util as Util

def precisionLoss(cimetric, baselinemetric, toolmetric):
    return (toolmetric - baselinemetric) * 1.0 / (cimetric - baselinemetric)

def producePrecisionLossData(allPtaOutputs):
    app2tool2outs = Util.buildApp2Tool2PtaOutputMap(allPtaOutputs)
    app2tool2failcastloss = {}
    app2tool2calledgeloss = {}
    app2tool2reachablesloss = {}
    app2tool2polycallloss = {}
    for app in app2tool2outs:
        app2tool2failcastloss[app] = {}
        app2tool2calledgeloss[app] = {}
        app2tool2reachablesloss[app] = {}
        app2tool2polycallloss[app] = {}
        tool2outs = app2tool2outs[app]
        ci = tool2outs['insens']
        twoobj = tool2outs['2o']
        ztwoobj = tool2outs['Z-2o']
        ctwoobj = tool2outs['2o+D']
        xtwoobj = tool2outs['2o+DX']
        # threeobj = tool2outs['3o']
        # zthreeobj = tool2outs['Z-3o']
        # cthreeobj = tool2outs['3o+D']
        # xthreeobj = tool2outs['3o+DX']
        if twoobj.analysisCompleted():
            # fail-casts
            ztwofailcast = precisionLoss(int(ci.mayFailCasts), int(twoobj.mayFailCasts), int(ztwoobj.mayFailCasts))
            ctwofailcast = precisionLoss(int(ci.mayFailCasts), int(twoobj.mayFailCasts), int(ctwoobj.mayFailCasts))
            xtwofailcast = precisionLoss(int(ci.mayFailCasts), int(twoobj.mayFailCasts), int(xtwoobj.mayFailCasts))
            print([app, 'k=2', 'fail-casts', ztwofailcast, ctwofailcast, xtwofailcast])
            app2tool2failcastloss[app]['Z-2o'] = ztwofailcast
            app2tool2failcastloss[app]['2o+D'] = ctwofailcast
            app2tool2failcastloss[app]['2o+DX'] = xtwofailcast
            # call edges
            ztwocalledge = precisionLoss(int(ci.callEdges), int(twoobj.callEdges), int(ztwoobj.callEdges))
            ctwocalledge = precisionLoss(int(ci.callEdges), int(twoobj.callEdges), int(ctwoobj.callEdges))
            xtwocalledge = precisionLoss(int(ci.callEdges), int(twoobj.callEdges), int(xtwoobj.callEdges))
            print([app, 'k=2', 'call-edges', ztwocalledge, ctwocalledge, xtwocalledge])
            app2tool2calledgeloss[app]['Z-2o'] = ztwocalledge
            app2tool2calledgeloss[app]['2o+D'] = ctwocalledge
            app2tool2calledgeloss[app]['2o+DX'] = xtwocalledge
            # reachables
            ztworeachables = precisionLoss(int(ci.reachMethods), int(twoobj.reachMethods), int(ztwoobj.reachMethods))
            ctworeachables = precisionLoss(int(ci.reachMethods), int(twoobj.reachMethods), int(ctwoobj.reachMethods))
            xtworeachables = precisionLoss(int(ci.reachMethods), int(twoobj.reachMethods), int(xtwoobj.reachMethods))
            print([app, 'k=2', 'reachables', ztworeachables, ctworeachables, xtworeachables])
            app2tool2reachablesloss[app]['Z-2o'] = ztworeachables
            app2tool2reachablesloss[app]['2o+D'] = ctworeachables
            app2tool2reachablesloss[app]['2o+DX'] = xtworeachables
            # poly-calls
            ztwopolycalls = precisionLoss(int(ci.polyCalls), int(twoobj.polyCalls), int(ztwoobj.polyCalls))
            ctwopolycalls = precisionLoss(int(ci.polyCalls), int(twoobj.polyCalls), int(ctwoobj.polyCalls))
            xtwopolycalls = precisionLoss(int(ci.polyCalls), int(twoobj.polyCalls), int(xtwoobj.polyCalls))
            print([app, 'k=2', 'poly-calls', ztwopolycalls, ctwopolycalls, xtwopolycalls])
            app2tool2polycallloss[app]['Z-2o'] = ztwopolycalls
            app2tool2polycallloss[app]['2o+D'] = ctwopolycalls
            app2tool2polycallloss[app]['2o+DX'] = xtwopolycalls
        # if threeobj.analysisCompleted():

    return app2tool2failcastloss, app2tool2calledgeloss, app2tool2reachablesloss, app2tool2polycallloss

def dumpprecisionLossData(allPtaOutputs, benchmarks):
    app2tool2failcastloss, app2tool2calledgeloss, app2tool2reachablesloss, app2tool2polycallloss = producePrecisionLossData(allPtaOutputs)
    ztwofailcast, ctwofailcast,  xtwofailcast = ([] for _ in range(3))
    ztwocalledge, ctwocalledge, xtwocalledge = ([] for _ in range(3))
    ztworeachables, ctworeachables, xtworeachables = ([] for _ in range(3))
    ztwopolycalls, ctwopolycalls, xtwopolycalls = ([] for _ in range(3))
    for app in benchmarks:
        ztwofailcast.append(app2tool2failcastloss[app]['Z-2o'])
        ctwofailcast.append(app2tool2failcastloss[app]['2o+D'])
        xtwofailcast.append(app2tool2failcastloss[app]['2o+DX'])

        ztwocalledge.append(app2tool2calledgeloss[app]['Z-2o'])
        ctwocalledge.append(app2tool2calledgeloss[app]['2o+D'])
        xtwocalledge.append(app2tool2calledgeloss[app]['2o+DX'])

        ztworeachables.append(app2tool2reachablesloss[app]['Z-2o'])
        ctworeachables.append(app2tool2reachablesloss[app]['2o+D'])
        xtworeachables.append(app2tool2reachablesloss[app]['2o+DX'])

        if 'Z-2o' not in app2tool2polycallloss[app]:
            print("why" + app)
        ztwopolycalls.append(app2tool2polycallloss[app]['Z-2o'])
        ctwopolycalls.append(app2tool2polycallloss[app]['2o+D'])
        xtwopolycalls.append(app2tool2polycallloss[app]['2o+DX'])

    # fail-casts
    print(Util.genTexDataCommand("ztwofailcastminloss", "{:.1f}\%".format(min(ztwofailcast) * 100.0)))
    print(Util.genTexDataCommand("ctwofailcastminloss", "{:.1f}\%".format(min(ctwofailcast) * 100.0)))
    print(Util.genTexDataCommand("xtwofailcastminloss", "{:.1f}\%".format(min(xtwofailcast) * 100.0)))

    print(Util.genTexDataCommand("ztwofailcastmaxloss", "{:.1f}\%".format(max(ztwofailcast) * 100.0)))
    print(Util.genTexDataCommand("ctwofailcastmaxloss", "{:.1f}\%".format(max(ctwofailcast) * 100.0)))
    print(Util.genTexDataCommand("xtwofailcastmaxloss", "{:.1f}\%".format(max(xtwofailcast) * 100.0)))

    print(Util.genTexDataCommand("ztwofailcastavgloss", "{:.1f}\%".format(Util.average(ztwofailcast) * 100.0)))
    print(Util.genTexDataCommand("ctwofailcastavgloss", "{:.1f}\%".format(Util.average(ctwofailcast) * 100.0)))
    print(Util.genTexDataCommand("xtwofailcastavgloss", "{:.1f}\%".format(Util.average(xtwofailcast) * 100.0)))

    # call-edges
    print(Util.genTexDataCommand("ztwocalledgeminloss", "{:.1f}\%".format(min(ztwocalledge) * 100.0)))
    print(Util.genTexDataCommand("ctwocalledgeminloss", "{:.1f}\%".format(min(ctwocalledge) * 100.0)))
    print(Util.genTexDataCommand("xtwocalledgeminloss", "{:.1f}\%".format(min(xtwocalledge) * 100.0)))

    print(Util.genTexDataCommand("ztwocalledgemaxloss", "{:.1f}\%".format(max(ztwocalledge) * 100.0)))
    print(Util.genTexDataCommand("ctwocalledgemaxloss", "{:.1f}\%".format(max(ctwocalledge) * 100.0)))
    print(Util.genTexDataCommand("xtwocalledgemaxloss", "{:.1f}\%".format(max(xtwocalledge) * 100.0)))

    print(Util.genTexDataCommand("ztwocalledgeavgloss", "{:.1f}\%".format(Util.average(ztwocalledge) * 100.0)))
    print(Util.genTexDataCommand("ctwocalledgeavgloss", "{:.1f}\%".format(Util.average(ctwocalledge) * 100.0)))
    print(Util.genTexDataCommand("xtwocalledgeavgloss", "{:.1f}\%".format(Util.average(xtwocalledge) * 100.0)))

    # reachables
    print(Util.genTexDataCommand("ztworeachableminloss", "{:.1f}\%".format(min(ztworeachables) * 100.0)))
    print(Util.genTexDataCommand("ctworeachableminloss", "{:.1f}\%".format(min(ctworeachables) * 100.0)))
    print(Util.genTexDataCommand("xtworeachableminloss", "{:.1f}\%".format(min(xtworeachables) * 100.0)))

    print(Util.genTexDataCommand("ztworeachablemaxloss", "{:.1f}\%".format(max(ztworeachables) * 100.0)))
    print(Util.genTexDataCommand("ctworeachablemaxloss", "{:.1f}\%".format(max(ctworeachables) * 100.0)))
    print(Util.genTexDataCommand("xtworeachablemaxloss", "{:.1f}\%".format(max(xtworeachables) * 100.0)))

    print(Util.genTexDataCommand("ztworeachableavgloss", "{:.1f}\%".format(Util.average(ztworeachables) * 100.0)))
    print(Util.genTexDataCommand("ctworeachableavgloss", "{:.1f}\%".format(Util.average(ctworeachables) * 100.0)))
    print(Util.genTexDataCommand("xtworeachableavgloss", "{:.1f}\%".format(Util.average(xtworeachables) * 100.0)))

    # polycalls
    print(Util.genTexDataCommand("ztwopolycallsminloss", "{:.1f}\%".format(min(ztwopolycalls) * 100.0)))
    print(Util.genTexDataCommand("ctwopolycallsminloss", "{:.1f}\%".format(min(ctwopolycalls) * 100.0)))
    print(Util.genTexDataCommand("xtwopolycallsminloss", "{:.1f}\%".format(min(xtwopolycalls) * 100.0)))

    print(Util.genTexDataCommand("ztwopolycallsmaxloss", "{:.1f}\%".format(max(ztwopolycalls) * 100.0)))
    print(Util.genTexDataCommand("ctwopolycallsmaxloss", "{:.1f}\%".format(max(ctwopolycalls) * 100.0)))
    print(Util.genTexDataCommand("xtwopolycallsmaxloss", "{:.1f}\%".format(max(xtwopolycalls) * 100.0)))

    print(Util.genTexDataCommand("ztwopolycallsavgloss", "{:.1f}\%".format(Util.average(ztwopolycalls) * 100.0)))
    print(Util.genTexDataCommand("ctwopolycallsavgloss", "{:.1f}\%".format(Util.average(ctwopolycalls) * 100.0)))
    print(Util.genTexDataCommand("xtwopolycallsavgloss", "{:.1f}\%".format(Util.average(xtwopolycalls) * 100.0)))

    # draw an average bar graph.
    ztwoloss, ctwoloss, xtwoloss = ([] for _ in range(3))
    for i in range(len(benchmarks)):
        ztwoloss.append(Util.average([ztwofailcast[i], ztwocalledge[i], ztworeachables[i], ztwopolycalls[i]]))
        ctwoloss.append(Util.average([ctwofailcast[i], ctwocalledge[i], ctworeachables[i], ctwopolycalls[i]]))
        xtwoloss.append(Util.average([xtwofailcast[i], xtwocalledge[i], xtworeachables[i], xtwopolycalls[i]]))
    print(Util.genTexDataCommand("zipperoveralltwoprecisionloss", "{:.1f}\%".format(Util.average(ztwoloss) * 100.0)))
    print(Util.genTexDataCommand("conchoveralltwoprecisionloss", "{:.1f}\%".format(Util.average(ctwoloss) * 100.0)))
    print(Util.genTexDataCommand("debloaterxoveralltwoprecisionloss", "{:.1f}\%".format(Util.average(xtwoloss) * 100.0)))

    indp1 = np.array([0.0, 1.2, 2.4, 3.6, 4.8, 6.0, 7.2, 8.4, 9.6, 10.8, 12.0, 13.2])
    indp2 = np.array([0.3, 1.5, 2.7, 3.9, 5.1, 6.3, 7.5, 8.7, 9.9, 11.1, 12.3, 13.5])
    indp3 = np.array([0.6, 1.8, 3.0, 4.2, 5.4, 6.6, 7.8, 9.0, 10.2, 11.4, 12.6, 13.8])
    xtickInd = np.array([0.3, 1.5, 2.7, 3.9, 5.1, 6.3, 7.5, 8.7, 9.9, 11.1, 12.3, 13.5])
    width = 0.30  # the width of the bars: can also be len(x) sequence

    plt.figure(figsize=(11, 4.2))
    x1 = plt.bar(indp1, xtwoloss, width, color= 'lightgray', edgecolor='black')
    x2 = plt.bar(indp2, ctwoloss, width, color='mistyrose', edgecolor='black')
    x3 = plt.bar(indp3, ztwoloss, width, color='lightsteelblue', edgecolor='black')

    plt.yticks(np.arange(0, 0.1, 0.01), weight='bold')
    plt.xticks(xtickInd, benchmarks, rotation=10, weight='bold')
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1, decimals=0))
    for i in range(len(benchmarks)):
        plt.text(indp1[i] - 0.08, xtwoloss[i] + 0.002, "{:.1f}%".format(xtwoloss[i] * 100.0), rotation = 90)
    for i in range(len(benchmarks)):
        plt.text(indp2[i] - 0.08, ctwoloss[i] + 0.002, "{:.1f}%".format(ctwoloss[i] * 100.0), rotation = 90)
    for i in range(len(benchmarks)):
        plt.text(indp3[i] - 0.08, ztwoloss[i] + 0.002, "{:.1f}%".format(ztwoloss[i]* 100.0), rotation = 90)
    plt.legend((x1[0], x2[0], x3[0]), (r'X-2obj', r'C-2obj', r'Z-2obj'), loc='upper left',  ncol=3, prop={'weight': 'bold'})
    plt.savefig("precisionlosstwo.pdf")
    # plt.show()
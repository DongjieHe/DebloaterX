#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import util.Util as Util
import scipy.stats

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
        stwoobj = tool2outs['2o+DC']
        threeobj = tool2outs['3o']
        zthreeobj = tool2outs['Z-3o']
        cthreeobj = tool2outs['3o+D']
        xthreeobj = tool2outs['3o+DX']
        sthreeobj = tool2outs['3o+DC']
        if twoobj.analysisCompleted():
            # fail-casts
            ztwofailcast = precisionLoss(int(ci.mayFailCasts), int(twoobj.mayFailCasts), int(ztwoobj.mayFailCasts))
            ctwofailcast = precisionLoss(int(ci.mayFailCasts), int(twoobj.mayFailCasts), int(ctwoobj.mayFailCasts))
            xtwofailcast = precisionLoss(int(ci.mayFailCasts), int(twoobj.mayFailCasts), int(xtwoobj.mayFailCasts))
            stwofailcast = precisionLoss(int(ci.mayFailCasts), int(twoobj.mayFailCasts), int(stwoobj.mayFailCasts))
            print([app, 'k=2', 'fail-casts', ztwofailcast, stwofailcast, ctwofailcast, xtwofailcast])
            app2tool2failcastloss[app]['Z-2o'] = ztwofailcast
            app2tool2failcastloss[app]['2o+D'] = ctwofailcast
            app2tool2failcastloss[app]['2o+DX'] = xtwofailcast
            app2tool2failcastloss[app]['2o+DC'] = stwofailcast
            # call edges
            ztwocalledge = precisionLoss(int(ci.callEdges), int(twoobj.callEdges), int(ztwoobj.callEdges))
            ctwocalledge = precisionLoss(int(ci.callEdges), int(twoobj.callEdges), int(ctwoobj.callEdges))
            xtwocalledge = precisionLoss(int(ci.callEdges), int(twoobj.callEdges), int(xtwoobj.callEdges))
            stwocalledge = precisionLoss(int(ci.callEdges), int(twoobj.callEdges), int(stwoobj.callEdges))
            print([app, 'k=2', 'call-edges', ztwocalledge, stwocalledge, ctwocalledge, xtwocalledge])
            app2tool2calledgeloss[app]['Z-2o'] = ztwocalledge
            app2tool2calledgeloss[app]['2o+D'] = ctwocalledge
            app2tool2calledgeloss[app]['2o+DX'] = xtwocalledge
            app2tool2calledgeloss[app]['2o+DC'] = stwocalledge
            # reachables
            ztworeachables = precisionLoss(int(ci.reachMethods), int(twoobj.reachMethods), int(ztwoobj.reachMethods))
            ctworeachables = precisionLoss(int(ci.reachMethods), int(twoobj.reachMethods), int(ctwoobj.reachMethods))
            xtworeachables = precisionLoss(int(ci.reachMethods), int(twoobj.reachMethods), int(xtwoobj.reachMethods))
            stworeachables = precisionLoss(int(ci.reachMethods), int(twoobj.reachMethods), int(stwoobj.reachMethods))
            print([app, 'k=2', 'reachables', ztworeachables, stworeachables, ctworeachables, xtworeachables])
            app2tool2reachablesloss[app]['Z-2o'] = ztworeachables
            app2tool2reachablesloss[app]['2o+D'] = ctworeachables
            app2tool2reachablesloss[app]['2o+DX'] = xtworeachables
            app2tool2reachablesloss[app]['2o+DC'] = stworeachables
            # poly-calls
            ztwopolycalls = precisionLoss(int(ci.polyCalls), int(twoobj.polyCalls), int(ztwoobj.polyCalls))
            ctwopolycalls = precisionLoss(int(ci.polyCalls), int(twoobj.polyCalls), int(ctwoobj.polyCalls))
            xtwopolycalls = precisionLoss(int(ci.polyCalls), int(twoobj.polyCalls), int(xtwoobj.polyCalls))
            stwopolycalls = precisionLoss(int(ci.polyCalls), int(twoobj.polyCalls), int(stwoobj.polyCalls))
            print([app, 'k=2', 'poly-calls', ztwopolycalls, stwopolycalls, ctwopolycalls, xtwopolycalls])
            app2tool2polycallloss[app]['Z-2o'] = ztwopolycalls
            app2tool2polycallloss[app]['2o+D'] = ctwopolycalls
            app2tool2polycallloss[app]['2o+DX'] = xtwopolycalls
            app2tool2polycallloss[app]['2o+DC'] = stwopolycalls
        if threeobj.analysisCompleted():
            # fail-casts
            zthreefailcast = precisionLoss(int(ci.mayFailCasts), int(threeobj.mayFailCasts), int(zthreeobj.mayFailCasts))
            cthreefailcast = precisionLoss(int(ci.mayFailCasts), int(threeobj.mayFailCasts), int(cthreeobj.mayFailCasts))
            xthreefailcast = precisionLoss(int(ci.mayFailCasts), int(threeobj.mayFailCasts), int(xthreeobj.mayFailCasts))
            sthreefailcast = precisionLoss(int(ci.mayFailCasts), int(threeobj.mayFailCasts), int(sthreeobj.mayFailCasts))
            print([app, 'k=3', 'fail-casts', zthreefailcast, sthreefailcast, cthreefailcast, xthreefailcast])
            app2tool2failcastloss[app]['Z-3o'] = zthreefailcast
            app2tool2failcastloss[app]['3o+D'] = cthreefailcast
            app2tool2failcastloss[app]['3o+DX'] = xthreefailcast
            app2tool2failcastloss[app]['3o+DC'] = sthreefailcast
            # call edges
            zthreecalledge = precisionLoss(int(ci.callEdges), int(threeobj.callEdges), int(zthreeobj.callEdges))
            cthreecalledge = precisionLoss(int(ci.callEdges), int(threeobj.callEdges), int(cthreeobj.callEdges))
            xthreecalledge = precisionLoss(int(ci.callEdges), int(threeobj.callEdges), int(xthreeobj.callEdges))
            sthreecalledge = precisionLoss(int(ci.callEdges), int(threeobj.callEdges), int(sthreeobj.callEdges))
            print([app, 'k=3', 'call-edges', zthreecalledge, sthreecalledge, cthreecalledge, xthreecalledge])
            app2tool2calledgeloss[app]['Z-3o'] = zthreecalledge
            app2tool2calledgeloss[app]['3o+D'] = cthreecalledge
            app2tool2calledgeloss[app]['3o+DX'] = xthreecalledge
            app2tool2calledgeloss[app]['3o+DC'] = sthreecalledge
            # reachables
            zthreereachables = precisionLoss(int(ci.reachMethods), int(threeobj.reachMethods), int(zthreeobj.reachMethods))
            cthreereachables = precisionLoss(int(ci.reachMethods), int(threeobj.reachMethods), int(cthreeobj.reachMethods))
            xthreereachables = precisionLoss(int(ci.reachMethods), int(threeobj.reachMethods), int(xthreeobj.reachMethods))
            sthreereachables = precisionLoss(int(ci.reachMethods), int(threeobj.reachMethods), int(sthreeobj.reachMethods))
            print([app, 'k=3', 'reachables', zthreereachables, sthreereachables, cthreereachables, xthreereachables])
            app2tool2reachablesloss[app]['Z-3o'] = zthreereachables
            app2tool2reachablesloss[app]['3o+D'] = cthreereachables
            app2tool2reachablesloss[app]['3o+DX'] = xthreereachables
            app2tool2reachablesloss[app]['3o+DC'] = sthreereachables
            # poly-calls
            zthreepolycalls = precisionLoss(int(ci.polyCalls), int(threeobj.polyCalls), int(zthreeobj.polyCalls))
            cthreepolycalls = precisionLoss(int(ci.polyCalls), int(threeobj.polyCalls), int(cthreeobj.polyCalls))
            xthreepolycalls = precisionLoss(int(ci.polyCalls), int(threeobj.polyCalls), int(xthreeobj.polyCalls))
            sthreepolycalls = precisionLoss(int(ci.polyCalls), int(threeobj.polyCalls), int(sthreeobj.polyCalls))
            print([app, 'k=3', 'poly-calls', zthreepolycalls, sthreepolycalls, cthreepolycalls, xthreepolycalls])
            app2tool2polycallloss[app]['Z-3o'] = zthreepolycalls
            app2tool2polycallloss[app]['3o+D'] = cthreepolycalls
            app2tool2polycallloss[app]['3o+DX'] = xthreepolycalls
            app2tool2polycallloss[app]['3o+DC'] = sthreepolycalls
    return app2tool2failcastloss, app2tool2calledgeloss, app2tool2reachablesloss, app2tool2polycallloss

def dumpprecisionLossData(allPtaOutputs, benchmarks):
    app2tool2failcastloss, app2tool2calledgeloss, app2tool2reachablesloss, app2tool2polycallloss = producePrecisionLossData(allPtaOutputs)
    ztwofailcast, ctwofailcast,  xtwofailcast, stwofailcast = ([] for _ in range(4))
    ztwocalledge, ctwocalledge, xtwocalledge, stwocalledge = ([] for _ in range(4))
    ztworeachables, ctworeachables, xtworeachables, stworeachables = ([] for _ in range(4))
    ztwopolycalls, ctwopolycalls, xtwopolycalls, stwopolycalls = ([] for _ in range(4))

    zthreefailcast, cthreefailcast,  xthreefailcast,  sthreefailcast = ([] for _ in range(4))
    zthreecalledge, cthreecalledge, xthreecalledge, sthreecalledge = ([] for _ in range(4))
    zthreereachables, cthreereachables, xthreereachables, sthreereachables = ([] for _ in range(4))
    zthreepolycalls, cthreepolycalls, xthreepolycalls, sthreepolycalls = ([] for _ in range(4))
    for app in benchmarks:
        ztwofailcast.append(app2tool2failcastloss[app]['Z-2o'])
        ctwofailcast.append(app2tool2failcastloss[app]['2o+D'])
        xtwofailcast.append(app2tool2failcastloss[app]['2o+DX'])
        stwofailcast.append(app2tool2failcastloss[app]['2o+DC'])

        ztwocalledge.append(app2tool2calledgeloss[app]['Z-2o'])
        ctwocalledge.append(app2tool2calledgeloss[app]['2o+D'])
        xtwocalledge.append(app2tool2calledgeloss[app]['2o+DX'])
        stwocalledge.append(app2tool2calledgeloss[app]['2o+DC'])

        ztworeachables.append(app2tool2reachablesloss[app]['Z-2o'])
        ctworeachables.append(app2tool2reachablesloss[app]['2o+D'])
        xtworeachables.append(app2tool2reachablesloss[app]['2o+DX'])
        stworeachables.append(app2tool2reachablesloss[app]['2o+DC'])

        ztwopolycalls.append(app2tool2polycallloss[app]['Z-2o'])
        ctwopolycalls.append(app2tool2polycallloss[app]['2o+D'])
        xtwopolycalls.append(app2tool2polycallloss[app]['2o+DX'])
        stwopolycalls.append(app2tool2polycallloss[app]['2o+DC'])

        # k = 3
        if app in ['antlr', 'fop', 'hsqldb' , 'JPC']: # a temporary hack.
            zthreefailcast.append(app2tool2failcastloss[app]['Z-3o'])
            cthreefailcast.append(app2tool2failcastloss[app]['3o+D'])
            xthreefailcast.append(app2tool2failcastloss[app]['3o+DX'])
            sthreefailcast.append(app2tool2failcastloss[app]['3o+DC'])

            zthreecalledge.append(app2tool2calledgeloss[app]['Z-3o'])
            cthreecalledge.append(app2tool2calledgeloss[app]['3o+D'])
            xthreecalledge.append(app2tool2calledgeloss[app]['3o+DX'])
            sthreecalledge.append(app2tool2calledgeloss[app]['3o+DC'])

            zthreereachables.append(app2tool2reachablesloss[app]['Z-3o'])
            cthreereachables.append(app2tool2reachablesloss[app]['3o+D'])
            xthreereachables.append(app2tool2reachablesloss[app]['3o+DX'])
            sthreereachables.append(app2tool2reachablesloss[app]['3o+DC'])

            zthreepolycalls.append(app2tool2polycallloss[app]['Z-3o'])
            cthreepolycalls.append(app2tool2polycallloss[app]['3o+D'])
            xthreepolycalls.append(app2tool2polycallloss[app]['3o+DX'])
            sthreepolycalls.append(app2tool2polycallloss[app]['3o+DC'])

    # fail-casts
    print(Util.genTexDataCommand("ztwofailcastminloss", "{:.1f}\%".format(min(ztwofailcast) * 100.0)))
    print(Util.genTexDataCommand("ctwofailcastminloss", "{:.1f}\%".format(min(ctwofailcast) * 100.0)))
    print(Util.genTexDataCommand("xtwofailcastminloss", "{:.1f}\%".format(min(xtwofailcast) * 100.0)))
    print(Util.genTexDataCommand("stwofailcastminloss", "{:.1f}\%".format(min(stwofailcast) * 100.0)))

    print(Util.genTexDataCommand("ztwofailcastmaxloss", "{:.1f}\%".format(max(ztwofailcast) * 100.0)))
    print(Util.genTexDataCommand("ctwofailcastmaxloss", "{:.1f}\%".format(max(ctwofailcast) * 100.0)))
    print(Util.genTexDataCommand("xtwofailcastmaxloss", "{:.1f}\%".format(max(xtwofailcast) * 100.0)))
    print(Util.genTexDataCommand("stwofailcastmaxloss", "{:.1f}\%".format(max(stwofailcast) * 100.0)))

    print(Util.genTexDataCommand("ztwofailcastavgloss", "{:.1f}\%".format(Util.average(ztwofailcast) * 100.0)))
    print(Util.genTexDataCommand("ctwofailcastavgloss", "{:.1f}\%".format(Util.average(ctwofailcast) * 100.0)))
    print(Util.genTexDataCommand("xtwofailcastavgloss", "{:.1f}\%".format(Util.average(xtwofailcast) * 100.0)))
    print(Util.genTexDataCommand("stwofailcastavgloss", "{:.1f}\%".format(Util.average(stwofailcast) * 100.0)))

    # k = 3
    print(Util.genTexDataCommand("zthreefailcastminloss", "{:.1f}\%".format(min(zthreefailcast) * 100.0)))
    print(Util.genTexDataCommand("cthreefailcastminloss", "{:.1f}\%".format(min(cthreefailcast) * 100.0)))
    print(Util.genTexDataCommand("xthreefailcastminloss", "{:.1f}\%".format(min(xthreefailcast) * 100.0)))
    print(Util.genTexDataCommand("sthreefailcastminloss", "{:.1f}\%".format(min(sthreefailcast) * 100.0)))

    print(Util.genTexDataCommand("zthreefailcastmaxloss", "{:.1f}\%".format(max(zthreefailcast) * 100.0)))
    print(Util.genTexDataCommand("cthreefailcastmaxloss", "{:.1f}\%".format(max(cthreefailcast) * 100.0)))
    print(Util.genTexDataCommand("xthreefailcastmaxloss", "{:.1f}\%".format(max(xthreefailcast) * 100.0)))
    print(Util.genTexDataCommand("sthreefailcastmaxloss", "{:.1f}\%".format(max(sthreefailcast) * 100.0)))

    print(Util.genTexDataCommand("zthreefailcastavgloss", "{:.1f}\%".format(Util.average(zthreefailcast) * 100.0)))
    print(Util.genTexDataCommand("cthreefailcastavgloss", "{:.1f}\%".format(Util.average(cthreefailcast) * 100.0)))
    print(Util.genTexDataCommand("xthreefailcastavgloss", "{:.1f}\%".format(Util.average(xthreefailcast) * 100.0)))
    print(Util.genTexDataCommand("sthreefailcastavgloss", "{:.1f}\%".format(Util.average(sthreefailcast) * 100.0)))

    # call-edges
    print(Util.genTexDataCommand("ztwocalledgeminloss", "{:.1f}\%".format(min(ztwocalledge) * 100.0)))
    print(Util.genTexDataCommand("ctwocalledgeminloss", "{:.1f}\%".format(min(ctwocalledge) * 100.0)))
    print(Util.genTexDataCommand("xtwocalledgeminloss", "{:.1f}\%".format(min(xtwocalledge) * 100.0)))
    print(Util.genTexDataCommand("stwocalledgeminloss", "{:.1f}\%".format(min(stwocalledge) * 100.0)))

    print(Util.genTexDataCommand("ztwocalledgemaxloss", "{:.1f}\%".format(max(ztwocalledge) * 100.0)))
    print(Util.genTexDataCommand("ctwocalledgemaxloss", "{:.1f}\%".format(max(ctwocalledge) * 100.0)))
    print(Util.genTexDataCommand("xtwocalledgemaxloss", "{:.1f}\%".format(max(xtwocalledge) * 100.0)))
    print(Util.genTexDataCommand("stwocalledgemaxloss", "{:.1f}\%".format(max(stwocalledge) * 100.0)))

    print(Util.genTexDataCommand("ztwocalledgeavgloss", "{:.1f}\%".format(Util.average(ztwocalledge) * 100.0)))
    print(Util.genTexDataCommand("ctwocalledgeavgloss", "{:.1f}\%".format(Util.average(ctwocalledge) * 100.0)))
    print(Util.genTexDataCommand("xtwocalledgeavgloss", "{:.1f}\%".format(Util.average(xtwocalledge) * 100.0)))
    print(Util.genTexDataCommand("stwocalledgeavgloss", "{:.1f}\%".format(Util.average(stwocalledge) * 100.0)))

    # k = 3
    print(Util.genTexDataCommand("zthreecalledgeminloss", "{:.1f}\%".format(min(zthreecalledge) * 100.0)))
    print(Util.genTexDataCommand("cthreecalledgeminloss", "{:.1f}\%".format(min(cthreecalledge) * 100.0)))
    print(Util.genTexDataCommand("xthreecalledgeminloss", "{:.1f}\%".format(min(xthreecalledge) * 100.0)))
    print(Util.genTexDataCommand("sthreecalledgeminloss", "{:.1f}\%".format(min(sthreecalledge) * 100.0)))

    print(Util.genTexDataCommand("zthreecalledgemaxloss", "{:.1f}\%".format(max(zthreecalledge) * 100.0)))
    print(Util.genTexDataCommand("cthreecalledgemaxloss", "{:.1f}\%".format(max(cthreecalledge) * 100.0)))
    print(Util.genTexDataCommand("xthreecalledgemaxloss", "{:.1f}\%".format(max(xthreecalledge) * 100.0)))
    print(Util.genTexDataCommand("sthreecalledgemaxloss", "{:.1f}\%".format(max(sthreecalledge) * 100.0)))

    print(Util.genTexDataCommand("zthreecalledgeavgloss", "{:.1f}\%".format(Util.average(zthreecalledge) * 100.0)))
    print(Util.genTexDataCommand("cthreecalledgeavgloss", "{:.1f}\%".format(Util.average(cthreecalledge) * 100.0)))
    print(Util.genTexDataCommand("xthreecalledgeavgloss", "{:.1f}\%".format(Util.average(xthreecalledge) * 100.0)))
    print(Util.genTexDataCommand("sthreecalledgeavgloss", "{:.1f}\%".format(Util.average(sthreecalledge) * 100.0)))

    # reachables
    print(Util.genTexDataCommand("ztworeachableminloss", "{:.1f}\%".format(min(ztworeachables) * 100.0)))
    print(Util.genTexDataCommand("ctworeachableminloss", "{:.1f}\%".format(min(ctworeachables) * 100.0)))
    print(Util.genTexDataCommand("xtworeachableminloss", "{:.1f}\%".format(min(xtworeachables) * 100.0)))
    print(Util.genTexDataCommand("stworeachableminloss", "{:.1f}\%".format(min(stworeachables) * 100.0)))

    print(Util.genTexDataCommand("ztworeachablemaxloss", "{:.1f}\%".format(max(ztworeachables) * 100.0)))
    print(Util.genTexDataCommand("ctworeachablemaxloss", "{:.1f}\%".format(max(ctworeachables) * 100.0)))
    print(Util.genTexDataCommand("xtworeachablemaxloss", "{:.1f}\%".format(max(xtworeachables) * 100.0)))
    print(Util.genTexDataCommand("stworeachablemaxloss", "{:.1f}\%".format(max(stworeachables) * 100.0)))

    print(Util.genTexDataCommand("ztworeachableavgloss", "{:.1f}\%".format(Util.average(ztworeachables) * 100.0)))
    print(Util.genTexDataCommand("ctworeachableavgloss", "{:.1f}\%".format(Util.average(ctworeachables) * 100.0)))
    print(Util.genTexDataCommand("xtworeachableavgloss", "{:.1f}\%".format(Util.average(xtworeachables) * 100.0)))
    print(Util.genTexDataCommand("stworeachableavgloss", "{:.1f}\%".format(Util.average(stworeachables) * 100.0)))

    # k = 3
    print(Util.genTexDataCommand("zthreereachableminloss", "{:.1f}\%".format(min(zthreereachables) * 100.0)))
    print(Util.genTexDataCommand("cthreereachableminloss", "{:.1f}\%".format(min(cthreereachables) * 100.0)))
    print(Util.genTexDataCommand("xthreereachableminloss", "{:.1f}\%".format(min(xthreereachables) * 100.0)))
    print(Util.genTexDataCommand("sthreereachableminloss", "{:.1f}\%".format(min(sthreereachables) * 100.0)))

    print(Util.genTexDataCommand("zthreereachablemaxloss", "{:.1f}\%".format(max(zthreereachables) * 100.0)))
    print(Util.genTexDataCommand("cthreereachablemaxloss", "{:.1f}\%".format(max(cthreereachables) * 100.0)))
    print(Util.genTexDataCommand("xthreereachablemaxloss", "{:.1f}\%".format(max(xthreereachables) * 100.0)))
    print(Util.genTexDataCommand("sthreereachablemaxloss", "{:.1f}\%".format(max(sthreereachables) * 100.0)))

    print(Util.genTexDataCommand("zthreereachableavgloss", "{:.1f}\%".format(Util.average(zthreereachables) * 100.0)))
    print(Util.genTexDataCommand("cthreereachableavgloss", "{:.1f}\%".format(Util.average(cthreereachables) * 100.0)))
    print(Util.genTexDataCommand("xthreereachableavgloss", "{:.1f}\%".format(Util.average(xthreereachables) * 100.0)))
    print(Util.genTexDataCommand("sthreereachableavgloss", "{:.1f}\%".format(Util.average(sthreereachables) * 100.0)))

    # polycalls
    print(Util.genTexDataCommand("ztwopolycallsminloss", "{:.1f}\%".format(min(ztwopolycalls) * 100.0)))
    print(Util.genTexDataCommand("ctwopolycallsminloss", "{:.1f}\%".format(min(ctwopolycalls) * 100.0)))
    print(Util.genTexDataCommand("xtwopolycallsminloss", "{:.1f}\%".format(min(xtwopolycalls) * 100.0)))
    print(Util.genTexDataCommand("stwopolycallsminloss", "{:.1f}\%".format(min(stwopolycalls) * 100.0)))

    print(Util.genTexDataCommand("ztwopolycallsmaxloss", "{:.1f}\%".format(max(ztwopolycalls) * 100.0)))
    print(Util.genTexDataCommand("ctwopolycallsmaxloss", "{:.1f}\%".format(max(ctwopolycalls) * 100.0)))
    print(Util.genTexDataCommand("xtwopolycallsmaxloss", "{:.1f}\%".format(max(xtwopolycalls) * 100.0)))
    print(Util.genTexDataCommand("stwopolycallsmaxloss", "{:.1f}\%".format(max(stwopolycalls) * 100.0)))

    print(Util.genTexDataCommand("ztwopolycallsavgloss", "{:.1f}\%".format(Util.average(ztwopolycalls) * 100.0)))
    print(Util.genTexDataCommand("ctwopolycallsavgloss", "{:.1f}\%".format(Util.average(ctwopolycalls) * 100.0)))
    print(Util.genTexDataCommand("xtwopolycallsavgloss", "{:.1f}\%".format(Util.average(xtwopolycalls) * 100.0)))
    print(Util.genTexDataCommand("stwopolycallsavgloss", "{:.1f}\%".format(Util.average(stwopolycalls) * 100.0)))

    # k = 3
    print(Util.genTexDataCommand("zthreepolycallsminloss", "{:.1f}\%".format(min(zthreepolycalls) * 100.0)))
    print(Util.genTexDataCommand("cthreepolycallsminloss", "{:.1f}\%".format(min(cthreepolycalls) * 100.0)))
    print(Util.genTexDataCommand("xthreepolycallsminloss", "{:.1f}\%".format(min(xthreepolycalls) * 100.0)))
    print(Util.genTexDataCommand("sthreepolycallsminloss", "{:.1f}\%".format(min(sthreepolycalls) * 100.0)))

    print(Util.genTexDataCommand("zthreepolycallsmaxloss", "{:.1f}\%".format(max(zthreepolycalls) * 100.0)))
    print(Util.genTexDataCommand("cthreepolycallsmaxloss", "{:.1f}\%".format(max(cthreepolycalls) * 100.0)))
    print(Util.genTexDataCommand("xthreepolycallsmaxloss", "{:.1f}\%".format(max(xthreepolycalls) * 100.0)))
    print(Util.genTexDataCommand("sthreepolycallsmaxloss", "{:.1f}\%".format(max(sthreepolycalls) * 100.0)))

    print(Util.genTexDataCommand("zthreepolycallsavgloss", "{:.1f}\%".format(Util.average(zthreepolycalls) * 100.0)))
    print(Util.genTexDataCommand("cthreepolycallsavgloss", "{:.1f}\%".format(Util.average(cthreepolycalls) * 100.0)))
    print(Util.genTexDataCommand("xthreepolycallsavgloss", "{:.1f}\%".format(Util.average(xthreepolycalls) * 100.0)))
    print(Util.genTexDataCommand("sthreepolycallsavgloss", "{:.1f}\%".format(Util.average(sthreepolycalls) * 100.0)))

    ztwoloss, ctwoloss, xtwoloss, stwoloss = ([] for _ in range(4))
    for i in range(len(benchmarks)):
        ztwoloss.append(Util.average([ztwofailcast[i], ztwocalledge[i], ztworeachables[i], ztwopolycalls[i]]))
        ctwoloss.append(Util.average([ctwofailcast[i], ctwocalledge[i], ctworeachables[i], ctwopolycalls[i]]))
        xtwoloss.append(Util.average([xtwofailcast[i], xtwocalledge[i], xtworeachables[i], xtwopolycalls[i]]))
        stwoloss.append(Util.average([stwofailcast[i], stwocalledge[i], stworeachables[i], stwopolycalls[i]]))
    print(Util.genTexDataCommand("zipperoveralltwoprecisionloss", "{:.1f}\%".format(Util.average(ztwoloss) * 100.0)))
    print(Util.genTexDataCommand("conchoveralltwoprecisionloss", "{:.1f}\%".format(Util.average(ctwoloss) * 100.0)))
    print(Util.genTexDataCommand("debloaterxoveralltwoprecisionloss", "{:.1f}\%".format(Util.average(xtwoloss) * 100.0)))
    print(Util.genTexDataCommand("collectionoveralltwoprecisionloss", "{:.1f}\%".format(Util.average(stwoloss) * 100.0)))

    # k = 3
    zthreeloss, cthreeloss, xthreeloss, sthreeloss = ([] for _ in range(4))
    for i in range(len(zthreefailcast)):
        zthreeloss.append(Util.average([zthreefailcast[i], zthreecalledge[i], zthreereachables[i], zthreepolycalls[i]]))
        cthreeloss.append(Util.average([cthreefailcast[i], cthreecalledge[i], cthreereachables[i], cthreepolycalls[i]]))
        xthreeloss.append(Util.average([xthreefailcast[i], xthreecalledge[i], xthreereachables[i], xthreepolycalls[i]]))
        sthreeloss.append(Util.average([sthreefailcast[i], sthreecalledge[i], sthreereachables[i], sthreepolycalls[i]]))
    print(Util.genTexDataCommand("zipperoverallthreeprecisionloss", "{:.1f}\%".format(Util.average(zthreeloss) * 100.0)))
    print(Util.genTexDataCommand("conchoverallthreeprecisionloss", "{:.1f}\%".format(Util.average(cthreeloss) * 100.0)))
    print(Util.genTexDataCommand("debloaterxoverallthreeprecisionloss", "{:.1f}\%".format(Util.average(xthreeloss) * 100.0)))
    print(Util.genTexDataCommand("collectionoverallthreeprecisionloss", "{:.1f}\%".format(Util.average(sthreeloss) * 100.0)))

    # significance checking
    d1 = xtwoloss[0:5]
    d1 = d1 + xthreeloss[0:3]
    d2 = xtwoloss[5:7]
    d2 = d2 + xthreeloss[-1:]
    d3 = xtwoloss[-5:]
    print()
    print("LOSS:")
    print(d1)
    print(d2)
    print(d3)
    print(Util.genTexDataCommand("xoverallprecisionlossindacaposix", "{:.1f}\%".format(Util.average(d1) * 100.0)))
    print(Util.genTexDataCommand("xoverallprecisionlossinthirdapp", "{:.1f}\%".format(Util.average(d2) * 100.0)))
    print(Util.genTexDataCommand("xoverallprecisionlossindacaponine", "{:.1f}\%".format(Util.average(d3) * 100.0)))
    print()

    # draw an average bar graph.
    indp1 = np.array([0.0, 1.2, 2.4, 3.6, 4.8, 6.0, 7.2, 8.4, 9.6, 10.8, 12.0, 13.2])
    indp2 = np.array([0.25, 1.45, 2.65, 3.85, 5.05, 6.25, 7.45, 8.65, 9.85, 11.05, 12.25, 13.45])
    indp3 = np.array([0.5, 1.7, 2.9, 4.1, 5.3, 6.5, 7.7, 8.9, 10.1, 11.3, 12.5, 13.7])
    indp4 = np.array([0.75, 1.95, 3.15, 4.35, 5.55, 6.75, 7.95, 9.15, 10.35, 11.55, 12.75, 13.95])
    xtickInd = np.array([0.375, 1.575, 2.775, 3.975, 5.175, 6.375, 7.575, 8.775, 9.975, 11.175, 12.375, 13.575])
    width = 0.25  # the width of the bars: can also be len(x) sequence

    plt.figure(figsize=(11, 2.2))
    x1 = plt.bar(indp1, xtwoloss, width, color= 'lightgray', edgecolor='black')
    x2 = plt.bar(indp2, ctwoloss, width, color='mistyrose', edgecolor='black')
    x3 = plt.bar(indp3, ztwoloss, width, color='lightsteelblue', edgecolor='black')
    x4 = plt.bar(indp4, stwoloss, width, color='wheat', edgecolor='black')

    plt.yticks(np.arange(0, 0.14, 0.01), weight='bold')
    plt.xticks(xtickInd, benchmarks, weight='bold', fontsize = 8)
    plt.tick_params(axis='y', labelsize=8)
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1, decimals=0))
    font = {'size': 6, 'weight':'bold'}
    for i in range(len(benchmarks)):
        plt.text(indp1[i] - 0.08, xtwoloss[i] + 0.002, "{:.1f}%".format(xtwoloss[i] * 100.0), rotation = 90, fontdict = font)
    for i in range(len(benchmarks)):
        plt.text(indp2[i] - 0.08, ctwoloss[i] + 0.002, "{:.1f}%".format(ctwoloss[i] * 100.0), rotation = 90, fontdict = font)
    for i in range(len(benchmarks)):
        plt.text(indp3[i] - 0.08, ztwoloss[i] + 0.002, "{:.1f}%".format(ztwoloss[i]* 100.0), rotation = 90, fontdict = font)
    for i in range(len(benchmarks)):
        plt.text(indp4[i] - 0.08, stwoloss[i] + 0.002, "{:.1f}%".format(stwoloss[i]* 100.0), rotation = 90, fontdict = font)
    plt.legend((x1[0], x2[0], x3[0], x4[0]), (r'X-2obj', r'C-2obj', r'Z-2obj', r'S-2obj'), loc='upper center',  ncol=4, prop={'size': 8, 'weight': 'bold'})
    plt.savefig("precisionlosstwo.pdf")
    # plt.show()
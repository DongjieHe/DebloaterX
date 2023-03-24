#!/usr/bin/env python3

import util.Util as Util

# analysisList = ['insens', '2o', 'Z-2o', '2o+D', '2o+DX', '3o', 'Z-3o', '3o+D', '3o+DX']
def produceSpeedupData(allPtaOutputs, benchmarks):
    print("eoweoewoew")
    #
    app2tool2outs = Util.buildApp2Tool2PtaOutputMap(allPtaOutputs)
    app2tool2speedups = {}
    for app in app2tool2outs:
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

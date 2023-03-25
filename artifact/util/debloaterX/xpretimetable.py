#!/usr/bin/env python3

import util.Util as Util
import util.Tex as Tex
import scipy.stats

def buildAppNameToTimeList(app2outputs):
    app2times = {}
    for app in app2outputs:
        ptaOutputs = app2outputs[app]
        anaName2Obj = Util.buildAnalysisNameToObjMap(ptaOutputs)
        if anaName2Obj['Z-2o'].preAnalysisTime == '':
            print(app + "why???")
            anaName2Obj['Z-2o'].dump()
        zipperTime = float(anaName2Obj['Z-2o'].preAnalysisTime)
        debloaterXTime = float(anaName2Obj['2o+DX'].preAnalysisTime)
        conchTime = float(anaName2Obj['2o+D'].preAnalysisTime)
        sparkTime = float(anaName2Obj['insens'].analysisTime)
        app2times[app] = [round(sparkTime, 1), round(zipperTime, 1), round(conchTime, 1), round(debloaterXTime, 1)]
    return app2times

def buildToolNameToTimeByAppOrder(app2times, appOrderList, timeOrderList):
    ret = {}
    for i in range(len(timeOrderList)):
        tool = timeOrderList[i]
        mList = []
        for app in appOrderList:
            mTime = app2times[app][i]
            mList.append(mTime)
        ret[tool] = mList
    return ret

def genPretimeTable(tool2appstime, benchmarks):
    # classify by App name.
    texContent = genTableHeadPart(benchmarks)
    sparkPreTime = tool2appstime['spark']
    zipperPreTime = tool2appstime['zipper']
    conchPreTime = tool2appstime['conch']
    debloaterXPreTime = tool2appstime['debloaterX']
    print(Util.genTexDataCommand("gmeansparktime", "{:.1f}".format(scipy.stats.gmean(sparkPreTime))))
    print(Util.genTexDataCommand("gmeanzipperpretime", "{:.1f}".format(scipy.stats.gmean(zipperPreTime))))
    print(Util.genTexDataCommand("gmeanconchpretime", "{:.1f}".format(scipy.stats.gmean(conchPreTime))))
    print(Util.genTexDataCommand("gmeandebloaterxpretime", "{:.1f}".format(scipy.stats.gmean(debloaterXPreTime))))

    texContent += '\\textsc{Spark}'
    for i in sparkPreTime:
        texContent += '\t &' + str(i)
    texContent += '\\\\ \n'

    texContent += '\\rowcolor{lightgray} \\textsc{DebloaterX}'
    for i in debloaterXPreTime:
        texContent += '\t &' + str(i)
    texContent += '\\\\ \n'

    texContent += '\\textsc{Zipper}'
    for i in zipperPreTime:
        texContent += '\t &' + str(i)
    texContent += '\\\\ \n'

    texContent += '\\textsc{Conch}'
    for i in conchPreTime:
        texContent += '\t &' + str(i)
    texContent += '\\\\ \\bottomrule\n'
    texContent += Tex.genTableTailPart()
    return texContent

def genTableHeadPart(benchmarks):
    headPart = [
        r"\begin{table}[tbp]",
        r"\centering",
        r"\caption{Times spent by \textsc{Spark} and pre-analyses in seconds.}",
        r"\label{table:pretime}",
        r"\scalebox{0.75}{",
        r"\begin{tabular}{@{} c ",
    ]

    ret = "\n".join(headPart)
    for _ in range(len(benchmarks) + 1):
        ret += " r "
    ret += "@{}}	\\toprule \n"
    ret += "\t  \t "
    for elem in benchmarks:
        ret += "& " + elem + " \t "
    # ret += "& Avg \t "
    ret += "\\\\ \\midrule\n"
    return ret


timeOrderList = ['spark', 'zipper', 'conch', 'debloaterX']


def genDebloaterXPretimeTable(allPtaOutputs, outputfile, benchmarks):
    ret = Util.classifyByAppName(allPtaOutputs)
    app2times = buildAppNameToTimeList(ret)
    tool2appstime = buildToolNameToTimeByAppOrder(app2times, benchmarks, timeOrderList)
    texContent = Tex.genDocHeadPart()
    texContent += genPretimeTable(tool2appstime, benchmarks)
    texContent += Tex.genDocTailPart()
    f = open(outputfile, "w")
    f.write(texContent)
    f.close()
#!/usr/bin/env python3

import util.Tex as Tex
import util.Util as Util
from util.common import TOOLNAMEMAP


def plainStyle(analysisList):
    ret = ''
    for i in range(len(analysisList)):
        ret += " r |"
    ret += "@{}}	\\hline \n"
    ret += "\t Benchmark \t & Metrics \t "
    for elem in analysisList:
        ret += "& " + TOOLNAMEMAP[elem] + " \t "
    ret += "\\\\ \\hline\n"
    return ret

def paperStyle(analysisList):
    ret = ''
    x = int(len(analysisList)  / 2)
    for i in range(len(analysisList)):
        if (i % x) == 0:
            if i != 0:
                if i == len(analysisList) - 1:
                    ret += " >{\columncolor{lightgray!35}} r |"
                else:
                    ret += " >{\columncolor{lightgray!35}} r ||"
            else:
                ret += " >{\columncolor{lightgray!10}} r ||"
        else:
            ret += " r |"
    ret += "@{}}	\\hline \n"
    ret += "\t Program \t & Metrics \t "
    for elem in analysisList:
        ret += "& " + TOOLNAMEMAP[elem] + " \t "
    ret += "\\\\ \\hline\n"
    return ret

# latex code for table head
def genTableHeadPart(analysisList, caption):
    headPart = [
        r"\begin{table}[hbtp]",
        r"\centering",
        r"\caption{" + caption + "}",
        r"\label{table:main}",
        r"\scalebox{0.75}{",
        r"\begin{tabular}{@{}|c|l||",
    ]

    ret = "\n".join(headPart)
    # ret = ret + plainStyle(analysisList)
    ret = ret + paperStyle(analysisList)
    return ret


# generate latex code for table body.
def genTableTexContentForOneApp(app, ptaOutputs, analysisList):
    # ordered by analysis name
    anaName2Obj = Util.buildAnalysisNameToObjMap(ptaOutputs)
    times = ['', 'Time (s)']
    casts = ['', '\#fail-casts']
    edges = ['', '\#call-edges']
    reachs = ['', '\#reachables']
    aliaspairs = ['', '\#aliases']
    poly = ['', '\#poly-calls']
    allAnaList = []
    allAnaList.extend(analysisList)
    for elem in allAnaList:
        if elem in anaName2Obj and anaName2Obj[elem].analysisCompleted():
            ptaOutput = anaName2Obj[elem]
            timeStr = '%.1f' % ptaOutput.analysisTime
            times.append(timeStr)
            casts.append(ptaOutput.mayFailCasts)
            edges.append(ptaOutput.callEdges)
            reachs.append(ptaOutput.reachMethods)
            aliaspairs.append(ptaOutput.aliases)
            poly.append(ptaOutput.polyCalls)
        else:
            if elem in OoT and app in OoT[elem]:
                times.append('\\textcolor{blue}{\\textbf{OoT}}')
            else:
                times.append('\\textcolor{red}{\\textbf{OoM}}')
            casts.append('-')
            edges.append('-')
            reachs.append('-')
            aliaspairs.append('-')
            poly.append('-')

    ret = "\t &".join(times) + "\\\\ \n"
    ret += "\t &".join(casts) + "\\\\ \n"
    ret += "\t &".join(edges) + "\\\\ \n"
    ret += "\t &".join(reachs) + "\\\\ \n"
    ret += "\t &".join(aliaspairs) + "\\\\ \n"
    ret += '\multirow{-5}{*}{' + app + '}' + "\t &".join(poly) + "\\\\ \\hline\n"
    return ret


# input should be a list of PTAOutput instances.
def genTable(allPtaOutput, benchmarks, analysisList, caption):
    # classify by App name.
    texContent = genTableHeadPart(analysisList, caption)
    ret = Util.classifyByAppName(allPtaOutput)
    for app in benchmarks:
        if app not in ret:
            continue
        ptaOutputs = ret[app]
        texContent += genTableTexContentForOneApp(app, ptaOutputs, analysisList)
    texContent += Tex.genTableTailPart()
    return texContent


def genDebloaterXClientTable(allPtaOutput, outputfile, benchmarks, analysisList, caption):
    texContent = Tex.genDocHeadPart()
    texContent += genTable(allPtaOutput, benchmarks, analysisList, caption)
    texContent += Tex.genDocTailPart()
    f = open(outputfile, "w")
    f.write(texContent)
    f.close()

def mainStyle(analysisList):
    ret = ''
    x = int(len(analysisList)  / 2)
    for i in range(len(analysisList)):
        if (i % x) == 0:
            if i != 0:
                if i == len(analysisList) - 1:
                    ret += " >{\columncolor{lightgray!35}} r |"
                else:
                    ret += " >{\columncolor{lightgray!35}} r ||"
            else:
                ret += " >{\columncolor{lightgray!10}} r ||"
        else:
            ret += " r |"
    ret += "@{}}	\\hline \n"
    ret += "\t \multicolumn{2}{|c|}{Program} \t & Metrics \t "
    for elem in analysisList:
        ret += "& " + TOOLNAMEMAP[elem] + " \t "
    ret += "\\\\ \\hline\n"
    return ret

# latex code for table head
def genMainTableHeadPart(analysisList, caption):
    headPart = [
        r"\begin{table}[hbtp]",
        r"\centering",
        r"\caption{" + caption + "}",
        r"\label{table:main}",
        r"\scalebox{0.75}{",
        r"\begin{tabular}{@{}|c|c|l||",
    ]

    ret = "\n".join(headPart)
    # ret = ret + plainStyle(analysisList)
    ret = ret + mainStyle(analysisList)
    return ret


OoT = {
    '3o': ['bloat'],
    '3o+D': ['checkstyle'],
    'E-3o': ['checkstyle', 'findbugs'],
    'Z-3o': ['checkstyle'],
}
# generate latex code for table body.
def genMainTableTexContentForOneApp(app, ptaOutputs, analysisList, x, categoryName):
    # ordered by analysis name
    anaName2Obj = Util.buildAnalysisNameToObjMap(ptaOutputs)
    times = ['', '', 'Time (s)']
    casts = ['', '', '\#fail-casts']
    edges = ['', '', '\#call-edges']
    reachs = ['', '', '\#reachables']
    poly = ['', '\#poly-calls']
    aliaspairs = ['', '', '\#aliases']
    allAnaList = []
    allAnaList.extend(analysisList)
    for elem in allAnaList:
        if elem in anaName2Obj and anaName2Obj[elem].analysisCompleted():
            ptaOutput = anaName2Obj[elem]
            timeStr = '%.1f' % ptaOutput.analysisTime
            times.append(timeStr)
            casts.append(ptaOutput.mayFailCasts)
            edges.append(ptaOutput.callEdges)
            reachs.append(ptaOutput.reachMethods)
            poly.append(ptaOutput.polyCalls)
            aliaspairs.append(ptaOutput.aliases)
        else:
            if elem in OoT and app in OoT[elem]:
                times.append('\\textcolor{blue}{\\textbf{OoT}}')
            else:
                times.append('\\textcolor{red}{\\textbf{OoM}}')
            casts.append('-')
            edges.append('-')
            reachs.append('-')
            poly.append('-')
            aliaspairs.append('')

    ret = "\t &".join(times) + "\\\\ \n"
    ret += "\t &".join(casts) + "\\\\ \n"
    ret += "\t &".join(edges) + "\\\\ \n"
    ret += "\t &".join(reachs) + "\\\\ \n"
    # ret += "\t &".join(aliaspairs) + "\\\\ \n"
    if x == 0:
        ret += "\t &"
        ret += '\multirow{-5}{*}{' + app + '}' + "\t &".join(poly) + "\\\\ \\cline{2-" + str(len(analysisList) + 3) + "}\n"
    else:
        ret += "\t \multirow{-" + str(x) + '}{*}{\\rotatebox[origin=c]{90}{' + categoryName + '}} & '
        ret += '\multirow{-5}{*}{' + app + '}' + "\t &".join(poly) + "\\\\ \\hline\n"
    return ret

def genMainTable(allPtaOutput, bench06, thirdApps, bench09, analysisList, caption):
    # classify by App name.
    texContent = genMainTableHeadPart(analysisList, caption)
    ret = Util.classifyByAppName(allPtaOutput)
    i = 0
    for app in bench06:
        i = i + 1
        if app not in ret:
            continue
        ptaOutputs = ret[app]
        if i == len(bench06):
            texContent += genMainTableTexContentForOneApp(app, ptaOutputs, analysisList, i * 5, 'DaCapo 2006')
        else:
            texContent += genMainTableTexContentForOneApp(app, ptaOutputs, analysisList, 0, '')
    texContent += "\\hline\n"
    i = 0
    for app in thirdApps:
        i = i + 1
        if app not in ret:
            continue
        ptaOutputs = ret[app]
        if i == len(thirdApps):
            texContent += genMainTableTexContentForOneApp(app, ptaOutputs, analysisList, i * 5, 'Non-DaCapo Apps')
        else:
            texContent += genMainTableTexContentForOneApp(app, ptaOutputs, analysisList, 0, '')
    texContent += "\\hline\n"
    i = 0
    for app in bench09:
        i = i + 1
        if app not in ret:
            continue
        ptaOutputs = ret[app]
        if i == len(bench09):
            texContent += genMainTableTexContentForOneApp(app, ptaOutputs, analysisList, i * 5, 'DaCapo-9.12')
        else:
            texContent += genMainTableTexContentForOneApp(app, ptaOutputs, analysisList, 0, '')
    texContent += Tex.genTableTailPart()
    return texContent

def genDebloaterXMainClientTable(allPtaOutput, outputfile, bench06, thirdApps, bench09, analysisList, caption):
    texContent = Tex.genDocHeadPart()
    texContent += genMainTable(allPtaOutput, bench06, thirdApps, bench09, analysisList, caption)
    texContent += Tex.genDocTailPart()
    f = open(outputfile, "w")
    f.write(texContent)
    f.close()
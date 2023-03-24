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
        print(i)
        if (i % x) == 0:
            if i != 0:
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
    allAnaList = []
    allAnaList.extend(analysisList)
    for elem in allAnaList:
        if elem in anaName2Obj:
            ptaOutput = anaName2Obj[elem]
            timeStr = '%.1f' % ptaOutput.analysisTime
            times.append(timeStr)
            casts.append(ptaOutput.mayFailCasts)
            edges.append(ptaOutput.callEdges)
            reachs.append(ptaOutput.reachMethods)
            aliaspairs.append(ptaOutput.aliases)
        else:
            times.append('')
            casts.append('')
            edges.append('')
            reachs.append('')
            aliaspairs.append('')

    ret = "\t &".join(times) + "\\\\ \n"
    ret += "\t &".join(casts) + "\\\\ \n"
    ret += "\t &".join(edges) + "\\\\ \n"
    ret += "\t &".join(reachs) + "\\\\ \n"
    ret += '\multirow{-5}{*}{' + app + '}' + "\t &".join(aliaspairs) + "\\\\ \\hline\n"
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
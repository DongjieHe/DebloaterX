#!/usr/bin/env python3
import os
from util.debloaterX.xinfo import Xinfo
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import util.Util as Util
import scipy.stats

def loadXinfos(benchmarks, ptaOutputPath):
    allOutput = []
    for r, d, f in os.walk(ptaOutputPath):
        for file in f:
            path = os.path.join(r, file)
            appName = path[path.rfind('/') + 1: path.rfind('_')]
            analysisName = file[file.rfind('_') + 1: -4]
            if appName in benchmarks and analysisName == '2o+DX':
                xinfo = Xinfo()
                xinfo.parseXinfo(path)
                allOutput.append(xinfo)
    return allOutput

def buildApp2Xinfo(xinfos):
    ret = {}
    for elem in xinfos:
        ret[elem.app] = elem
    return ret

def drawDifferentObjsRatioBar(xinfos, benchmarks):
    app2xinfo = buildApp2Xinfo(xinfos)
    allObj, containers, cdobjs, conchcdobjs = ([] for _ in range(4))
    for app in benchmarks:
        xinfo = app2xinfo[app]
        allObj.append(1.0)
        containers.append(xinfo.containernum * 1.0 / xinfo.heapnum)
        cdobjs.append(xinfo.cdobjnum * 1.0 / xinfo.heapnum)
        conchcdobjs.append(xinfo.conchcdobjnum * 1.0 / xinfo.heapnum)

    # dump data
    print(Util.genTexDataCommand("gmeancontainers", "{:.1f}\%".format(scipy.stats.gmean(containers) * 100.0)))
    print(Util.genTexDataCommand("gmeanctxdobjs", "{:.1f}\%".format(scipy.stats.gmean(cdobjs) * 100.0)))
    print(Util.genTexDataCommand("gmeanctxidobjs", "{:.1f}\%".format((1.0 - scipy.stats.gmean(cdobjs)) * 100.0)))
    print(Util.genTexDataCommand("gmeanconchctxdobjs", "{:.1f}\%".format(scipy.stats.gmean(conchcdobjs) * 100.0)))
    # draw bar
    indp1 = np.array([0.0, 1.2, 2.4, 3.6, 4.8, 6.0, 7.2, 8.4, 9.6, 10.8, 12.0, 13.2])
    indp2 = np.array([0.3, 1.5, 2.7, 3.9, 5.1, 6.3, 7.5, 8.7, 9.9, 11.1, 12.3, 13.5])
    indp3 = np.array([0.6, 1.8, 3.0, 4.2, 5.4, 6.6, 7.8, 9.0, 10.2, 11.4, 12.6, 13.8])
    xtickInd = np.array([0.3, 1.5, 2.7, 3.9, 5.1, 6.3, 7.5, 8.7, 9.9, 11.1, 12.3, 13.5])
    width = 0.30  # the width of the bars: can also be len(x) sequence

    plt.figure(figsize=(11, 2.2))
    x1 = plt.bar(indp1, allObj, width, color= 'lightskyblue', edgecolor='black')
    x2 = plt.bar(indp2, containers, width, color='palegoldenrod', edgecolor='black')
    x3 = plt.bar(indp3, cdobjs, width, color='peachpuff', edgecolor='black')

    plt.yticks(np.arange(0, 1.08, 0.1), weight='bold')
    plt.xticks(xtickInd, benchmarks, rotation=0, weight='bold')
    plt.tick_params(axis='x', labelsize=8)
    plt.tick_params(axis='y', labelsize=8)
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1, decimals=0))
    font = {'size': 6, 'weight': 'bold'}
#     for i in range(len(benchmarks)):
#         plt.text(indp1[i] - 0.28, allObj[i] + 0.02, "{:.0f}%".format(allObj[i] * 100.0), rotation = 0, fontsize=8)
    for i in range(len(benchmarks)):
        plt.text(indp2[i] - 0.08, containers[i] + 0.02, "{:.1f}%".format(containers[i] * 100.0), rotation = 90, fontdict = font)
    for i in range(len(benchmarks)):
        plt.text(indp3[i] - 0.08, cdobjs[i] + 0.02, "{:.1f}%".format(cdobjs[i]* 100.0), rotation = 90, fontdict = font)
    plt.legend((x1[0], x2[0], x3[0]), (r'All Objects', r'Container Objects', r'Context-Dependent Objects'), fontsize = 8, loc='upper center', bbox_to_anchor=(0.5, 1.17), ncol=3, prop={'size': 8, 'weight': 'bold'})
    plt.savefig("diffObjRatioBar.pdf")
    # plt.show()

def drawConainerPatternBar(xinfos, benchmarks):
    app2xinfo = buildApp2Xinfo(xinfos)
    inners, wrappers, factorys = ([] for _ in range(3))
    for app in benchmarks:
        xinfo = app2xinfo[app]
        inners.append(xinfo.innernum * 1.0 / xinfo.heapnum)
        wrappers.append(xinfo.wrappernum * 1.0 / xinfo.heapnum)
        factorys.append(xinfo.factorynum * 1.0 / xinfo.heapnum)

    # dump data
    print(Util.genTexDataCommand("gmeaninners", "{:.1f}\%".format(scipy.stats.gmean(inners) * 100.0)))
    print(Util.genTexDataCommand("gmeanwrappers", "{:.1f}\%".format(scipy.stats.gmean(wrappers) * 100.0)))
    print(Util.genTexDataCommand("gmeanfactorys", "{:.1f}\%".format(scipy.stats.gmean(factorys) * 100.0)))
    # draw bars
    indp1 = np.array([0.0, 1.2, 2.4, 3.6, 4.8, 6.0, 7.2, 8.4, 9.6, 10.8, 12.0, 13.2])
    indp2 = np.array([0.3, 1.5, 2.7, 3.9, 5.1, 6.3, 7.5, 8.7, 9.9, 11.1, 12.3, 13.5])
    indp3 = np.array([0.6, 1.8, 3.0, 4.2, 5.4, 6.6, 7.8, 9.0, 10.2, 11.4, 12.6, 13.8])
    xtickInd = np.array([0.3, 1.5, 2.7, 3.9, 5.1, 6.3, 7.5, 8.7, 9.9, 11.1, 12.3, 13.5])
    width = 0.30  # the width of the bars: can also be len(x) sequence

    plt.figure(figsize=(11, 2.2))
    x1 = plt.bar(indp1, inners, width, hatch='////', linewidth = 0.1, color= 'peachpuff', edgecolor='black')
    x2 = plt.bar(indp2, wrappers, width, hatch='oooo', linewidth = 0.1, color='peachpuff', edgecolor='black')
    x3 = plt.bar(indp3, factorys, width, hatch='\\\\\\\\', linewidth = 0.1, color='peachpuff', edgecolor='black')

    plt.yticks(np.arange(0, 0.11, 0.01), weight='bold')
    plt.xticks(xtickInd, benchmarks, rotation=0, weight='bold')
    plt.tick_params(axis='x', labelsize=8)
    plt.tick_params(axis='y', labelsize=8)
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1, decimals=0))
    font = {'size': 6, 'weight': 'bold'}
    for i in range(len(benchmarks)):
        plt.text(indp1[i] - 0.08, inners[i] + 0.0018, "{:.1f}%".format(inners[i] * 100.0), rotation = 90, fontdict = font)
    for i in range(len(benchmarks)):
        plt.text(indp2[i] - 0.08, wrappers[i] + 0.0018, "{:.1f}%".format(wrappers[i] * 100.0), rotation = 90, fontdict = font)
    for i in range(len(benchmarks)):
        plt.text(indp3[i] - 0.08, factorys[i] + 0.0018, "{:.1f}%".format(factorys[i]* 100.0), rotation = 90, fontdict = font)
    plt.legend((x1[0], x2[0], x3[0]), (r'Inner Containers', r'Container Wrappers', r'Factory-Created Containers'), loc='upper center', bbox_to_anchor=(0.5, 1.17), ncol=3, prop={'size':8, 'weight': 'bold'})
    plt.savefig("containerPatternBar.pdf")
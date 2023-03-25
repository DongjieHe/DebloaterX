#!/usr/bin/env python3


'''
Xinfo is an object that is specifically designed to record information of DebloaterX.
'''

class Xinfo(object):
    def __init__(self):
        self.app = ''
        self.analysisName = ''
        self.heapnum = -1
        self.containernum = -1
        self.cdobjnum = -1
        self.factorynum = -1
        self.wrappernum = -1
        self.innernum = -1
        self.conchcdobjnum = -1

    def parseAppName(self, file):
            self.app = file[file.rfind('/') + 1: file.rfind('_')]

    def parseAnalysisName(self, file):
        self.analysisName = file[file.rfind('_') + 1: -4]

    def parseXinfo(self, file):
        self.parseAppName(file)
        self.parseAnalysisName(file)
        f = open(file)
        for line in f:
            ln = line.strip()
            if '#OBJECTS:' in ln:
                self.heapnum = int(ln[ln.find(':') + 1:].strip())
            if '#Container:' in ln:
                self.containernum = int(ln[ln.find(':') + 1:].strip())
            if '#CS:' in ln:
                tmp = int(ln[ln.find(':') + 1:].strip())
                if self.cdobjnum == -1:
                    self.cdobjnum = tmp
                else:
                    self.cdobjnum = min(self.cdobjnum, tmp)
                if self.conchcdobjnum == -1:
                    self.conchcdobjnum = tmp
                else:
                    self.conchcdobjnum = max(self.conchcdobjnum, tmp)
            if '#ContainerFactory:' in ln:
                self.factorynum = int(ln[ln.find(':') + 1:].strip())
            if '#ContainerWrapper:' in ln:
                self.wrappernum = int(ln[ln.find(':') + 1:].strip())
            if '#InnerContainer:' in ln:
                self.innernum = int(ln[ln.find(':') + 1:].strip())

    def dump(self):
        print("APP:" + self.app)
        print("AnalysisName:" + self.analysisName)
        print("#Objects: %d" % self.heapnum)
        print("#Containers: %d" % self.containernum)
        print("#CSOBJ: %d" % self.cdobjnum)
        print("#Factory: %d" % self.factorynum)
        print("#Wrappers: %d" % self.wrappernum)
        print("#Inners: %d" % self.innernum)
        print("#ConchCSOBJ: %d" % self.conchcdobjnum)

# x = Xinfo()
# x.parseXinfo("/Users/dongjie/Documents/Work/qilin/artifact/output/run1/antlr_2o+DX.txt")
# x.dump()
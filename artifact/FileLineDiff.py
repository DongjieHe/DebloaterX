#!/usr/bin/env python
import sys


def readLines(fileName):
    f = open(fileName, 'r')
    lines = f.readlines()
    return lines


def diff(lines1, lines2):
    ldiff = list(set(lines1) - set(lines2))
    rdiff = list(set(lines2) - set(lines1))
    return (ldiff, rdiff)


def fileDiff(f1, f2):
    line1 = readLines(f1)
    line2 = readLines(f2)
    return diff(line1, line2)


if __name__ == '__main__':
    # do something here
    f1 = sys.argv[1]
    f2 = sys.argv[2]
    (ldiffs, rdiffs) = fileDiff(f1, f2)
    print("lines in " + f1 + "but not in " + f2)
    for l in ldiffs:
        print("\t" + l.strip())
    print("lines in " + f2 + "but not in " + f1)
    for l in rdiffs:
        print("\t" + l.strip())

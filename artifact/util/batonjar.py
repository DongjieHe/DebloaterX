#!/usr/bin/env python3

BENCHMARKS = ['briss', 'columba', 'eclipse', 'gruntspud', 'jedit', 'pmd', 'soot', 'h2',
              'galleon', 'heritrix', 'jasperreports']

MAINCLASSES = {
    'briss': "at.laborg.briss.Briss", 
    'columba': "org.columba.core.main.Main", 
    'eclipse': "dacapo.eclipse.Main", 
    'gruntspud': "gruntspud.standalone.JDK13GruntspudHost", 
    'jedit': "org.gjt.sp.jedit.jEdit", 
    'pmd': "net.sourceforge.pmd.PMD", 
    'soot': "soot.Main", 
    'h2': "Harness",
    'galleon': "org.lnicholls.galleon.server.Server", 
    'heritrix':"org.archive.crawler.Heritrix", 
    'jasperreports': "net.sf.jasperreports.view.JasperViewer"
}

APPPATH = {
    'briss': "benchmarks/baton-jars/briss/briss-0.9.jar", 
    'columba': "benchmarks/baton-jars/columba/1.4/columba.jar", 
    'eclipse': "benchmarks/baton-jars/eclipse/eclipse.jar", 
    'gruntspud': "benchmarks/baton-jars/gruntspud/GruntspudSA.jar", 
    'jedit': "benchmarks/baton-jars/jedit/3.0/jedit.jar", 
    'pmd': "benchmarks/baton-jars/pmd/5.3.2/pmd-core-5.3.2.jar", 
    'soot': "benchmarks/baton-jars/soot/2.3.0/sootclasses-2.3.0.jar", 
    'h2': "benchmarks/baton-jars/h2/h2.jar",
    'galleon': "benchmarks/baton-jars/galleon-2.3.0/lib/galleon.jar", 
    'heritrix': "benchmarks/baton-jars/heritrix-1.14.4/heritrix.jar", 
    'jasperreports': "benchmarks/baton-jars/jasperreports-3.7.4/jasperreports.jar"
}

LIBPATH = {
    'briss': "benchmarks/baton-jars/briss/", 
    'columba': "benchmarks/baton-jars/columba/1.4/lib/", 
    'eclipse': "benchmarks/baton-jars/eclipse/eclipse-deps.jar", 
    'gruntspud': "benchmarks/baton-jars/gruntspud/", 
    'jedit': "benchmarks/baton-jars/jedit/3.0/jars/", 
    'pmd': "benchmarks/baton-jars/pmd/5.3.2/", 
    'soot': "benchmarks/baton-jars/soot/2.3.0/", 
    'h2': "benchmarks/baton-jars/h2/h2-deps.jar",
    'galleon': "benchmarks/baton-jars/galleon-2.3.0/lib/", 
    'heritrix': "benchmarks/baton-jars/heritrix-1.14.4/lib/", 
    'jasperreports': "benchmarks/baton-jars/jasperreports-3.7.4/lib/"
}

TAMIFLEXLOG = {
    'briss': "benchmarks/baton-jars/briss/briss-refl.log", 
    'columba': "benchmarks/baton-jars/columba/1.4/columba-refl.log", 
    'eclipse': "benchmarks/baton-jars/eclipse/eclipse-refl.log", 
    'gruntspud': "benchmarks/baton-jars/gruntspud/gruntspud-refl.log", 
    'jedit': "benchmarks/baton-jars/jedit/3.0/jedit-default-refl.log", 
    'pmd': "benchmarks/baton-jars/pmd/5.3.2/pmd-refl.log", 
    'soot': "benchmarks/baton-jars/soot/2.3.0/soot-refl.log", 
    'h2': "benchmarks/baton-jars/h2/h2-tamiflex-default.log",
    'galleon': "benchmarks/baton-jars/galleon-2.3.0/galleon-refl.log", 
    'heritrix': "benchmarks/baton-jars/heritrix-1.14.4/heritrix-refl.log", 
    'jasperreports': "benchmarks/baton-jars/jasperreports-3.7.4/jasperreports-refl.log"
}

def getBatonAppMain(app):
    return MAINCLASSES[app]

def getBatonAppPath(app):
    return APPPATH[app]


def getBatonAppLibPath(app):
    return LIBPATH[app]


def getTamiflexLog(app):
    return TAMIFLEXLOG[app]

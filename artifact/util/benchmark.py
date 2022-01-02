#!/usr/bin/env python3

BENCHMARKS = ['antlr', 'bloat', 'chart', 'eclipse', 'fop', 'luindex', 'lusearch', 'pmd', 'xalan', 'checkstyle', 'JPC',
              'findbugs']

XCORPUS = ['aoi', 'drawswf', 'emma', 'freecol', 'itext', 'jasml', 'javacc', 'jext',
           'jgrapht', 'jgroups', 'jmoney', 'jrat', 'jsXe', 'marauroa', 'megamek', 'pooka',
           'proguard', 'sablecc', 'weka', ]

MAINCLASSES = {
    'antlr': 'dacapo.antlr.Main',
    'bloat': 'dacapo.bloat.Main',
    'chart': 'dacapo.chart.Main',
    'eclipse': 'dacapo.eclipse.Main',
    'fop': 'dacapo.fop.Main',
    'luindex': 'dacapo.luindex.Main',
    'lusearch': 'dacapo.lusearch.Main',
    'pmd': 'dacapo.pmd.Main',
    'xalan': 'dacapo.xalan.Main',
    'checkstyle': 'com.puppycrawl.tools.checkstyle.Main',
    'findbugs': 'edu.umd.cs.findbugs.FindBugs',
    'JPC': 'org.jpc.j2se.JPCApplication',

    'batik': 'org.apache.batik.apps.svgbrowser.Main',
    'sunflow': 'SunflowGUI',
    'soot': 'soot.Main',
    'jedit': 'org.gjt.sp.jedit.jEdit',
    'briss': 'at.laborg.briss.Briss',
    'avrora': 'avrora.Main',
    'h2': 'org.h2.tools.Server',
    'gruntspud': 'gruntspud.CVSRoot',
    # 'columba':'columba',
    'JPF': 'gov.nasa.jpf.JPF',
    'aoi': 'artofillusion.ArtOfIllusion',
    'drawswf': 'DrawSWF',
    'emma': 'emma',
    'freecol': 'net.sf.freecol.FreeCol',
    'itext': 'com.itextpdf.rups.Rups',
    'jasml': 'jasml',
    'javacc': 'javacc',
    'jext': 'org.jext.Jext',
    'jgrapht': 'org.jgrapht.demo.JGraphAdapterDemo',
    'jgroups': 'org.jgroups.Version',
    'jmoney': 'net.sf.jmoney.Start',
    'jrat': 'org.shiftone.jrat.cli.Cli',
    'jsXe': 'net.sourceforge.jsxe.jsXe',
    'marauroa': 'marauroa.server.marauroad',
    'megamek': 'megamek.MegaMek',
    'pooka': 'net.suberic.pooka.Pooka',
    'proguard': 'proguard.ProGuard',
    'sablecc': 'org.sablecc.sablecc.SableCC',
    'weka': 'weka.gui.GUIChooser',
}

APPPATH = {
    'antlr': 'benchmarks/dacapo/antlr.jar',
    'bloat': 'benchmarks/dacapo/bloat.jar',
    'chart': 'benchmarks/dacapo/chart.jar',
    'eclipse': 'benchmarks/dacapo/eclipse.jar',
    'fop': 'benchmarks/dacapo/fop.jar',
    'luindex': 'benchmarks/dacapo/luindex.jar',
    'lusearch': 'benchmarks/dacapo/lusearch.jar',
    'pmd': 'benchmarks/dacapo/pmd.jar',
    'xalan': 'benchmarks/dacapo/xalan.jar',
    'checkstyle': 'benchmarks/applications/checkstyle/checkstyle-5.7-all.jar',
    'findbugs': 'benchmarks/applications/findbugs/findbugs.jar',
    'JPC': 'benchmarks/applications/JPC/JPCApplication.jar',
}

APPJARNAMES = {
    'batik': '1.6.1/batik-squiggle',
    'checkstyle': 'checkstyle-5.7-all',
    'findbugs': 'findbugs',
    'JPC': 'JPCApplication',
    'sunflow': 'sunflow',
    'soot': 'sootclasses-2.3.0',
    'jedit': 'jedit',
    'briss': 'briss-0.9',
    'avrora': 'avrora',
    'h2': 'h2',
    'gruntspud': 'GruntspudSA',
    # 'columba':'columba',
    'JPF': 'javapathfinder-r1258/lib/jpf',
    'aoi': 'aoi-2.8.1',
    'drawswf': 'drawswf-1.2.9',
    'emma': 'emma-2.0.5312',
    'freecol': 'freecol-0.10.7',
    'itext': 'itext-5.0.3',
    'jasml': 'jasml-0.10',
    'javacc': 'javacc-5.0',
    'jext': 'jext-5.0',
    'jgrapht': 'jgrapht-0.8.1',
    'jgroups': 'jgroups-2.10.0',
    'jmoney': 'jmoney-0.4.4',
    'jrat': 'jrat-0.6',
    'jsXe': 'jsXe-04_beta',
    'marauroa': 'marauroa-3.8.1',
    'megamek': 'megamek-0.35.18',
    'pooka': 'pooka-3.0-080505',
    'proguard': 'proguard-4.5.1',
    'sablecc': 'sablecc-3.2',
    'weka': 'weka-3-7-9',
}

LIBPATH = {
    'antlr': 'benchmarks/dacapo/antlr-deps.jar',
    'bloat': 'benchmarks/dacapo/bloat-deps.jar',
    'chart': 'benchmarks/dacapo/chart-deps.jar',
    'eclipse': 'benchmarks/dacapo/eclipse-deps.jar',
    'fop': 'benchmarks/dacapo/fop-deps.jar',
    'luindex': 'benchmarks/dacapo/luindex-deps.jar',
    'lusearch': 'benchmarks/dacapo/lusearch-deps.jar',
    'pmd': 'benchmarks/dacapo/pmd-deps.jar',
    'xalan': 'benchmarks/dacapo/xalan-deps.jar',
    'checkstyle': 'benchmarks/applications/checkstyle/',
    'findbugs': 'benchmarks/applications/findbugs/',
    'JPC': 'benchmarks/applications/JPC/',
}

TAMIFLEXLOG = {
    'antlr': 'benchmarks/dacapo/antlr-refl.log',
    'bloat': 'benchmarks/dacapo/bloat-refl.log',
    'chart': 'benchmarks/dacapo/chart-refl.log',
    'eclipse': 'benchmarks/dacapo/eclipse-refl.log',
    'fop': 'benchmarks/dacapo/fop-refl.log',
    'luindex': 'benchmarks/dacapo/luindex-refl.log',
    'lusearch': 'benchmarks/dacapo/lusearch-refl.log',
    'pmd': 'benchmarks/dacapo/pmd-refl.log',
    'xalan': 'benchmarks/dacapo/xalan-refl.log',
    'checkstyle': 'benchmarks/applications/checkstyle/checkstyle-refl.log',
    'findbugs': 'benchmarks/applications/findbugs/findbugs-refl.log',
    'JPC': 'benchmarks/applications/JPC/JPC-refl.log',
}

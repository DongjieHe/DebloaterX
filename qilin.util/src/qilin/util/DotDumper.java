package qilin.util;

import qilin.util.graph.DirectedGraph;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;

public class DotDumper<N> extends AbstractDotDumper<N> {
    private final String fileName;

    public DotDumper(DirectedGraph<N> graph) {
        this(graph, "a.dot");
    }

    public DotDumper(DirectedGraph<N> graph, String fileName) {
        super(graph);
        this.fileName = fileName;
    }

    @Override
    public void dumpToDot() {
        StringBuilder builder = new StringBuilder();
        drawADotGraph(graph.allNodes(), builder);
        try {
            FileOutputStream fos = new FileOutputStream(fileName);
            PrintStream ps = new PrintStream(fos);
            ps.println(builder);
            ps.close();
            fos.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

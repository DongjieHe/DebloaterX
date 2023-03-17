package qilin.util;

import qilin.util.graph.DirectedGraph;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public abstract class AbstractDotDumper<N> {
    protected final DirectedGraph<N> graph;

    protected AbstractDotDumper(DirectedGraph<N> graph) {
        this.graph = graph;
    }

    private int index = 0;
    protected final Map<N, Integer> node2Id = new HashMap<>();

    protected int getNodeID(N node) {
        if (node2Id.containsKey(node)) {
            return node2Id.get(node);
        } else {
            node2Id.put(node, index++);
            return node2Id.get(node);
        }
    }

    protected String addEdgeString(N x, N y) {
        return "\t" + getNodeID(x) + " -> " + getNodeID(y) + ";\n";
    }

    public abstract void dumpToDot();

    protected void drawADotGraph(Collection<N> nodes, StringBuilder dumpString) {
        dumpString.append("digraph G {\n");
        for (N x : nodes) {
            graph.succsOf(x).forEach(y -> {
                dumpString.append(addEdgeString(x, y));
            });
        }
        dumpString.append("}");
    }
}

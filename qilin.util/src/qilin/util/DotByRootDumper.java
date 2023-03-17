package qilin.util;

import qilin.util.graph.DirectedGraph;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.util.*;

public class DotByRootDumper<N> extends AbstractDotDumper<N> {

    public DotByRootDumper(DirectedGraph<N> graph) {
        super(graph);
    }

    public Set<N> computeReachableNodes(N source) {
        Set<N> reachableNodes = new HashSet<>();
        Stack<N> stack = new Stack<>();
        stack.push(source);
        while (!stack.isEmpty()) {
            N node = stack.pop();
            if (reachableNodes.add(node)) {
                stack.addAll(graph.succsOf(node));
            }
        }
        return reachableNodes;
    }

    private Vector<String> constructDotString() {
        Collection<N> roots = graph.computeRootNodes();
        Collection<N> tails = graph.computeTailNodes();
        Vector<String> vector = new Vector<>();
        roots.stream().filter(x -> !tails.contains(x)).forEach(root -> {
            Set<N> reachs = computeReachableNodes(root);
            StringBuilder dumpString = new StringBuilder();
            drawADotGraph(reachs, dumpString);
            vector.add(dumpString.toString());
        });
        node2Id.forEach((k, v) -> {
            System.out.println("\tID " + String.format("%04d", v) + ":" + k.toString());
        });
        return vector;
    }

    public void dumpToDot() {
        Vector<String> vec = constructDotString();
        for (int idx = 0; idx < vec.size(); ++idx) {
            String fileName = "a" + idx + ".dot";
            try {
                FileOutputStream fos = new FileOutputStream(fileName);
                PrintStream ps = new PrintStream(fos);
                ps.println(vec.get(idx));
                ps.close();
                fos.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}

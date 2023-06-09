import java.util.*;

class Node {
    char character;
    int frequency;
    Node left;
    Node right;

    public Node(char character, int frequency) {
        this.character = character;
        this.frequency = frequency;
    }

    public boolean isLeaf() {
        return left == null && right == null;
    }
}


public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Provide text to code: ");
        String text = scanner.nextLine();

        Map<Character, Integer> frequencyCounterMap = new HashMap<>();
        for (char c : text.toCharArray()) {
            if (Character.isLetter(c)) {
                frequencyCounterMap.put(c, frequencyCounterMap.getOrDefault(c, 0) + 1);
            }
        }

        List<Node> nodes = new ArrayList<>();
        for (Map.Entry<Character, Integer> entry : frequencyCounterMap.entrySet()) {
            nodes.add(new Node(entry.getKey(), entry.getValue()));
        }

        while (nodes.size() > 1) {
            Collections.sort(nodes, Comparator.comparingInt(node -> node.frequency));

            Node left = nodes.remove(0);
            Node right = nodes.remove(0);

            Node parent = new Node('\0', left.frequency + right.frequency);
            parent.left = left;
            parent.right = right;

            nodes.add(parent);
        }

        Node root = nodes.get(0);
        Map<Character, String> huffmanCode = new HashMap<>();
        generateCodes(root, "", huffmanCode);

        System.out.println("Char  |  Code");
        System.out.println("-------------");
        for (Map.Entry<Character, String> entry : huffmanCode.entrySet()) {
            System.out.println(entry.getKey() + "   |   " + entry.getValue());
        }
    }

    public static void generateCodes(Node node, String code, Map<Character, String> huffmanCode) {
        if (node.isLeaf()) {
            huffmanCode.put(node.character, code);
            return;
        }

        generateCodes(node.left, code + "0", huffmanCode);
        generateCodes(node.right, code + "1", huffmanCode);
    }
}


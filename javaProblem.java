import java.util.*;

public class javaProblem {
    public static String smallestSubsequence(String s) {
        Stack<Character> stack = new Stack<Character>();
        Set<Character> visited = new HashSet<Character>();
        Map<Character, Integer> lastOccurence = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); i++) {
            lastOccurence.put(s.charAt(i), i);
        }
        for (int i = 0; i < s.length(); i++) {
            if (!visited.contains(s.charAt(i))) {
                while (!stack.isEmpty() && stack.lastElement() > s.charAt(i) && lastOccurence.get(s.charAt(i)) > i) {
                    visited.remove(stack.pop());
                }
                System.out.println(stack.toString());
                System.out.println(stack.toString());
                stack.add(s.charAt(i));
                visited.add(s.charAt(i));
            }
        }
        System.out.println(stack.toString());
        String res ="";
        while (!stack.isEmpty()) {
            res += stack.pop();
        }
        return res;
    }
    public static void main(String[] args) {
        System.out.println(smallestSubsequence("bcabc"));
    }
}
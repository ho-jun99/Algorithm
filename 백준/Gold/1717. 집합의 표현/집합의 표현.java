

import java.util.Scanner;

public class Main {
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] parent = new int[n+1];
        for (int i=0; i<parent.length; i++) {
            parent[i] = i;
        }

        for (int i=0; i<m; i++) {
            int operation = sc.nextInt();
            int first = sc.nextInt();
            int second = sc.nextInt();

            if (operation == 0) { // union?
                union(parent,first,second);
            } else { // isSameSet?
                if ( isSameSet(parent,first,second)) System.out.println("YES");
                else System.out.println("NO");
            }
        }
    }

    public static void union(int[] parent, int first, int second) {
        first = find(parent,first);
        second = find(parent,second);

        if (first <= second) {
            parent[second] = first;
        }else{
            parent[first] = second;
        }
    }

    public static int find(int[] parent,int node) {
        if (parent[node] == node) return node;
        return parent[node] = find(parent,parent[node]);
    }

    public static boolean isSameSet(int[] parent, int first, int second) {
        if (find(parent,first) == find(parent,second)) return true;
        else return false;
    }
}

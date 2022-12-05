

import java.util.Scanner;

// [백준1922] 네트워크 연결을 이용한 Prim풀이 공부
public class Main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int n = sc.nextInt(); // 컴퓨터의 수
        int m = sc.nextInt(); // 연결할 수 있는 선의 수
        int[][] network = new int[n+1][n+1];
        for (int i=0; i<n+1; i++) {
            for (int j=0; j<n+1; j++) {
                network[i][j] = Integer.MAX_VALUE;
            }
        }

        int a,b,weight;
        for (int i=0; i<m; i++) {
            a = sc.nextInt();
            b = sc.nextInt();
            weight = sc.nextInt();
            network[a][b] = weight;
            network[b][a] = weight;
        }

        sovleWithPrim(n,m,network);

    }

    public static void sovleWithPrim(int n, int m, int[][] network) {
        int[] nearest = new int[n+1];
        int[] distance = new int[n+1];
        int result = 0;
        // init nearest, distance
        for (int i=2; i<=n; i++) {
            nearest[i] = 1;
            distance[i] = network[1][i];
        }

        // 모든 간선이 연결될때까지 (n-1)번 반복
        for (int cnt=0; cnt<n-1; cnt++) {
            int min = Integer.MAX_VALUE;
            int vnear = 0;

            // 가장 작은 weight를 찾아줌 ( 1은 이미 연결 돼 있기 때문에 2부터 )
            for (int i=2; i<=n; i++) {
                if (1 <= distance[i] && distance[i] < min) {
                    min = distance[i];
                    vnear = i;
                }
            }
            // 여기로 오면 가장 작은 distance가 선택 됨.
            result += distance[vnear];
            distance[vnear] = -1; // 선택 됐음을 표
//            System.out.println(vnear);

            for(int i=2; i<=n; i++) {
                if(network[vnear][i] < distance[i]) { // vnear가 연결된 것 때문에 업데이트가 가능한게 있으면 업데이트
                    distance[i] = network[vnear][i];
                    nearest[i] = vnear;
                }
            }
        }

        System.out.println(result);
    }
}

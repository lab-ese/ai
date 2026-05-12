import java.util.Scanner;

public class magicsquare{

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter odd N: ");
        int n = sc.nextInt();

        if (n % 2 == 0) {
            System.out.println("Only odd order allowed");
            return;
        }

        int[][] square = new int[n][n];

        int i = 0;
        int j = n / 2;

        for (int num = 1; num <= n * n; num++) {
            square[i][j] = num;

            int ni = (i - 1 + n) % n;
            int nj = (j + 1) % n;

            if (square[ni][nj] != 0) {
                i = (i + 1) % n;
            } else {
                i = ni;
                j = nj;
            }
        }

        // Print magic square
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                System.out.print(square[r][c] + " ");
            }
            System.out.println();
        }

        int magicConstant = n * (n * n + 1) / 2;
        System.out.println("\nMagic Constant = " + magicConstant);
    }
}
import java.util.*;

public class TicTacToeNonAI {

    static int[][] MAGIC = {
        {8, 1, 6},
        {3, 5, 7},
        {4, 9, 2}
    };

    static char[][] board = {
        {'X', ' ', 'X'},
        {' ', 'O', ' '},
        {'O', 'X', 'O'}
    };

    static void printBoard() {
        for (int i = 0; i < 3; i++) {
            System.out.println(board[i][0] + " | " + board[i][1] + " | " + board[i][2]);
            System.out.println("---------");
        }
    }

    static int[] getPos(int value) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (MAGIC[i][j] == value) {
                    return new int[]{i, j};
                }
            }
        }
        return null;
    }

    static boolean vacant(int value) {
        int[] pos = getPos(value);
        return board[pos[0]][pos[1]] == ' ';
    }

    static List<Integer> getPlayerValues(char player) {
        List<Integer> vals = new ArrayList<>();

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == player) {
                    vals.add(MAGIC[i][j]);
                }
            }
        }
        return vals;
    }

    static char detectTurn() {
        int xCount = 0, oCount = 0;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == 'X') xCount++;
                if (board[i][j] == 'O') oCount++;
            }
        }

        return (xCount == oCount) ? 'X' : 'O';
    }

    static boolean magicMove(char player) {
        List<Integer> values = getPlayerValues(player);

        for (int i = 0; i < values.size(); i++) {
            for (int j = i + 1; j < values.size(); j++) {

                int sum = values.get(i) + values.get(j);
                int target = 15 - sum;

                if (target >= 1 && target <= 9 && sum <= 15 && vacant(target)) {
                    int[] pos = getPos(target);
                    board[pos[0]][pos[1]] = player;
                    return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {

        System.out.println("Initial Board:");
        printBoard();

        char turn = detectTurn();
        System.out.println("\nTurn detected: " + turn);

        boolean played = magicMove(turn);

        if (played) {
            System.out.println("\nBoard after " + turn + "'s move:");
            printBoard();
        } else {
            System.out.println("No valid magic move for " + turn);
        }
    }
}
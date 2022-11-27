import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class solution {
    public static boolean canMakeWord(char[][] board, String word) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == word.charAt(0)) {
                    if (helper(0, i, j, board, word)) {
                        return true;
                    }
                }
            }
        }

        return false;
    }

    private static boolean helper(int index, int i, int j, char[][] board, String word) {
        if (i < 0 || j < 0 || i >= board.length || j >= board[i].length) { // out of bounds
            return false;
        } else if (board[i][j] != word.charAt(index)) { // wrong letter or already visited
            return false;
        } else if (index == word.length() - 1) { // found word
            return true;
        }

        char c = board[i][j];
        board[i][j] = 0;

        if (helper(index + 1, i - 1, j, board, word) // up
                || helper(index + 1, i + 1, j, board, word) // down
                || helper(index + 1, i, j - 1, board, word) // left
                || helper(index + 1, i, j + 1, board, word)) { // right
            return true;
        }

        board[i][j] = c; // backtrack

        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ArrayList<char[]> al = new ArrayList<char[]>();
        String rawInput;
        String word;

        while (true) {
            rawInput = br.readLine();
            if (rawInput.split(" ").length != 1) {
                al.add(rawInput.replace(" ", "").toCharArray());
            } else {
                word = rawInput;
                break;
            }
        }

        char[][] arr = new char[al.size()][];
        arr = al.toArray(arr); // making into 2d array so its easier to work with

        System.out.println(canMakeWord(arr, word));
    }
}

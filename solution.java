public class solution {
    public static void main(String[] args) {
        char[][] board = {
                {'A', 'B', 'C', 'E'},
                {'S', 'F', 'C', 'S'},
                {'A', 'D', 'E', 'E'}};
        System.out.println("ABCCED: "+canConnect(board, "ABCCED"));
        System.out.println("SEE: "+canConnect(board, "SEE"));
        System.out.println("ABCB: "+canConnect(board, "ABCB"));
    }

    public static boolean canConnect(char[][] board, String word) {
        int l = word.length();

        if (l == 0) return true;

        if (l > board.length * (board.length < 1 ? 0 : board[0].length))
            return false;

        int firstCount = 0, lastCount = 0;
        char firstChar = word.charAt(0), lastChar = word.charAt(l-1), boardChar;
        char[] chars = word.toCharArray();

        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) {
                boardChar = board[r][c];

                for (int i = 0; i < chars.length; i++) {
                    if (chars[i] == boardChar) {
                        chars[i] = 0;
                        break;
                    }
                }

                if (boardChar == firstChar)
                    firstCount++;
                else if (boardChar == lastChar)
                    lastCount++;
            }
        }

        for (char c : chars)
            if (c != 0)
                return false;

        if (lastCount < firstCount)
            word = new StringBuilder(word).reverse().toString();

        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) {

                if (board[r][c] == word.charAt(0)) {
                    char temp = board[r][c];
                    board[r][c] = 0;

                    if (canConnect(board, word.substring(1), r, c)) {
                        board[r][c] = temp;
                        return true;
                    }

                    board[r][c] = temp;
                }
            }
        }
        return false;
    }

    public static boolean canConnect(char[][] board, String word, int r, int c) {
        if (word.length() == 0) return true;

        for (int a=-2; a<=2; a++){
            if(a==0) continue;
            int i=a/2, j = a%2;

            if(r+i>=0 && r+i<board.length && c+j>=0 && c+j<board[0].length) {
                if (board[r+i][c+j] == word.charAt(0)) {
                    char temp = board[r+i][c+j];
                    board[r+i][c+j] = 0;

                    if (canConnect(board, word.substring(1), r+i, c+j)) {
                        board[r+i][c+j] = temp;
                        return true;
                    }

                    board[r+i][c+j] = temp;
                }
            }
        }
        return false;
    }
}
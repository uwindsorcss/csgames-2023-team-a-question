import java.util.List;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Scanner;

public class solution {

    public static List<Integer> search(char board[][], int x, int y, char current){
        var list = new LinkedList<Integer>();

        if(x+1 <= board.length-1 && board[x+1][y] == current){
            list.add(x+1);
            list.add(y);
            board[x+1][y] = '1';
        }
        else if(x-1 > 0 && board[x-1][y] == current){
            list.add(x-1);
            list.add(y);
            board[x-1][y] = '1';
        }
        else if(y+1 <= board[x].length-1 && board[x][y+1] == current){
            list.add(x);
            list.add(y+1);
            board[x][y+1] = '1';
        }
        else if(y-1 > 0 && board[x][y-1] == current){
            list.add(x);
            list.add(y-1);
            board[x][y-1] = '1';
        }

        return list;
    }

    public static char[][] copyArray(char[][] arr){
        char[][] copy = new char[arr.length][];
        for(int i=0; i<arr.length; i++){
            copy[i] = new char[arr[i].length];
            for(int j= 0; j<arr[i].length; j++){
                copy[i][j] = arr[i][j];
            }
        }

        return copy;
    }

    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);
        System.out.println("# of rows: ");
        int rows = scan.nextInt();
        System.out.println("# of columns: ");
        int cols = scan.nextInt();

        System.out.println("Enter your board:");
        char board[][] = new char[rows][cols];

        for (int i = 0; i < rows; i++) {
            String data = "";
            if (scan.hasNext()) { // input from user
                data = scan.next();
            } else {
                break;
            }
            for (int j = 0; j < cols; j++)
                board[i][j] = data.charAt(j);
        }

        Scanner myObj = new Scanner(System.in);
        System.out.println("Enter string: ");
        String word = myObj.nextLine();

        boolean ans = false;

        Queue<Character> q = new LinkedList<>();
        for (int i = 0; i < word.length(); i++) {
            q.add(word.charAt(i));
        }

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                Queue<Character> qCopy = new LinkedList<>(q);
                if(board[i][j] == qCopy.poll()) {
                    var copy = copyArray(board);
                    var list = search(copy, i, j, qCopy.poll());
                    if(list.isEmpty()){
                        break;
                    }
                    int x = list.get(0);
                    int y = list.get(1);

                    while(qCopy.peek() != null){
                        list = search(copy, x, y, qCopy.poll());
                        if(list.isEmpty()){
                            break;
                        }

                        if(qCopy.peek() == null){
                            ans = true;
                        }

                        if(!list.isEmpty()){
                            x = list.get(0);
                            y = list.get(1);
                        }

                    }
                    if(ans == true){
                        break;
                    }
                }
            }
        }

        System.out.println(ans);

    }
}

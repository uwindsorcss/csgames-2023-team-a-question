import java.util.Arrays;
public class Board {
    public char[][] a;//2d array of char inputs
    public int path[];//the collection of the points selected by the algorithm to spell the word
    public int explored = 0;//current stage of exploration at a given a[i][j]
    private int len;//length of word we must find in a[][]

    public Board(char a[][], int len){//board constructor
        this.a = a;
        path = new int[len];
        Arrays.fill(path, -1);//initialize all values of path to -1 to avoid confusion with a[0][0]
        this.len = len;
    }

    /**the search function will take indexes for a row and column of the array a and search for the first c it finds. Later on, we may use the first two
     * parameters to avoid double counting a character. Search returns a unique index for each element in a[][], it is calculated as 4*i + j. If a character is
     *not found it returns -1
     */
    public int search(int row, int col, char c){
        for(int i = row; i < 3; i++){
            for(int j = col; j < 4; j++){
                if(a[i][j] == c){
                    return 4*i + j;
                }
            }
        }
        return -1;
    }

    /**The available function takes a pathNum and then iterates through path[] to locate it, if it does, it returns false; otherwise, it will return
     * true
     */
    public boolean available(int pathNum){
        for(int i = 0; i < len; i++){
            if(path[i] == pathNum){
                return false;
            }
        }
        return true;
    }

    public int getRow(int pathNum){return (pathNum - pathNum%4)/4;}//returns i by deriving it from a pathNum

    public int getCol(int pathNum){return pathNum - (pathNum - pathNum%4);}//returns j by deriving it from a pathNum
}
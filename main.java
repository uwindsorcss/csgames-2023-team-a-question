import java.util.Scanner;

public class main {
    static boolean solution(String word, char[][] a){
        Board b = new Board(a, word.length());//create board object
        char c = word.charAt(0);//get first char in word
        int col = 0;//col & row are 0 so that b.search looks for c from the start of a[][] to the end
        int row = 0;
        b.path[0] = b.search(row, col, c);//assign the pathNum to path[0]
        boolean terminate = false;//if this becomes true, we are unable to locate a valid char in a[][] that would continue the word. Therefore, the function returns false
        int i = 1;//index i represents the index of the current letter in the word we are attempting to locate
        do{
            if(b.path[i - 1] >= 0){//if the previous path index is less than zero, we must skip to the next else-statement
                c = word.charAt(i);
                row = b.getRow(b.path[i - 1]);
                col = b.getCol(b.path[i - 1]);
            }
            else{//set explored = -1
                b.explored = -1;
            }
            switch (b.explored){
                case -1:
                    terminate = true;
                    break;
                case 0://if there is a character above the character path[i - 1], and it equals c, and it is not present anywhere else in the path
                    if(row > 0 && b.a[row - 1][col] == c && b.available(b.search(row - 1, col, c))){
                        b.path[i] = b.search(row - 1, col, c);
                        b.explored = -1;
                        i++;
                    }
                    b.explored++;
                    break;
                case 1://if there is a character to the right of the character path[i - 1], and it equals c, and it is not present anywhere else in the path
                    if(col < 3 && b.a[row][col + 1] == c && b.available(b.search(row, col + 1, c))){
                        b.path[i] = b.search(row, col + 1, c);
                        b.explored = -1;
                        i++;
                    }
                    b.explored++;
                    break;
                case 2://if there is a character below the character path[i - 1], and it equals c, and it is not present anywhere else in the path
                    if(row < 2 && b.a[row + 1][col] == c && b.available(b.search(row + 1, col, c))){
                        b.path[i] = b.search(row + 1, col, c);
                        b.explored = -1;
                        i++;
                    }
                    b.explored++;
                    break;
                case 3://if there is a character to the left of the character path[i - 1], and it equals c, and it is not present anywhere else in the path
                    if(col > 0 && b.a[row][col - 1] == c && b.available(b.search(row, col - 1, c))){
                        b.path[i] = b.search(row, col - 1, c);
                        b.explored = -1;
                        i++;
                    }
                    b.explored++;
                    break;
                default://if all cardinal directions of path[i-1] have been checked, and we still haven't found c
                    if(i == 1){//if path only contains the identifier of the first char in word
                        c = word.charAt(0);
                        row = b.getRow(b.path[0]);
                        col = b.getCol(b.path[0]) + 1;
                        int temp = b.search(row, col, c);//attempt to look for another candidate for path[0]
                        if(temp == -1){//if a candidate is not found
                            terminate = true;
                        }
                        else{//otherwise
                           b.path[0] = temp;
                           b.explored = 0;
                        }
                    }
                    if(i > 1){//if there are more than 1 chars in path[], check the previous two pathNums to determine which direction was taken from path[i - 2] to reach path[i - 1]
                        if(b.path[i - 2] == b.path[i - 1] + 4*b.getRow(b.path[i - 1])){//if the algorithm went up
                            b.explored = 1;
                        }
                        else if(b.path[i - 2] == b.path[i - 1] - 1){//if it went right
                            b.explored = 2;
                        }
                        else if(b.path[i - 2] == b.path[i - 1] - 4*b.getRow(b.path[i - 1])){//if it went down
                            b.explored = 3;
                        }
                        else{//else, it went left
                            b.explored = 4;
                            if(i == 2){
                                b.explored = -1;
                            }
                        }
                        i--;
                    }
                    break;
            }
        }while(i < word.length() && terminate == false);//while the loop has no found a pathNum for all indexes in path[] AND while terminate is false
        if(terminate == true){//path not found
            return false;
        }
        else{//word can be made
            return true;
        }
    }

    public static void main(String args[]){
        //initialize Scanner and 2D array
        Scanner in = new Scanner(System.in);
        char[][] array = new char[3][4];

        //Read three lines of input from console, erase the spaces from the string and convert each string into a char array. This array is then assigned to array[i]
        for(int i = 0; i < 3; i++){
            array[i] = in.nextLine().replaceAll(" ","").toCharArray();
        }

        //take the word input and pass it along with the array into the parameters of solution()
        System.out.println("What word would you like to find? Enter it unbroken below: ");
        String word = in.nextLine();
        System.out.println(solution(word, array));
    }
}
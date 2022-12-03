#include <stdio.h>

int used_positions[100][2] = {0};
int used_position_count = 0;

//Is a grid coordinate already used
int alreadyUsed(int row, int col) {
    for(int i = 0; i < used_position_count; i++) {
        if(used_positions[i][0] == row && used_positions[i][1] == col) {
            return 1;
        }
    }
    return 0;
}

//Search for the word
int search(char grid[100][100], int row_count, int col_count, char word[100], int let_count) {
    int row;
    int col;
    for(int r = 0; r < row_count; r++) {
        for(int c = 0; c < col_count; c++) {
            if(grid[r][c] == word[0]) {
                row = r;
                col = c;
                used_positions[used_position_count][0] = row;
                used_positions[used_position_count][1] = col;
                used_position_count++;
                
                for(int let = 1; let <= let_count; let++) {
                    if(row != row_count-1 && (alreadyUsed(row+1, col)) == 0 && grid[row+1][col] == word[let]) row++;
                    else if(row != 0 && (alreadyUsed(row-1, col)) == 0 && grid[row-1][col] == word[let]) row--;
                    else if(col != col_count-1 && (alreadyUsed(row, col+1)) == 0  && grid[row][col+1] == word[let]) col++;
                    else if(col != 0 && (alreadyUsed(row, col-1)) == 0  && grid[row][col-1] == word[let]) col--;
                    else {used_position_count = 0; break;}

                    if(let == let_count) return 1;

                    used_positions[used_position_count][0] = row;
                    used_positions[used_position_count][1] = col;
                    used_position_count++; 
                    
                }
            }
        }
    }
    
    return 0;
}

//Get the word from the user
int find_the_word() {
    
    int num;
    char grid[100][100];
    char word[100];
    int col = 0;
    int col_count = 0;
    int row = 0;
    int row_count = 0;
    int letter_scanned = 0;
    int let_count = 0;
    char c;
    
    //Get my integer array
    while((c = getchar())) {
        if(c == ' ') {
            col++;
            letter_scanned = 0;
        } else if(c == '\n'){
            row++;
            col_count = col+1;
            col = 0;
            letter_scanned = 0;
        } else if(!letter_scanned){
            grid[row][col] = c;
            letter_scanned = 1;
        } else {
            word[0] = grid[row][col];
            word[1] = c;
            let_count+=2;
            break;
        }
    }
    
    row_count = row;

    while((c = getchar()) != '\n') {
        word[let_count] = c;
        let_count++;
    }
    let_count--;
    
    return search(grid, row_count, col_count, word, let_count);;
}

//Main function
int main(void) {
    if(find_the_word())
        puts("True");
    else
        puts("False");

    return 0;
}
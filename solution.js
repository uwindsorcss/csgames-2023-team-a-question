// CSS GAMES QUESTION A
// CREATED BY KEAGAN WHISTON

let board = [
    ["a","b","c"],
    ["d","e","f"],
    ["g","h","x"]
    ];
let rows = board.length;
let cols = board[0].length;

let x=[-1, 0, 0, 1];
let y=[0, -1, 1, 0];

function word_search(board, word){
    for(let i = 0; i < rows; i++){
        for(let j = 0; j < cols; j++){
            console.log('Checking board at position ' + i + ', ' + j);
            if(search(board, word, i, j)){
                console.log(word + " was found in the board")
                return;
            } 
        }
    }
    console.log('Search term "' + word + '" was not found')
}

function search(board, word, currentLetterRow, currentLetterCol){
    // check if the first letter even exists in the board
    if(board[currentLetterRow][currentLetterCol] != word[0]){
        console.log(board[currentLetterRow][currentLetterCol] + ' does not equal ' + word[0]);
        return false;
    }
    
    console.log('First letter found! Checking local space.');

    // Initialize to 1 since we have the first letter at this point
    let foundLettersCount = 1;
    
    let len = word.length;
    let rd;
    let cd;
    
    // Iterate through every letter in our word
    for(let k = 1; k < len; k++){
        
        // Check all four cardinal directions per letter
        for(let dir = 0; dir < 4; dir++){
            
            // Reference our current position
            rd = currentLetterRow + x[dir];
            cd = currentLetterCol + y[dir];
            
            // If we are out of bounds then skip to the next direction
            if (rd >= rows || rd < 0 || cd >= cols || cd < 0){
                continue;
            }
  
            // If incorrect letter found here then skip to the next direction
            if (board[rd][cd] != word[k]){
                continue;
            }
            
            // If we make it here then the letter is found
            // Update our reference with our new current position
            currentLetterRow = rd;
            currentLetterCol = cd;
            
            // Increment our counter for found letters
            foundLettersCount++;
        }
        
        // Check if we found all letters
        if (foundLettersCount === len)
            return true;
    }
    return false;
}

word_search(board, "abcf");
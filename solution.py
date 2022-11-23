
# For team A
# board: 2d array of board
# word: a string 
def doesWorkExist(board, word):
    visted = set() # Indicates which spots have been visted while a word is searched for

    # Runs dfs to see if the word is on the grid
    def travelPath(ind, r, c):
        visted.add((r, c))
        if(ind == len(word)): return True
        test = False # test turns to true if one of the paths leads to a word
        if(r > 0 and board[r-1][c] == word[ind] and (r-1, c) not in visted):
            test = test or travelPath(ind+1, r-1, c)
        if(c > 0 and board[r][c-1] == word[ind] and (r, c-1) not in visted):
            test = test or travelPath(ind+1, r, c-1)
        if(c < (len(board[0]) - 1) and board[r][c+1] == word[ind] and (r, c+1) not in visted):
            test = test or travelPath(ind+1, r, c+1)
        if(r < (len(board)-1) and board[r+1][c] == word[ind] and (r+1, c) not in visted):
            test = test or travelPath(ind+1, r+1, c)
        
        visted.remove((r,c))
        return test
            
    for r in range(0, len(board)):
        for c in range(0, len(board[0])):
            if(board[r][c] == word[0]):
                # First letter is found -> see if other letters are on grid
                if(travelPath(1, r, c)): return True
    
    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

if(doesWorkExist(board, word)):
    print("Test 1 successful!")

word = "SEE"
if(doesWorkExist(board, word)):
    print("Test 2 successful!")

word = "ABCB"
if(not doesWorkExist(board, word)):
    print("Test 3 successful!")
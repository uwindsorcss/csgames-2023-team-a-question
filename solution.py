def exist(board, word):
    rows = len(board)
    columns = len(board[0])
    history = []
    word_freq = {}
    board_freq = {}
    
    for letter in word:
        if letter not in word_freq:
            word_freq[letter] = 0
        word_freq[letter] += 1
    
    for row in board:
        for letter in row:
            if letter not in board_freq:
                board_freq[letter] = 0
            board_freq[letter] += 1
    
    for char, count in word_freq.items(): 
        try:
            if count > board_freq[char]:
                return False 
        except KeyError:
            return False
    
    if board_freq[word[0]] > board_freq[word[-1]]:
        word = word[::-1]
    
    def search(row, column, current_char):
        if current_char == len(word):
            return True
        
        if (row < 0
        or column < 0 
        or row >= rows 
        or column >= columns 
        or word[current_char] != board[row][column] 
        or (row, column) in history):
            return False
        
        history.append((row, column))
        print(history)
        result = (search(row + 1, column, current_char + 1) 
        or search(row, column + 1, current_char + 1) 
        or search(row - 1, column, current_char + 1) 
        or search(row, column - 1, current_char + 1))
        history.pop()
        return result
    
    for row in range(rows):
        for column in range(columns):
            if search(row, column, 0):
                return True
    return False

def input_parser(string):
    board = []
    string = string.strip()
    temp_list = string.split("\n")
    word = temp_list.pop()
    for row in temp_list:
        board.append(row.split(" "))
    return (board, word)

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))

print(exist(*input_parser("""
A B C E
S F C S
A D E E
ABCCED
""")))

print(exist(*input_parser("""
A B C E
S F C S
A D E E
SEE
""")))

print(exist(*input_parser("""
A B C E
S F C S
A D E E
ABCB
""")))
import sys

class SearchWord:
    def __init__(self):
        self.moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def isWordInBoard(self, board, word):
        self.board = board
        self.word = word

        self.rows = len(board)
        self.cols = len(board[0])

        print(board)

        for i in range(self.rows):
            for j in range(self.cols):
                found = self.dfs(word, i, j)
                if found:
                    return True

        return False

    def dfs(self, word, i, j):
        if len(word) < 1:
            return True

        if i < 0 or i >= self.rows or j < 0 or j >= self.cols:
            return False

        if word[0] != self.board[i][j]:
            return False
        
        letter = self.board[i][j]
        self.board[i][j] = 0

        for (x, y) in self.moves:
            found = self.dfs(word[1:], i+x, j+y)

            if found:
                #Once found, immediately stops the search on other branches
                return True

        self.board[i][j] = letter

        return False

board = []

previous_line = ""
current_line = input()

#Get Input
while True:
    previous_line = current_line
    current_line = input()

    if not current_line:
        word = previous_line
        break

    board.append(previous_line.split(" "))


searchWord = SearchWord()
print(searchWord.isWordInBoard(board, word))
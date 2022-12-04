from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    # get all lengths of input
    rows, cols, word_len = len(board), len(board[0]), len(word)

    # convert board to a string
    board_str = ''.join([''.join(row) for row in board])

    # check if there are enough occurences of each character in the word in the board
    for char in word:
        if word.count(char) > board_str.count(char):
            return False

    # check if the last char appears less times then the first char, reverse the string if so
    if board_str.count(word[0]) < board_str.count(word[-1]):
        word = word[::-1]

    # create a visited set
    seen = set()

    # row and col are the current position of the board, n is the current position of the word
    def check(row, col, n=0):
        # check if the word exists
        if n == word_len:
            return True

        # check if the row and col are in range
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False

        # check if the current position is visited
        if (row, col) in seen:
            return False

        # backtrack if the current position of the board is not equal to the current position of the word
        if board[row][col] != word[n]:
            return False

        # mark the letter as visited
        seen.add((row, col))

        # check if the word is found in any direction            
        found = check(row + 1, col, n + 1) or \
            check(row - 1, col, n + 1) or \
            check(row, col + 1, n + 1) or \
            check(row, col - 1, n + 1)

        # mark the letter as unvisited
        seen.remove((row, col))

        # return the result
        return found

    # check if the word exists in the board
    return any(check(row, col) for row in range(rows) for col in range(cols))

if __name__ == '__main__':
    board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']]
    word = "ABCCED"

    print(exist(board, word))

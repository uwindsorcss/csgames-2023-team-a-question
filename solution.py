from typing import List

def inBoard(board: List[List[str]], givenWord: str) -> bool:
    rows, cols, length = len(board), len(board[0]), len(givenWord)

    board_str = ''.join([''.join(row) for row in board])

    for char in givenWord:
        if givenWord.count(char) > board_str.count(char):
            return False

    if board_str.count(givenWord[0]) < board_str.count(givenWord[-1]):
        givenWord = givenWord[::-1]

    seen = set()

    def check(row, col, i=0):
        if i == length:
            return True

        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False

        if (row, col) in seen:
            return False

        if board[row][col] != givenWord[i]:
            return False

        seen.add((row, col))

        found = check(row + 1, col, i + 1) or \
            check(row - 1, col, i + 1) or \
            check(row, col + 1, i + 1) or \
            check(row, col - 1, i + 1)

        seen.remove((row, col))

        return found

    return any(check(row, col) for row in range(rows) for col in range(cols))

if __name__ == '__main__':
    board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']]
    givenWord = "ABCCED"

    print(inBoard(board, givenWord))

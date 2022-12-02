class Board:

    def __init__(self, board):
        self._board = board
        self._stack = []

    def can_construct_word(self, word):
        pass

    def dfs_construct_word(self, word, r, c):
        pass

def read_input():
    with open('input.txt') as f:
        lines = f.readlines()
        word = lines.pop()
        grid = [line.strip().split(' ') for line in lines]
        return grid, word

if __name__ == '__main__':
    (grid, word) = read_input()
    print(grid)
    print(word)
    board = Board(grid)
    print("Attempting to construct " + word + ": " + board.can_construct_word(word))
import sys

dr = [-1, 0, 1, 0]  # Row change for neighbours UP, RIGHT, DOWN, and LEFT
dc = [0, 1, 0, -1]  # Column change for neighbours UP, RIGHT, DOWN, and LEFT


class Board:

    # board is stored as an instance variable so we don't have to pass it every time, and so we can easily run
    # multiple test words on the same board
    def __init__(self, board, show_trace):
        self._board = board
        self._show_trace = show_trace

    def can_construct_word(self, word):
        # Iterate over each node, and call _dfs_construct_word when the first letter of word is found
        for r in range(len(self._board)):
            for c in range(len(self._board[r])):
                if self._dfs_construct_word(word, r, c, 0):
                    return True
        return False

    def _dfs_construct_word(self, word, r, c, i):
        # Note that if a cell in the board is visited (i.e., set to 0), this if statement will not be entered
        if word[i] == self._board[r][c]:
            if self._show_trace:
                print(f'Found {word[i]} at ({r},{c}). Word thus far: {word[0:i+1]}')

            if i == len(word)-1:
                return True

            # Otherwise, the search continues. Mark this node as visited
            old_char = self._board[r][c]
            self._board[r][c] = 0

            # Perform DFS on the unvisited neighbour nodes
            for neighbour_num in range(4):
                neighbour_row = r+dr[neighbour_num]
                neighbour_col = c+dc[neighbour_num]
                # If one of the neighbours led to the finished word, break out and return true
                if (self._is_unvisited_neighbour(neighbour_row, neighbour_col) and
                        self._dfs_construct_word(word, neighbour_row, neighbour_col, i+1)):
                    return True

            # None of this node's neighbours led to the word. Make this node unvisited again since we are backtracking
            # out of it
            self._board[r][c] = old_char
            if self._show_trace:
                print(f'Backtracking...\t  Word thus far: {word[0:i]}')
        return False

    def _is_unvisited_neighbour(self, r, c):
        return (
            (0 <= r < len(self._board)) and
            (0 <= c < len(self._board[r])) and
            (self._board[r][c] != 0)
        )


def read_input():
    with open('input.txt') as f:
        lines = f.readlines()
        word = lines.pop()
        grid = [line.strip().split(' ') for line in lines]
        return grid, word


if __name__ == '__main__':
    show_trace = len(sys.argv) > 1 and sys.argv[1] == '-t'
    (grid, word) = read_input()
    board = Board(grid, show_trace)
    print(str(board.can_construct_word(word)))

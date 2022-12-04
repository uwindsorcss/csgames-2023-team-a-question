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
        # Reverse the word if it will make the algorithm more efficient
        word = self._get_equivalent_search_word(word)
        if word is None:    # i.e., a letter in the word does not exist anywhere in the grid
            return False
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

    # Compares the prefix and suffix of word and finds out whether reversing the word will make the algorithm more
    # efficient.
    def _get_equivalent_search_word(self, word):
        # Get the frequency of each letter from word in the board
        letter_freq = [0] * len(word)
        for r in range(len(self._board)):
            for c in range(len(self._board[r])):
                for l in range(len(word)):
                    if self._board[r][c] == word[l]:
                        letter_freq[l] += 1
        # If a letter does not show up in the board, return None so the algorithm doesn't search for the word at all
        if 0 in letter_freq:
            if self._show_trace:
                print('A letter from the word does not exist in the board!')
            return None
        # Otherwise, iterate from both ends of the list and compare the two values at each iterator at each step. If the
        # first discrepancy in frequencies is such that the later letter is less frequent, then return the reversed
        # word. Otherwise, return word.
        for i in range(len(letter_freq) // 2):
            if letter_freq[len(letter_freq) - i - 1] == letter_freq[i]:
                continue
            return word if letter_freq[i] < letter_freq[len(letter_freq) - i - 1] else word[::-1]
        return word


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

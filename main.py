import sys


def try_add_unvisited_neighbour(unvisited_neighbours, coords, visited_set):
    if coords not in visited_set:
        unvisited_neighbours.append(coords)


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
                if self._board[r][c] == word[0]:
                    if self._dfs_construct_word(word, r, c, 0, set()):
                        return True
        return False

    def _dfs_construct_word(self, word, r, c, i, visited_set):

        if word[i] == self._board[r][c]:
            if self._show_trace:
                print(f'Found {word[i]} at ({r},{c}). Word thus far: {word[0:i + 1]}')

            if i == len(word) - 1:
                return True

            # Otherwise, the search continues. Mark this node as visited
            visited_set.add((r, c))

            # Perform DFS on the unvisited neighbour nodes
            for (rn, cn) in self._get_unvisited_neighbours(r, c, visited_set):
                # If one of the neighbours led to the finished word, break out and return true
                if self._dfs_construct_word(word, rn, cn, i + 1, visited_set):
                    return True

            # None of this node's neighbours led to the word. Make this node unvisited again since we are backtracking
            # out of it
            visited_set.remove((r, c))
        return False

    def _get_unvisited_neighbours(self, r, c, visited_set):
        unvisited_neighbours = []
        if r > 0:
            try_add_unvisited_neighbour(unvisited_neighbours, (r - 1, c), visited_set)
        if r < len(self._board) - 1:
            try_add_unvisited_neighbour(unvisited_neighbours, (r + 1, c), visited_set)
        if c > 0:
            try_add_unvisited_neighbour(unvisited_neighbours, (r, c - 1), visited_set)
        if c < len(self._board[r]) - 1:
            try_add_unvisited_neighbour(unvisited_neighbours, (r, c + 1), visited_set)
        return unvisited_neighbours


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

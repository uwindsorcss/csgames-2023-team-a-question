
from itertools import product

def search(points: set, s: str, board: dict, path: set = None) -> bool:
    # points is a list of tuples (x, y) for points to try to connect to the first character of s
    # s is the string to connect, check the list of points to see if they can be connected to form s
    # board is the board of characters
    # path is a list of points that have been used to connect to s so far
    # return True if s can be connected, False otherwise
    if path is None:
        path = set()
    if len(s) == 0:
        return True
    for p in points:
        if s[0] == board[p]:
            path.add(p)
            # list of points left, right, up, down from p that are in the board keyset
            adj = set([(p[0] + 1, p[1]), (p[0] - 1, p[1]), (p[0], p[1] + 1),
                      (p[0], p[1] - 1)]).intersection(board.keys()).difference(path)
            if search(adj, s[1:], board, path):
                return True
            path.remove(p)
    return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # convert board to a dictionary of (x, y) -> character
        board = {(x, y): board[x][y] for x, y in product(
            range(len(board)), range(len(board[0])))}

        # if any char in the word is not in the board, return False
        if not set(word).issubset(set(board.values())): 
            return False

        # if there are less occurences of the last character than the first character, reverse the word
        boardstr = ''.join(board.values())
        if boardstr.count(word[0]) > boardstr.count(word[-1]):
            word = word[::-1]

        # you take the input, and see if for each character, you can follow a path from character to character. The same character cannot be used more than once
        return search(
            set(board.keys()),
            word,
            board
        )
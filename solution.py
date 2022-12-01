# /usr/bin/python3

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


def exist(board: list[list[str]], word: str) -> bool:
    # convert board to a dictionary of (x, y) -> character
    board = {(x, y): board[x][y] for x, y in product(
        range(len(board)), range(len(board[0])))}

    # you take the input, and see if for each character, you can follow a path from character to character. The same character cannot be used more than once
    return search(
        set(board.keys()),
        word,
        board
    )


if __name__ == '__main__':

    # assume input comes from stdin
    # board input is single characters, space separated for columns and newlines for rows
    # word is on its own line
    # example input:
    # ```
    # A B C E
    # S F C S
    # A D E E
    # word
    # ```

    board = []
    word = None
    while (True):
        line = input().split(" ")
        if (len(line) == 1):
            word = line[0]
            break
        board.append(line)

    print(board)
    print(word)

    print(exist(board, word))

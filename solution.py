
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

    
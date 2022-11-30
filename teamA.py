def solve(board, word):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0] and findString(board, [], [i, j], word[1:]):
                return True
    return False


def findString(board, visited, coord, word):
    if word == '':
        return True

    checkPos = [
        [coord[0]-1, coord[1]],
        [coord[0], coord[1]-1],
        [coord[0]+1, coord[1]],
        [coord[0], coord[1]+1],
    ]

    visited.append(coord)
    for p in checkPos:
        if p[0] >= 0 and \
           p[1] >= 0 and \
           p[0] < len(board) and \
           p[1] < len(board[p[0]]) and \
           board[p[0]][p[1]] == word[0] and \
           p not in visited and \
           findString(board, visited, p, word[1:]):
            return True

    visited.pop()
    return False


if __name__ == '__main__':
    testCases = [
        (
            [
                ['A', 'B', 'C', 'E'],
                ['S', 'F', 'C', 'S'],
                ['A', 'D', 'E', 'E']
            ],
            {"ABCCED": True, "SEE": True, "ABCB": False}
        ),
        (
            [
                ['A', 'B', 'B', 'C'],
                ['E', 'D', 'D', 'D'],
                ['E', 'F', 'D', 'G']
            ],
            {"AEDDDC": True, "FDBBDDF": False, "DCBDDF": True}
        ),
    ]

    for case in testCases:
        print(f"Board: {case[0]}\n")
        for test, value in case[1].items():
            solution = solve(case[0], test)
            print(f"Test Case: {test}")
            print(f"Test Solution: {value}")
            print(f"Actual Solution: {solution}")
            print(("SUCCESS" if solution == value else "FAILURE") + "\n")

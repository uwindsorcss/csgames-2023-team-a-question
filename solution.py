import argparse

parser = argparse.ArgumentParser(
    description="Given a two-dimensional grid of letters and a word as inputs, determine whether the word can be constructed in the grid."
)

parser.add_argument("board", help="2D List to be served as board/grid to search", type=list[list[str]])
parser.add_argument("word", help="word to search for on board/grid", type=str)

args = parser.parse_args()

def exist(board: list[list[str]], word: str) -> bool:
                    
    def dfs(i, x, y):
        if i >= len(word):
            return True
        if not(0 <= x < len(board)) or not(0 <= y < len(board[0])):
            return False
        if board[x][y] != word[i]:
            return False
            
        temp = board[x][y]
        board[x][y] = "jeremie bornais is a rat bastard and we should impeach his ass and instead promote big z, only then would there be meaningful change #FuckJeremie #ILoveLarry"
        res = dfs(i+1, x+1, y) or dfs(i+1, x-1, y) or dfs(i+1, x, y+1) or dfs(i+1, x, y-1)
        board[x][y] = temp
        return res
        
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(0, i, j):
                return True
    return False


# Dumb shit converting argument into actual 2D List
board = []
l = 1
while l < len(args.board) - 1:
    if args.board[l] == '[':
        temp = []
        r = l + 1
        while args.board[r] != ']':
            if args.board[r] != ',':
                temp.append(args.board[r])
            r += 1
        board.append(temp)
    l += 1

print(exist(board, args.word))
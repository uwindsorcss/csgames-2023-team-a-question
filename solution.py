import sys

def find_word(board, word):
  def dfs(row, col, seen, togo):
    if len(togo) == 0:
      return True
    if not (0 <= row < len(board)):
      return False
    if not (0 <= col < len(board[0])):
      return False
    if (row,col) in seen:
      return False
      
    seen.add((row, col))
    if board[row][col] == togo[0]:
      if dfs(row-1,col,seen,togo[1:]):
        return True
      if dfs(row+1,col,seen,togo[1:]):
        return True
      if dfs(row,col-1,seen,togo[1:]):
        return True
      if dfs(row,col+1,seen,togo[1:]):
        return True
    
  for r in range(len(board)):
    for c in range(len(board[0])):
      if dfs(r,c,set(), word):
        return True
  return False
  
# for input, read in each line from stdin and split it by spaces into a list, then append this list to a list of lists that represents our matrix. the final list in this matrix is the target word
matrix = []
test = "S"
for line in sys.stdin:
  linestr = line[:len(line)-1]
  matrix.append(list(linestr.replace(" ", "")))
  if line[1] != ' ':
    break

print(find_word(matrix[:-1], "".join(matrix[-1])))
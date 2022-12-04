import pprint
def adj(board,word, i, j):
  if word == "":
    return True
      
  elif i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
    return False
      
  board[i][j] = 0
  if (adj(board,word[1:],i-1,j) or adj(board,word[1:],i+1,j) or adj(board,word[1:],i,j-1) or adj(board,word[1:],i,j+1)):
    return True
    
  return False
    
def exist(uBoard, word):  
  for i in range(len(uBoard)):
    for j in range(len(uBoard)):
      if adj(uBoard,word[1:],i,j):
        return True
              
  return False
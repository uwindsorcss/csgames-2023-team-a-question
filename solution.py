class Solution:
    rowmax = 0
    colmax = 0
    board = []
    word = ""
    def canconstword (self,board:list, word:str) -> bool: 
        self.rowmax = len(board)
        self.colmax = len(board[0])
        self.board = board
        self.word = word
        #iterate through board, if value does not start with word[0], skip value
        #go row,
        #then go by column
        for a in range(len(board)): #for each row in board
            for b in range(len(board[0])): #for each column in board
                if board[a][b] == word[0]: #if row element, starts with the first letter of the word
                    if (self.backtrack(a,b)):
                        return True
        return False #assume false by default
        
    def backtrack(self,a:int,b:int):
        movelist = []
        forbidlist = []
        originala = a
        originalb = b
        #started at position a + b
        #first check down adjacent value if not match word backtrack, 
        #check up adjacent value
        #check left adjacent value
        #check right adjacent
        while (len(forbidlist) < 4):
            #check if first move is not in forbidden moves 
            #make sure cant do opposite moves (inf loop possiblity)
            i = 1
            while (i < len(self.word)):
                    if self.movedown(a,b,i) and (i != 1 or 'down' not in forbidlist) and (len(movelist) == 0 or movelist[-1] != 'up'):
                        movelist.append('down')
                        a = a + 1
                    elif self.moveup(a,b,i) and (i != 1 or 'up' not in forbidlist) and (len(movelist) == 0 or movelist[-1] != 'down'):
                        movelist.append('up')
                        a = a -1
                    elif self.moveleft(a,b,i) and (i != 1 or 'left' not in forbidlist) and (len(movelist) == 0 or movelist[-1] != 'right'): 
                        movelist.append('left')
                        b = b -1
                    elif self.moveright(a,b,i) and (i != 1 or 'right' not in forbidlist) and (len(movelist) == 0 or movelist[-1] != 'left'):
                        movelist.append('right')
                        b = b + 1
                    else:
                        a = originala
                        b = originalb
                        if (len(movelist) != 0): 
                            forbidlist.append(movelist[0])
                        else:
                            return False
                        movelist = []
                        i = 0
                    i += 1
            if (self.board[a][b] == self.word[len(self.word)-1] and i == len(self.word)): #valid condition
                    return True
        return False

    #moving across the array    
    def movedown(self,a,b,i):
        if (a>=0 and a+1 < self.rowmax and self.board[a+1][b] == self.word[i]):
                return True
        return False
    def moveup(self,a,b,i):
        if (a-1>=0 and a < self.rowmax and self.board[a-1][b] == self.word[i]):
            return True
        return False
    def moveright(self,a,b,i):
        if (b>=0 and b+1 < self.colmax and self.board[a][b+1] == self.word[i]):
            return True
        return False
    def moveleft(self,a,b,i):
        if (b-1>=0 and b < self.colmax and self.board[a][b-1] == self.word[i]):
            return True 
        return False      

#for testing process
def test(board,word,exp = True):
    s = Solution()
    if (not( s.canconstword(board,word) == exp)) :
        print("test case " + word + " failed")

b1 = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
] #board for testing


test(b1,"ABCCED")
test(b1,"SEE")
test(b1,"ABCB",False)

      
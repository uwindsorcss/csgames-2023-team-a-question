

#Arfaa Rashid
#solution.py
#Team A Solution

#implements depth first search
#finds every occurence of the first letter in the word to use as potential start positions
#tries dfs for each; if the next node is the next letter, then recursively continues dfs until the last letter is reached. otherwise, doesnt bother continuing

import sys

#taking input
inp = sys.stdin.read()
colSize = len(inp[:inp.index("\n")])//2 + 1
flat = inp.replace("\n", " ").strip().split(" ")
word = flat.pop()

#creating adjacency list to use in dfs
g = []                              #2d adjacency list -> position of letter in flat corresponds to position of list in g. list holds tups indicating which letters it is adj to  

startPositions = []                 #holds positions of occurences of first letter of word in flat, to be used as potential start positions for dfs
for i, let in enumerate(flat):
    adj = []

    if i-1 >= 0:                                            #if position of adjacent node is not off the board, then it is added to adj as a tup containing the position in flat and the letter itself
        adj.append((i-1, flat[i-1]))    #left
    if i+1 < len(flat):
        adj.append((i+1, flat[i+1]))    #right
    if i-colSize >= 0:                                      #colSize is length of board. +- colSize gives position in flat of adjacently above and below nodes
        adj.append((i-colSize, flat[i-colSize]))    #up
    if i+colSize < len(flat):
        adj.append((i+colSize, flat[i+colSize]))    #down
    g.append(adj)

    if let == word[0]:                  #finding potential start positions for dfs
        startPositions.append(i)


#implementing dfs
def dfs(node, visited, word, i):        
    #i indicates index of word at which the letter we are currently looking for is at
    #node is a tuple with [0] being position of letter in flat, visited, etc; and [1] being string containing letter
    global reachable

    visited[node[0]] = True 
    if node[1] == word[i]:          #if letter in current node is same as letter we are looking for, we can move onto the next letter and continue dfs
        if (i==(len(word)-1)):          #entire word has been found
            reachable = True
            return
        for nxt in g[node[0]]:
            if not visited[nxt[0]]:
                dfs(nxt, visited, word, i+1)


visited = [False for i in range(len(g))]            #used to make sure used nodes are not revisited. each index corresponds to index in flat of letter
reachable = False                                   #flag to indicate if word can be made or not
for startPosition in startPositions:                  
    node = (startPosition, flat[startPosition])
    dfs(node, visited, word, 0)
    if (reachable):
        break

if reachable:
    print("True")
else:
    print("False")
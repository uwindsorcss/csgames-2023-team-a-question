
# Question

Given a two-dimensional grid of letters and a word as inputs, determine whether the word can be constructed in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are horizontally or vertically neighbouring. The same letter cell may not be used more than once.

### Example:
```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
```

Given word = "ABCCED", return true.

Given word = "SEE", return true.

Given word = "ABCB", return false.


### Input:
1) `board` - 2D array of characters
2) `word` - String word that you are looking for in the board

Assume inputs are separated by spaces and new lines. So for Team A it will look like:
```
A B C E
S F C S
A D E E
word
```


### Output:
Boolean value representing whether the word can be found (true) in the board or not (false). Your function should return this value.

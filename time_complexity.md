### (Worst Case) Time Complexity

Suppose the input grid is MxN. In the worst case, every element of the grid is the same letter,
say 'A', and the length of the word is greater than MxN such that every letter in the word is
also this letter. This guarantees that the word can begin at each of the MxN cells. Now, as we
conduct a DFS for each cell in the grid, each cell can have up to 3 unvisited neighbours (other
than the first cell which can have 4). Now, since each DFS will span all MxN nodes, we have the
following recurrence to model the number of operations done:

  T(k) <= 3T(k-1)

We are interested in finding T(MxN).

T(MxN) <= 3T(MxN-1)
<= 3(3T(MxN-2))
<= 3(3(3T(MxN-3)))
<= ...
<= 3^(MxN-1)T(1)
= 3^(MxN-1)

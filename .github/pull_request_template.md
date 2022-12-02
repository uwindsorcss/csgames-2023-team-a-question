# CS Games 2023 Team A Application

PLEASE FILL IN THE FOLLOWING!

> ok

## Full Name

Cole Fuerth

## UWindsor Email

[fuert11g@uwindsor.ca](mailto:fuert11g@uwindsor.ca)

## Application Form

- [x] I certify I have submitted the [application form](https://forms.office.com/r/R4A1JyB3Xf)

## Briefly explain how your solution works and how to run it 

### Brief

I first developed my solution in Python, then remade it in C++ for speed. **I would prefer the C++ solution to be considered, since it is considerably faster**, but it should still be noted that the Python solution came first, and runs almost as fast. The Python is also (understandably) much easier to read and understand, since the solutions are very much the same algorithmically.
### How it works

My solution first tries to find exceptional cases that clearly will not fit first, then picks the better order of characters of the word (reversing the word will not change whether it fits the puzzle, and the order with the least starting points runs exponentially faster). Once it is known all the characters in the string appear on the board frequent enough to potentially fit, and that we have the optimal order of characters, a **depth first** approach is employed. Using sets to keep track of points, the board, and history, we can keep track of everything using set operations. `dfs` exhaustively tries all possible paths for the string, until eventually either fitting or exhausting all possibilities.

### Running the code

On **leetcode** (how I assume you are testing), you can copy and paste either of the solutions that are found under the **leetcode** folder directly onto the site. The C++ solution is in the top 1.5% of submissions; the Python solution is in the top 10% for runtime.

**Locally**, I am testing using `make` with the provided Makefile, or `python3 solution.py`. The test case is hard coded into `main` on each of the source files in the root directory.

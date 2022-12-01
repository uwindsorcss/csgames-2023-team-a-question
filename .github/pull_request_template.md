# CS Games 2023 Team A Application

PLEASE FILL IN THE FOLLOWING!

> ok

## Full Name

Cole Fuerth

## UWindsor Email

fuert11g@uwindsor.ca

## Application Form

- [x] I certify I have submitted the [application form](https://forms.office.com/r/R4A1JyB3Xf)

## Briefly explain how your solution works and how to run it 

My solution uses dfs to find the result. The first recursive call to `search()` includes the entire array as the possible set of starting points. For each call to `search()`, it trims the list to the points that match the first character of the word, then generates a valid list of adjacent points that have not been visited yet, and makes a recursive call to `search()` with the adjacent points, the word with the current character popped off, and the updated points visited so far.

On **leetcode** (how I assume you are testing), this solution uses python3. You copy the body of the evaluate() function into exist() in leetcode, and copy my `import`s and `search()` function to the top of the script.

**Locally**, I am testing using `python3 solution.py < sample_input.txt`, where sample_input.txt contains the input. Input is read in on `stdin`, the way it is formatted in the problem statement.

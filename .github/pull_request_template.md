# CS Games 2023 Team A Application

PLEASE FILL IN THE FOLLOWING!

## Full Name
Zain-Ul-Ebad Raza
otherwise known as **big z**

## UWindsor Email
razaz@uwindsor.ca

## Application Form
- [x] I certify I have submitted the [application form](https://forms.office.com/r/R4A1JyB3Xf)

## Briefly explain how your solution works and how to run it 

### Explanation
My solution is a depth first search solution that checks all decision paths from a certain character. There are a couple of false exit cases such as index being out of range and the current character being checked does not match `word[i]`. There's also some temp variable fuckery just so that it doesn't visit an already checked index.

### How to Build
It works in terminal, enter your command like this (once u cd in):

`python3 solution.py <board> <word>`

you're supposed to enter in the parameters like you would if you were coding the function yourself so here are a couple of examples.

`python3 solution.py [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] "ABCCED"`

`python3 solution.py [["A"]] "A"`

`python3 solution.py [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] "ABCCEDO"`

alternatively you could be a lazy fuck and just copy and paste the function into LeetCode like a fkn demon but I just recommend you make a script or something idgaf ima go spend my time learning 4th grade french.
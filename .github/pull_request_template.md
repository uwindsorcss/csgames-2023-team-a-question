# CS Games 2023 Team A Application

PLEASE FILL IN THE FOLLOWING!

## Full Name
Mathew Pellarin

## UWindsor Email
pellarim@uwindsor.ca

## Application Form
- [x] I certify I have submitted the [application form](https://forms.office.com/r/R4A1JyB3Xf)

## Briefly explain how your solution works and how to run it 

My solution first checks for any cases that might cause the program to timeout due to run time length. It first checks if there is enough occurences of the letters within the board for the given the string and if not fails it. It then check if the last character appears more times then the first and reverses the string if so. 

A recursive function is called and this function first goes through prechecks to check if a letter is matched, the rows and coloumns are in range, if the letter was visted before or if the letter does not match the needed letter. If the letter is correct, add it to a correct set and check all adjecent letters for the next character calling itself recursivly. Once all letters are found return the restult

The variables are hard coded for testing. To test other inputs, chnaging the board and word variable will allow for other testing results. There is also a folder with a script that can be run on codeleet
# CS Games 2023 Team A Application

PLEASE FILL IN THE FOLLOWING!

## Full Name
Juan P. Villalobos Rujano

## UWindsor Email
villaloj@uwindsor.ca

## Application Form
- [x] I certify I have submitted the [application form](https://forms.office.com/r/R4A1JyB3Xf)

## Briefly explain how your main works and how to run it 
When the main file is run, it will construct a 2D array of the same dimensions as the examples given (3x4) using user input. The input must be entered into the console and must be a row of 4 char values separated by spaces, three such rows must be entered; Each row is converted into a char array and assigned to the 2d array at array[i]. Lastly, the programs asks for a word from the user and passes both word and array[][] variables into solution().

In solution() we first construct a Board obj which has the properties a[][] to store the 2D array, explored to keep track of the stage of exploration for a given point in a, and path[] to store the path numbers used to spell the word. A path number is a unique identifier for each element in a[][] that is calculated as row_number*row_size + column_number. The search function will iterate through a[][] at a specified starting point and if it finds a value of a[i][j] that equals the 3rd parameter passed into search(), char c, it will return the page number. Otherwise, it returns -1.

available() iterates through path[] to determine if it contains a specific page number, this helps us determine if a specific element in a[][] has already been passed through once.

Returning to solution(), we find the pathNum of the first char in word and assign it to path[0], then we initialize boolean terminate and enter a do-while loop. The loop will continue until path[] is full or terminate becomes true. In the loop we enter a switch that takes board.explored as its parameter. If explored is equal to -1, the algorithm has reached a dead-end and will set terminate equal to true and return false. If case is between 0-3, it will check a cardinal direction of from the current position in the path and check if that neighbour is both equal to the next letter and has not been passed through in path[].

If explored reverts to default in the switch, a given position has checked all four of its neighbours and none of them are the next letter. Therefore, we must either revert to the previous position in the path and check the next direction, we must search for another element in a[][] to be the first letter in the path if the old path was a dead-end, or we must terminate the loop if there are no more candidates for path[].

When the loop ends, we either return false if terminate = true or we return true if it doesn't as that would mean a viable path that spells the 'word' has been found.

The solution() function has been tested using the test cases in the solutionTest.java file.
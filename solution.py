from copy import copy

def solution(grid: list[list[str]], word: str) -> bool:
    """Word finder"""

    def _solution(grid: list[list[str]], word: str, row: int, col: int) -> bool:
        """Inner recursive solution"""
        result = False
        try:
            #base case
            if len(word) == 0:
                result = True
            #next letter found
            elif word[0] == grid[row][col]:
                copied_grid = copy(grid) #needed to prevent repeat letters
                copied_grid[row][col] = '\0'
                result = result or \
                _solution(copied_grid, word[1:], row + 1, col) or \
                _solution(copied_grid, word[1:], row - 1, col) or \
                _solution(copied_grid, word[1:], row, col + 1) or \
                _solution(copied_grid, word[1:], row, col - 1)
        #stay within bounds of the grid
        except IndexError:
            pass
        return result

    result = False
    #search for the word starting with every instance of the first letter
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == word[0]:
                result = result or _solution(copy(grid), word, row, col)
    return result

def main():
    """Driver code"""
    grid = list()

    #get user input
    while True:
        data = input().split(' ')
        if len(data) > 1:
            grid.append(data)
        else:
            #print out solution
            print(solution(grid, ''.join(data)))
            break

main()

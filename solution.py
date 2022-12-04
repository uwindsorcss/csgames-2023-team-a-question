def solution(grid: list[list[str]], word: str) -> bool:
    """Word finder"""
    rows, cols = len(grid), len(grid[0])
    def _solution(grid: list[list[str]], word: str, row: int, col: int) -> bool:
        """Inner recursive solution"""
        result = False
        if len(word) == 0: #base case
            result = True
        elif not (0 <= row < rows and 0 <= col < cols): #no invalid indices
            pass
        elif word[0] == grid[row][col]: #next letter found
            grid[row][col] = '\0'
            result = result or \
            _solution(grid, word[1:], row + 1, col) or \
            _solution(grid, word[1:], row - 1, col) or \
            _solution(grid, word[1:], row, col + 1) or \
            _solution(grid, word[1:], row, col - 1)
            grid[row][col] = word[0]
        return result

    result = False
    for row in range(len(grid)): #search starting with each instance of first letter
        for col in range(len(grid[row])):
            if grid[row][col] == word[0]:
                result = result or _solution(grid, word, row, col)
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

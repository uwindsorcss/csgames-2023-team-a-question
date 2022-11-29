
#import numpy as np 

#gets the input and store them linearly
def get_input():
    line = [] 
    
    while True:
        row_input = input()

        # if the users enter 'null' then it means that the 2d array was inputted and  
        # the next input line is going to be the last one and its going to be the string to search for 
        if row_input == '':
            line.append(input()) #this is the string
            break      
        
        # we add every line of input in an array as a nested lst , and then pop the last element 
        #and store it as the string to look for 
        line.append(row_input.split())
    #print(line)
    return line  

#returns the deimension of the matrix 
def get_size(matrix): 
    return len(matrix) , len(matrix[0])  

#create a n * m matrix and initializes each index with False
#def create_bool_mtx(n , m): 

    bool_mtx = np.zeros((n ,m),dtype=bool)
    #print(bool_mtx)
    return bool_mtx 


#the function that calls the scavenger 
# checks to see if the board and input are valid  to pass to scavenger 
# if everything is good , calls scavenger for every index of the matrix 
def identifier (mtx, wrd) :
    
    n , m = get_size(mtx)
    if ( mtx == None or wrd == None or wrd.strip() == "" or n <= 0 or m <= 0   ) : 
        return False #returns false if the mtx or wrd were invalid 
    
    #create the bool_array for to keep track of visited nodes 
    #bool_mtx = create_bool_mtx(n,m)


    # go through each index in the mtx and see if the wrd wrd 
    #is constructable from its neighbour indexes 
    for i in range(0,n) : 
        for j in range (0,m) : 
            if Scavenger(mtx, wrd , i , j , 0) : # 0  is passed as the defaukt counter, it will increment in 
                return True                                 # scavenger if the characters match  
            
    # if the scavenger didnt find the match return False 
    return False 

# To be implemented .. 
# n & m are i & j , count is number of matched characters  
def Scavenger(mtx, wrd, i , j , count) :
    
    #wrd_stack = list(wrd) #lst of characters of keyword
    #print("The KeyWord_Stack is:", wrd_stack)

    #n is the lenght and m is the height of mtx 
    n , m = get_size(mtx) 

    #in case we found all the chars 
    if (len(wrd) == count ): 
        return True 
    
    # return false if :
    #   charcters dont match 
    #   i is out of bound or j is out of bound   
    if  i<0 or n <= i or j<0 or  m <= j or  mtx[i][j] != wrd[count]:
        #bool_mtx = False  # reseting the value of boolean matrix 
        return False 

    # this is the case were the characters match and i and j are still in bound 
    #bool_mtx[i][j] = True  
    
    
    mtx[i][j] = '-' # changing the char to avoid recounting the same index 
    # using recursion , we go right, left  , up and down respectively from each index here  
    result =  Scavenger( mtx, wrd, i + 1 , j , count + 1 ) or  \
    Scavenger( mtx, wrd, i - 1 , j , count + 1 ) or  \
    Scavenger( mtx, wrd, i , j + 1 , count + 1) or  \
    Scavenger( mtx, wrd, i , j -1 , count + 1)  
    mtx[i][j] = wrd[count] # switching back to the original character to keep the originaol mtx
    return result 




if __name__ == '__main__' : 

    #Instructions 
    print("  ================ WELCOME ================")
    print(f"- Enter each row of matrix and then press 'Enter', \n"
    "- When you are done inputting the matrix , press 'Enter' once more.\n"
    "- Then you can input the keyword that you'd like to search for!\n" 
    "  =========================================> ")


    # Get the Input, Seperate the Matrix and the KeyWord 
    mtx = get_input() #mtx represents matrix 
    wrd =  mtx.pop(-1) # wrd represents keyword  

    # we get the n, m to create the boolean function
    n , m  = get_size(mtx) #an array holding the dimensions of mtx
    
    #print statements  
    print("  ============== PROCCESSING ==============")
    print("- The Matrix is:", mtx)
    print("- The KeyWord is:", wrd)
    print(f"- Dimentions n = {n}, m = {m}")
    result = identifier(mtx, wrd )
    print(f"- result: {result}")
    print("  =========================================")
    
    #Scavenger() returns True or False 
    # depending of the presence of the keyword in mtx   
    #result = Scavenger()
    exit 
    



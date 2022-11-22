
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

#this function will help us find the first character using devide and conqour method 
# so the first iteration is as fast as possible 
def find_first_char():
    return None 


def identifier(mtx , wrd , wrd_stack) :
    
    #if  (not find_first_char()):
        #return False
    #else : 
    
    #while True: 
        # look_left() 
        #...

    return None

if __name__ == '__main__' : 

    # Get the Input, Seperate the Matrix and the KeyWord 
    mtx = get_input() #mtx represents matrix 
    wrd =  mtx.pop(-1) # wrd represents keyword 
    wrd_stack = list(wrd) #lst of characters of keyword 
    
    #print statements  
    print("The Matrix is:", mtx)
    print("The KeyWord is:", wrd)
    print("The KeyWord_Stack is:", wrd_stack)

    
    #call the identifier function
    result = identifier()
    print(result)
    



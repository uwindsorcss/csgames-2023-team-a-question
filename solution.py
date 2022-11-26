
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

'''just an idea
aybe we need 2 stacks so we can keep track of the index of the keyword that has been found 
and so if we find any char that matches we addd that char to the second stack and remove that char from our main stack, 
and if main was empty we know that the entire keyword matches 
and if we get to a point that there is no match we can simply reconstruct the keyword by transfering back the characters from the 
second stack to the first stack 
we can also create a function that does this stack transfer for simplicity and لاتی reasons 
[]use try else  to o around exceptions 
'''

"""he said i should be able to get the n*m of the input first 
then create another 2D array same with size n*m ( same size as original) __
and the values that it holds are just true and false and they are corresponding to the 
attribute "visited_before" of each index of the original matrix. 
this matrix will help me make sure that i dont visit the same character


he was supportive of the 2 stack idea 
but he said after i made it work i could possibly try to apply it using recursion 

also for out of bound : 
he said the try / except is okay but the regular way of doing this 
is that first of all o need the size of the original (n*m) and then when ever 
i wanna move to the right for example (add (0,1)) then i check that future index will be less than n so i wouldnt go out of the lenght 
if i wanna move to the top for example (add (1,0)) then i check the future index will be less than m .
"""

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
    



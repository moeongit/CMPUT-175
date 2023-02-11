#----------------------------------------------------
# Lab 5, Exercise 2: Web browser simulator
# Purpose of program:
#
# Author: Mohammed Al Robiay
# Collaborators/references:
#----------------------------------------------------

from stack import Stack

def getAction():
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''
    #delete pass and write your code here
    pass

def goToNewSite(current, bck, fwd):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''   
    #delete pass and write your code here
    pass
    
def goBack(current, bck, fwd):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''    
    #delete pass and write your code here
    pass

def goForward(current, bck, fwd):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''    
    #delete pass and write your code here
    pass

def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        try:
            action = getAction()
            
        except Exception as actionException:
            print(actionException.args[0])
            
        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            elif action == '<':
                current = goBack(current, back, forward)
            elif action == '>':
                current = goForward(current, back, forward)
            elif action == 'q':
                quit = True
            #TO DO: add code for the other valid actions ('<', '>', 'q')
            #HINT: LOOK AT LAB 4
            
            
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    
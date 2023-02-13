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
    Inputs: asks the user for a command
    Returns: the valid character entered by the user (str)
    '''
    action = input("Enter a command ('=', '<', '>', or 'q'): ")
    return action

def goToNewSite(current, bck, fwd):
    '''
    Inputs: 
    - current: the current website (str)
    - bck
    - fwd
    Returns: the new website address (str)
    '''
    newSite = input("URL: ")
    bck.push(current)
    fwd.clear()
    return newSite

def goBack(current, bck, fwd):
    '''
    Inputs: 
    - current: the current website (str)
    - bck
    - fwd
    Returns: the previous website address (str)
    '''
    try:
        prevSite = bck.pop()
        fwd.push(current)
        return prevSite
    except:
        print("Cannot go back.")
        return current

def goForward(current, bck, fwd):
    '''
    Inputs: None
    - current: the current website (str)
    - bck
    - fwd
    Returns: the next website address (str)
    '''
    try:
        nextSite = fwd.pop()
        bck.push(current)
        return nextSite
    except:
        print("Cannot go forward.")
        return current


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
            if action not in ('=', '<', '>', 'q'):
                raise Exception('Invalid entry.')
                
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
    
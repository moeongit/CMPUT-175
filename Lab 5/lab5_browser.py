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
    Prompts the user to enter a character for navigation:
    '=' to enter a new website address, 
    '<' to go back to previous website,
    '>' to go forward to next website, or 
    'q' to quit the browser simulation
    Inputs: None
    Returns: the valid character entered by the user (str)
    '''
    action = input("Enter a command ('=', '<', '>', or 'q'): ")
    return action

def goToNewSite(current, bck, fwd):
    '''
    Prompts the user to enter a new website address, 
    returns that address as a string, 
    and updates the back and forward stacks as appropriate
    Inputs: 
    - current: the current website (str)
    - bck: a reference to the Stack holding the webpage addresses to go back to
    - fwd: a reference to the Stack holding the webpage addresses to go forward to
    Returns: the new website address (str)
    '''
    newSite = input("URL: ")
    bck.push(current)
    fwd.clear()
    return newSite

def goBack(current, bck, fwd):
    '''
    Goes back to the previous website, 
    handles any exceptions raised by the Stack class, 
    updates the back and forward stacks as appropriate,
    and returns the previous website
    Inputs: 
    - current: the current website (str)
    - bck: a reference to the Stack holding the webpage addresses to go back to
    - fwd: a reference to the Stack holding the webpage addresses to go forward to
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
    Goes forward to the next website, 
    handles any exceptions raised by the Stack class, 
    updates the back and forward stacks as appropriate,
    and returns the next website
    Inputs: 
    - current: the current website (str)
    - bck: a reference to the Stack holding the webpage addresses to go back to
    - fwd: a reference to the Stack holding the webpage addresses to go forward to
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
    
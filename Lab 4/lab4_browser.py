#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program:
#
# Author: Mohammed Al Robiay
# Collaborators/references:
#----------------------------------------------------

def getAction():
    '''
    Write docstring to describe function
    Inputs: None
    Returns: string
    '''
    choices = ["=", "<", ">", "q"]
    user_input = input("Enter = to enter a URL, < to go back, > to go forward, q to quit: ")
    if user_input not in choices:
        print("Invalid Entry.")
        getAction()
    return user_input


def goToNewSite(current, pages):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''   
    # TO DO: delete pass and write your code here
    enter_url = input("Enter URL: ")
    pages.append(enter_url)
    return len(pages) - 1

    
def goBack(current, pages):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''    
    # TO DO: delete pass and write your code here
    if current == 0:
        print("Cannot go back.")
    return current - 1

def goForward(current, pages):
    '''
    Write docstring to describe function
    Inputs: None
    Returns: str
    '''    
    # TO DO: delete pass and write your code here
    if current < len(pages) - 1:
        return current + 1
    else:
        print("Cannot go forward.")


def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    currentIndex = 0
    quit = False
    
    while not quit:
        print('\nCurrently viewing', websites[currentIndex])
        action = getAction()
        
        if action == '=':
            currentIndex = goToNewSite(currentIndex, websites)
        elif action == '<':
            currentIndex = goBack(currentIndex, websites)
        elif action == '>':
            currentIndex = goForward(currentIndex, websites)
        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    
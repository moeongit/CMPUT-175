#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program: This program acts as a webbrowser in the sense that you can choose to type a url and go back or forward with the home webpage being www.cs.ualberta.ca.
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
    Inputs: int, list
    Returns: int
    '''   
    # TO DO: delete pass and write your code here
    for i in range(len(pages)):
        if i > current:
            pages.pop()
    pages.append(input("URL: "))
    return current + 1

    
def goBack(current, pages):
    '''
    Write docstring to describe function
    Inputs: list, int
    Returns: int
    '''    
    # TO DO: delete pass and write your code here
    if current == 0:
        print("Cannot go back.")
        return current
    return current - 1

def goForward(current, pages):
    '''
    Write docstring to describe function
    Inputs: list, int
    Returns: int
    '''    
    # TO DO: delete pass and write your code here
    if current == len(pages) - 1:
        print("Cannot go forward.")
        return current
    return current + 1


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
    
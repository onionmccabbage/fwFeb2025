def addThem(a,b):
    return a+b

def squareIt(n):
    return n**2 # here the double asterisk means raise to the power...



if __name__ == '__main__':
    # we use the above line to protect code
    #e.g. we ONLY want the following to run when THIS module is called directly
    # i.e. we exercise this module here, condifent the exercise code will not be used on import
    print(f'This module is called {__name__}')
    addThem(3,2)
    say = 'it is nearly \nthe end' # \n means a new line character
    print(say)
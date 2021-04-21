def checkForOne(number):
    '''
    Returns True if the number is 1.
    number: an input of an integer by the user. '''
    if number == 1:
        return True

def collatz(number):
    '''
    Checks to see if number is 1, even, or odd.
    If number is even, it is divided by two and the value is printed.
    If number is odd, it is multiplied by 3 and added by one and the value is printed.
    performs a loop of operations until 1 can be returned. '''
    while True:
        if checkForOne(number):
            return 1
        if number % 2 == 0: # checks to see if number is divisible by 2
            number = number // 2 # divides number by 2 and returns an integer
            if number == 1:
                return number
            else:
                print(number)
        else:
            number = 3 * number + 1
            if number == 1:
                return number
            else:
                print(number)

def cSequence():
    '''
    Allows the user to input a number for the program to run.
    Quits program if userInput is "q".
    Uses exception handling to determine if input is an integer. '''
    while True: # The main program loop
        try:
            userInput = input('Please type any integer, or \'q\' to quit. ')
            if userInput == 'q':
                return 'goodbye!'
            else:
                print(collatz(int(userInput)))
        except ValueError: # Happens if input is anything but an integer
            print('Oops! That was no valid number. Try again.')

print(cSequence())
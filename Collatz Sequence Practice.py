#Practise! (Collatz Sequence Exercise)

import sys

def collatz(number):
    '''If number is even, then collatz() should print number // 2 and return this value.
    If number is odd, then collatz() should print and return 3 * number + 1.'''

    if (number % 2 == 0):
        print(number // 2)
        return (number // 2)

    elif (number % 2 == 1):
        print(3 * number + 1)
        return (3 * number + 1)

    else:
        print('Program error')
        sys.exit()

while True:
    
    try:
        x = int(input("Enter number: "))
        while x != 1:
            x = collatz(x)
        print()

    except ValueError:
        print('Enter an integer.\n')
        continue

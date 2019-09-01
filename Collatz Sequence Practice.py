#Practise! (Collatz Sequence Exercise)

print('''This is a Python program answer for the program project of Chapter 3 of
    Automate The Boring Stuff with Python book\n''')
print('''
    Copyright (C) 2019 Nicholas Kang
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.\n\n''')
print("Feel free to contact the author at zt.kang@gmail.com or PM 'Nicholas Kang' in Orbiter Forum for bug reports and/or comments.\n")

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

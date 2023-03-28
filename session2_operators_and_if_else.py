# # 1
# # Briefly explain in your own words how does an if/else statement work.
# # An if/else statement runs a certain part of the code if the condition is True or a separate part of the code if the condition is False.


# # 2
# # Take an integer from input and verify if it is a natural number or not.
# #
# x = int(input('Choose a number: '))
# if x >= 0:
#     print('The number is natural')
# else:
#     print('The number is not natural')


# # 3
# # Take an integer from input and verify if it is positive, negative or neutral.
# #
# x = int(input('Choose a number: '))
# if x < 0:
#     print('negative')
# elif x == 0:
#     print('neutral')
# else:
#     print('positive')


# # 4
# # Take an integer from input and verify if it can be found between -2 and 13 including the start and end values.
# #
# # _________ Solution A: with the range method _________
# #
# x = int(input('Choose number: '))
# if x in range(-2, 14):
#     print('The number is within the range')
# else:
#     print('The number is outside the range')
# #
# # _________ Solution B: with comparisons _________
# #
# x = int(input('Choose number: '))
# if x >= -2 and x <= 13:
#     print('The number is within the range')
# else:
#     print('The number is outside the range')


# # 5
# # Take two integers from separate inputs and verify if the difference between them is smaller than 5.
# # The difference here refers to how many numbers are between them and not their subtraction. Hint: Use the abs() function.
# #
# x = int(input('Choose variable \'x\': '))
# y = int(input('Choose variable \'y\': '))
# if abs(x - y) <= 5:
#     print('The difference smaller or equal to 5')
# else:
#     print('The difference is larger than 5')


# # 6
# # Take an integer from input and verify that it cannot be found between 5 and 27 including the start and end values (use 'not').
# #
# # _________ Solution A: with the range method _________
# #
# x = int(input('Choose a number: '))
# if x not in range(5, 28):
#     print('The number is not within the range')
# else:
#     print('The number is inside the range')
# #
# # _________ Solution B: with comparisons _________
# #
# x = int(input('Choose a number: '))
# if not (5 <= x <= 27):
#     print('The number is not within the range')
# else:
#     print('The number is inside the range')


# # 7
# # Take two integers from separate inputs and verify if they are equal, and if not display the highest one.
# #
# x = int(input('x = '))
# y = int(input('y = '))
# if x == y:
#     print('They are equal')
# elif x > y:
#     print(f'x ({x}) is higher')
# else:
#     print(f'y ({y}) is higher')


# # 8
# # Three integers from separate inputs represent the sides of a triangle. Display if the triangle is either equilateral, scalene or isosceles.
# #
# x = int(input('Side x: '))
# y = int(input('Side y: '))
# z = int(input('Side z: '))
# if x == y == z:
#     print('The triangle is equilateral')
# elif x != y != z:
#     print('The triangle is scalene')
# else:
#     print('The triangle is isosceles')


# # 9
# # Take a letter as input then verify and display if it's a vocal or not. Find a solution for the uppercase and lowercase scenarios as well.
# #
# x = str(input('Choose a letter: ')).lower()
# if x == 'a' or x == 'e' or x == 'i' or x == 'o':
#     print('The letter is a vocal')
# else:
#     print('The letter is not a vocal')


# # 10
# # Transform and print the grades (1-10) form the Romanian educational system to the American one, as follows:
# # a. 9 and 10: A
# # b. Above 8: B
# # c. Above 7: C
# # d. Above 6: D
# # e. Above 4: E
# # f. 4 and Below: F
# #
# x = int(input('Choose a Romanian grade (number): '))
# if not (4 <= x <= 10):
#     print('Invalid grade')
# elif x <= 4:
#     print('F')
# elif x == 5:
#     print('E')
# elif x == 6:
#     print('D')
# elif x == 7:
#     print('C')
# elif x == 8:
#     print('B')
# elif x >= 10:
#     print('A')


# # 11
# # Take a number as input and verify if it has a minimum of 4 digits.
# #
# x = input('x = ')
# if len(x) <= 4:
#     print('The number has less than or 4 digits')
# else:
#     print('The number has more than 4 digits')


# # 12
# # Take a number as input and verify if it has exactly 6 digits.
# #
# x = input('Choose a number: ')
# if len(x) == 6:
#     print('The number has exactly 6 digits')
# else:
#     print('The number does not have 6 digits')


# # 13
# # Take a number from input and verify if it is odd or even
# #
# x = int(input('Choose a number: '))
# if x % 2 == 0:
#     print('The number is even')
# else:
#     print('The number is odd')


# # 14
# # Take three integers from input and display which one of them is the highest
# #
# x = int(input('x = '))
# y = int(input('y = '))
# z = int(input('z = '))
# if x > y and x > z:
#     print(f'Out of {x, y, z} the highest number is {x}')
# elif y > z:
#     print(f'Out of {x, y, z} the highest number is {y}')
# else:
#     print(f'Out of {x, y, z} the highest number is {z}')


# # 15
# # Take three integers from input and imagine these are the angles of a triangle. Verify and display if the triangle is valid or not.
# #
# x = int(input('x = '))
# y = int(input('y = '))
# z = int(input('z = '))
# if x + y + z == 180:
#     print('Valid triangle')
# elif x > z and y > z:
#     print('Valid triangle')
# else:
#     print('Invalid triangle')


# # 16
# # Consider the string: 'Coral is either the stupidest animal or the smartest rock'.
# # Take a number as input and display the string with that number of missing characters from the end of it.
# #
# string = 'Coral is either the stupidest animal or the smartest rock'
# x = int(input('How many characters are cut from the end?: '))
# print(string[0:-x])


# # 17
# # Consider the string: 'Coral is either the stupidest animal or the smartest rock'.
# # Declare a new string that is made out of the first 5 and the last 5 characters of the string.
# #
# string = 'Coral is either the stupidest animal or the smartest rock'
# new_string = string[0:5] + string[-5:]
# print(new_string)


# # 18
# # Consider the string: 'Coral is either the stupidest animal or the smartest rock'.
# # Save in a new variable the starting index of the word 'rock' and then display the string without the word.
# #
# string = 'Coral is either the stupidest animal or the smartest rock'
# index_cut = len(string) - 4
# saved_word = string[index_cut:]
# print(string[:index_cut])


# # 19
# # Take a string as input and verify with an assert method if the first and last characters are the same, while making the program case insensitive.
# #
# string = input('Type a string: ').upper()
# assert string[0] == string[-1]
# print('The first and last characters are the same')


# # 20
# # Consider the string: '0123456789'. First display the even numbers and then the odd ones.
# #
# x = '0123456789'
# print(x[2::2], x[1::2])


# # 21
# # A person can board the plane if either of the conditions below are met:
# # 1. They have over 18 years old and a passport
# # 2. They have under 18 years old, a passport, accompanied by both parents
# # 3. They have under 18 years old, a passport, accompanied by one parent and written approval from the other
# #
# a = int(input('Age: '))
# b = input('Accompanied by the mother? (yes/no) ')
# c = input('Accompanied by the father? (yes/no) ')
# d = input('Passport (yes/no) ')
# e = input('Approval from the mother? (yes/no) ')
# f = input('Approval from the father? (yes/no) ')
# if a >= 18 and d == 'yes':
#     print(f'Age is {a} years old, has passport => can board!')
# elif a < 18 and d == 'yes' and c == 'yes' and b == 'yes':
#     print(f'Age is {a} years old, has passport, both parents, no approvals needed => can board!')
# elif a < 18 and d == 'yes' and (b == 'yes' and f == 'yes') or (c == 'yes' and e == 'yes'):
#     print(f'Age is {a} years old, has passport, at least one parent and the other one\'s approval => can board!')
# else:
#     print('The passenger cannot board due to either missing the passport, a parent or an approval in case they are underage')


# # 22
# # Python game: Guess the dice roll (1-6)
# # Generate a random dice roll and compare it to a user's input, then display one of the three options:
# # the number was higher, the number was lower, the number is matching
# #
# import random
# dice_roll = (random.randint(1, 6))
# number = int(input('Pick a number: '))
# if number == dice_roll:
#     print(f'You guessed right! Congratulations! You picked {number} and the dice was {dice_roll}')
# elif dice_roll < number <= 6:
#     print(f'You lost. Your number was higher. You picked {number} and the dice was {dice_roll}')
# elif number < dice_roll and number <= 6:
#     print(f'You lost. Your number was lower. You picked {number} and the dice was {dice_roll}')
# else:
#     print('Only numbers from 1 to 6 can be picked')


















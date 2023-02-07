# 1
# # In a one line comment explain in your own words what a variable is
# # A variable is a storage space in the memory which we can label and fill with various types of data


# # 2
# # Declare and initialize a variable for each of these data types: string, integer, float, bool.
# # Choose your own values.
# contestant = 'Kevin'
# age = 36
# score = 8.6
# medal = True


# # 3
# # Use type casting to verify if each variable contains the expected data type.
# print(f'\'{contestant}\' has the following variable type: {type(contestant)}')
# print(f'\'{age}\' has the following variable type: {type(age)}')
# print(f'\'{score}\' has the following variable type: {type(score)}')
# print(f'\'{medal}\' has the following variable type: {type(medal)}')


# # 4
# # Round the float using the round() function and save the change in the same variable (overwriting).
# # Verify its type.
# score = round(score)
# print(f'\'{score}\' has now a new variable type which is: {type(score)}')


# # 5
# # Use the print() function to print in the console 4 sentences using those 4 variables.
# print(f'The contestant\'s name is {contestant}.')
# print(f'He is {age} years old.')
# print(f'His current score is {score} out of 10.')
# print(f'Does he own any medals? {medal}!')

# # 6
# # Take a first name as input.
# # Take a surname as input.
# # Print 'The complete name has X characters'
# #
# # _________ Solution A: with an extra variable _________
# first_name = input('Type your first name: \n')
# surname = input('Type your surname: \n')
# total = len(first_name) + len(surname)
# print(f'The full name has a total of {total} characters.')
# #
# # _________ Solution B: without an extra variable _________
# first_name = input('Type your first name: \n')
# surname = input('Type your surname: \n')
# print(f'The full name has a total of {len(first_name) + len(surname)} characters.')


# # 7
# # Take the length of a triangle as input, and then take its width as a separate input.
# # Display 'The area of the triangle is X cm'.
# #
# # _________ Solution A: with an extra variable _________
# length = int(input('Length: '))
# width = int(input('Width: '))
# triangle_area = (length * width) / 2
# print(f'The area of the triangle is {triangle_area} cm.')
# #
# # _________ Solution B: without an extra variable _________
# length = int(input('Length: '))
# width = int(input('Width: '))
# print(f'The area of the triangle is {(length * width) / 2} cm.')


# # 8
# # Considering the string: 'Coral is either the stupidest animal or the smartest rock':
# # Display how many times the combination of letters 'the' is present.
# sentence = 'Coral is either the stupidest animal or the smartest rock'
# print(sentence.count('the'))


# # 9
# # Considering the same string from problem #8:
# # Replace 'the' with 'THE' everywhere and print the result.
# sentence = 'Coral is either THE stupidest animal or THE smartest rock'
# print(sentence.replace("the", "THE"))


# # 10
# # Considering the same string from problem #8:
# # Use an Assert function to verify if the string contains only numbers.
# sentence = 'Coral is either the stupidest animal or the smartest rock'
# assert sentence == int(sentence)
# print('The string contains numbers')


# # 1 (optional)
# # Take from input a string with an odd length and display the middle character.
# #
# # _________Solution A_________(the shortest)
# x = input('Insert an odd string: \n')
# print(f'The middle character is: {x[(len(x) // 2)]}')
# #
# # _________Solution B_________(additional data)
# x = input('Insert an odd string: \n')
# number_of_characters = len(x)
# middle = int(number_of_characters / 2)
# print(f'The middle character is: {x[middle]}')
# print(f'The string has {number_of_characters} characters')
# print(f'The rounded position number of the middle character is: {middle}')
# #
# # _________Solution C_________(accepting only strings with odd character length)
# input_string = str(input('Insert a string with odd character length: '))
# length_string = len(input_string)
# if length_string % 2 != 0:
#     divide_string = length_string // 2
#     print('The middle character is:', input_string[divide_string])
# else:
#     print('Only strings with odd character length are accepted! Rerun script!')


# # 2 (optional)
# # Verify if the string is a palindrome
# #
# # _________Solution A_________(with the Assert method)
# string = input('Enter string: \n')
# assert string == string[::-1]
# print('Yes it is!')
# #
# # _________Solution B_________(with an if/else statement)
# string = input("Enter string: \n")
# if string == string[::-1]:
#     print(Yes it is!')
# else:
#     print('No, it is not!')


# # 3 (optional)
# # Using one line of code take two strings from one input and save both strings in separate variables.
# # Print both variables
# #
# # _________Solution A_________(more lines)
# user_input = str(input('Type two variables: \n'))
# separate = user_input.split(' ')
# var1 = separate[0]
# var2 = separate[1]
# print(f'The first variable is \'{var1}\'')
# print(f'The second variable is \'{var2}\'')
# #
# # _________Solution B_________(more lines)
# user_input = str(input('Type two variables: \n'))
# var1, var2 = user_input.split(' ')
# print(f'The first variable is \'{var1}\' and the second variable is \'{var2}\'.')


# # 4 (optional)
# # Take a string from input and store the first character in a variable.
# # Capitalize this character everywhere except the first and the last one.
# str = input('Type a string: \n')
# char_top = str[0]
# char_bot = str[-1]
# char_mid = str[1:-1]
# print(f'The modified string is: {char_top}{char_mid.replace(char_top, char_top.upper())}{char_bot}')
#
# # 5 (optional)
# # Take a username and a password from input.
# # Display example: "The user's password is ****** and contains 6 characters." (the stars update dynamically)
# #
# # _________Solution A_________(more lines)
# user_name = input('Type the username: \n')
# password = input('Type the password: \n')
# stars = len(password) * '*'
# show = print(f'The password for the user {user_name} is {stars} and has {len(password)} characters.')
# #
# # _________Solution B_________(less lines)
# x = user_name('Type the username: \n')
# y = password('Type the password: \n')
# print(f'The password for the user {user_name} is {len(password) * "*"} and has {len(password)} characters.')










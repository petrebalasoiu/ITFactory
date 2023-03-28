# # 1
# # Having the list below:
# # a. Use a for loop to iterate through the entire list and print out 'My favourite car is {x}'
# # b. Use a for each loop to iterate through the entire list and print out 'My favourite car is {x}'
# # c. User a while loop to iterate through the entire list and print out 'My favourite car is {x}'
# #
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# # a.
# for i in range(len(cars):
#     print(f'My favourite car is {cars[i]}')
# # b.
# for car in cars:
#     print(f'My favourite car is {car}')
# # c.
# i = 0
# while i < len(cars):
#     print(f'My favourite car is {cars[i]}')
#     i += 1


# # 2
# # Having the same list use a for else
# # In for: Modify the elements in the list so that they are written in all caps except the first and the last.
# # In else: Print the list
# #
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# x = len(cars)
# for i in range(x - 1):
#     cars[i] = cars[i].upper()
#     cars[0] = cars[0].lower()
#     cars[x - 1] = cars[x - 1].lower()
#     i = i + 1
# else:
#     print(cars)


# # 3
# # Having the same list
# # A buyer wants the buy a Mercedes
# # Iterate through the list with a for loop until the car is found and print a message to confirm it
# #
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for car in cars:
#     if car == 'Mercedes':
#         print('We found the Mercedes!')
#         break
#     else:
#         print(f'We found a {car}. We\'ll keep looking')


# # 4
# # Having the same list
# # A rich buyer wants to buy one of the expensive cars only. Hence, skip the Trabant and Lastun.
# #
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for car in cars:
#     if car == 'Trabant' or car == 'Lastun':
#         continue
#     print(f'You might like a {car}')


# # 5
# # Replace the cheap cars (Trabant and Lastun) with two Tesla and print the old models and the current models
# #
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# old_cars = []
# for car in cars:
#     if car == 'Trabant' or car == 'Lastun':
#         cars.remove('Trabant')
#         cars.remove('Lastun')
#         cars.append('Tesla')
#         cars.append('Tesla')
#         old_cars.append('Trabant')
#         old_cars.append('Lastun')
#         print(f'Old models: {old_cars}')
#         print(f'Current models: {cars}')


# # 6
# # Having a dictionary with car models, prices and a budget
# # Display only the cars that are within the budget
# # Iterate through the dict.items() and access the car with its price
# #
# car_prices = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
#     }
# budget = 15000
#
# for cars in car_prices:
#     if car_prices[cars] < budget:
#         print(cars)
#
# for cars in car_prices.items():
#     print(cars)
#
# for cars in car_prices:
#     if car_prices[cars] < budget:
#         print(f'For a budget under 15,000 euros you could choose car {cars}')
#
# for cars in car_prices:
#     print(cars)


# # 7
# # Having the list below, iterate through it and display how many times the number 3 appears without using the count method
# #
# numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# duplicates = 0
# for number in numbers:
#     if number == 3:
#         duplicates += 1
# print(duplicates)


# # 8
# # Having the list below, iterate through it and display the sum of the elements without using the sum method
# #
# numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# sum = 0
# for number in numbers:
#     sum += number
# print(sum)


# # 9
# # Having the list below, iterate through it and display the highest number without using the max method
# #
# numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# max = 0
# for number in numbers:
#     if number > max:
#         max = number
# print(max)


# # 10
# # Having the list below, iterate through it and replace the positive numbers with their negative counterparts
# #
# numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# negatives = []
# for number in numbers:
#     if number > 0:
#         number = -abs(number)
#         negatives.append(number)
# print(negatives)


# # 11
# # Having the list below, iterate through it and assign each number in their respective lists
# #
# other_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# even_numbers = []
# odd_numbers = []
# positive_numbers = []
# negative_numbers = []
# for number in other_numbers:
#     if number > 0:
#         positive_numbers.append(number)
#     if number < 0:
#         negative_numbers.append(number)
#     if number % 2 == 0:
#         even_numbers.append(number)
#     if number % 2 != 0:
#         odd_numbers.append(number)
# print(f'Even numbers: {even_numbers}')
# print(f'Odd numbers: {odd_numbers}')
# print(f'Positive numbers: {positive_numbers}')
# print(f'Negative numbers: {negative_numbers}')


# # 12
# # Having the list below, order the numbers in ascension without using the sort function
# #
# other_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# ordered_numbers = []
# while other_numbers:
#     minimum = other_numbers[0]
#     for number in other_numbers:
#         if number < minimum:
#             minimum = number
#     ordered_numbers.append(minimum)
#     other_numbers.remove(minimum)
# print(ordered_numbers)


# # 13
# # Guess the number game
# # secret_number = generate a random number between 1 and 30
# # guessed_number = None
# # Using a while loop the user picks a number and the program displays:
# # The secret number is too high
# # The secret number is too low
# # Congratulations! You guessed it right!
# #
# import random
# secret_number = random.randrange(1, 30)
# guessed_number = int(input("Choose a number: "))
# while secret_number != guessed_number:
#     if secret_number > guessed_number:
#         print("The secret number is higher")
#         guessed_number = int(input("Choose another number: "))
#     elif secret_number < guessed_number:
#         print("The secret number is lower")
#         guessed_number = int(input("Choose another number: "))
#     else:
#         break
# print("Congratulations! You guessed it right!")


# # 14
# # Write a program that generates the following pyramid in the console:
# # 1
# # 22
# # 333
# #
# x = int(input("Choose a number: "))
# for i in range(x + 1):
#     for j in range(i):
#         print(i, end='')
#     print('')


# # 15
# # Iterate through the following list 2D and print 'The current number is {x}'
# #
# tastatura_telefon = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# for x in tastatura_telefon:
#     for y in x:
#         print(f'The current number is {y}')






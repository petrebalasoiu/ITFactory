# # 1
# # Create a function that calculates and returns the sum of two numbers
# #
# def sum_of_numbers(a, b):
#     return a + b
#
#
# print(sum_of_numbers(4, 5))
# print(sum_of_numbers(10, 20))


# # 2
# # Create a function that returns True if a number is even and False if the number is odd
# #
# def odd_or_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
#
# print(odd_or_even(2))


# # 3
# # Create a function that returns the total number of characters in your full name
# #
# def sum_of_letters(*full_name):
#     total = []
#     for name in full_name:
#         for letter in name:
#             total.append(letter)
#     return len(total)
#
#
# print(sum_of_letters('Andrew', 'Martin', 'Walker'))


# # 4
# # Crate a function that returns the area of a rectangle
# #
# def rectangle_area(length, height):
#     return length * height
#
#
# print(rectangle_area(3, 5))


# # 5
# # Create a function that returns the area of a circle
# #
# def circle_area(radius):
#     return 3.14 * (radius ** 2)
#
#
# print(circle_area(4))


# # 6
# # Create a function that returns either True or False if a character 'x' can be found in a given string
# def char_match(char):
#     if 'x' in char:
#         return True
#     else:
#         return False
#
#
# print(char_match('xerox'))


# # 7
# # Create a function without return that takes a string and prints the number of lower case and the number of upper case
# #
# def display_characters(word):
#     number_lowercase = 0
#     number_uppercase = 0
#     for character in word:
#         if character.islower():
#             number_lowercase += 1
#         elif character.isupper():
#             number_uppercase += 1
#     print(f'There are currently {number_lowercase} lower case characters')
#     print(f'There are currently {number_uppercase} upper case characters')
#
#
# display_characters("John is a Good Student")


# # 8
# # Create a function that takes a list of numbers and returns only the positive ones
# #
# def only_positive(*nums):
#     for num in nums:
#         if num > 0:
#             print(num, end=' ')
#
#
# only_positive(11, -21, 0, 45, 66, -93)


# # 9
# # Create a function that takes 2 numbers and prints which one is higher than the other, or if there are equal
# #
# def num_relation(x, y):
#     if x > y:
#         print(f'{x} is higher than {y}')
#     elif x < y:
#         print(f'{y} is higher than {x}')
#     else:
#         print(f'{x} and {y} are equal')
#
#
# num_relation(4, 2)
# num_relation(2, 4)
# relatia_numerelor(3, 3)


# # 10
# # Create a function that takes a number and a set then prints out if the number was added in set or not (due to duplication)
# #
# def add_to_set(number, set_of_numbers):
#     if number in set_of_numbers:
#         print('The number was not added because it already exists in the set')
#         return False
#     else:
#         set_of_numbers.add(number)
#         print('The number was added to the set')
#         return True
#
#
# add_to_set(4, {2, 3, 5})


# # 11
# # Create a function that takes a month and returns how many days it has
# from calendar import monthrange
#
#
# def month_days(year, month):
#     return monthrange(year, month)[1]
#
#
# print(month_days(2023, 4))


# # 12
# # Create a function that takes two numbers and returns the addition, subtraction, multiplication and division at the same time
# #
# def calculator(num1, num2):
#     print(f'Addition: {num1} + {num2} =', (num1 + num2))
#     print(f'Subtraction: {num1} - {num2} =', (num1 - num2))
#     print(f'Multiplication: {num1} * {num2} =', (num1 * num2))
#     print(f'Division: {num1} / {num2} =', (num1 / num2))
#
#
# calculator(10, 2)


# # 13
# # Create a function that takes a list of digits (0-9) and returns a dictionary that displays how many of each digit there are
# import json
#
#
# def digit_count(*digits):
#     count = {}
#     for digit in digits:
#         if digit in count:
#             count[digit] += 1
#         else:
#             count[digit] = 1
#     return count
#
#
# print(json.dumps(digit_count(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0), indent=4))


# # 14
# # Create a function that takes 3 numbers and returns the maximum value that two of them can reach
# #
# def max_sum(num1, num2, num3):
#     return max(num1+num2, num2+num3, num1+num3)
#
#
# print(max_sum(2, 10, 43))


# # 15
# # Create a function that takes a number and returns the sum of all the numbers reaching that number from 0
# #
# def sum_to_n(n):
#     return sum(range(n+1))
#
#
# print(sum_to_n(3))


# # 16
# # Create a function that takes 2 lists of numbers and returns the numbers found in both
# #
# def common_numbers(list1, list2):
#     dup = []
#     for number in list1:
#         if number in list2 and number not in dup:
#             dup.append(number)
#     return dup
#
#
# lista1 = [1, 2, 3, 4, 5, 5, 6]
# lista2 = [4, 5, 6, 7, 8, 5, 6]
#
# duplicates = common_numbers(lista1, lista2)
# print(duplicates)


# # 17
# # Create a function that takes a price and a discount (1-100%) and displays the amount
# #
# def apply_discount(price, discount):
#     if discount <= 0 or discount >= 100:
#         return price
#     else:
#         reduced_price = price * (1 - discount / 100)
#         return round(reduced_price, 2)
#
#
# print(apply_discount(600, 45))


# # 18
# # Create a function that displays the current hour from Romania and China
# #
# import datetime
# import pytz
#
#
# def display_current_time():
#     timezone_ro = pytz.timezone('Europe/Bucharest')
#     now_ro = datetime.datetime.now(timezone_ro)
#     print(f'The date and current time in Romania: {now_ro.strftime("%Y-%m-%d %H:%M:%S")}')
#
#     timezone_cn = pytz.timezone('Asia/Shanghai')
#     now_cn = datetime.datetime.now(timezone_cn)
#     print(f'The date and current time in Chine: {now_cn.strftime("%Y-%m-%d %H:%M:%S")}')
#
#
# display_current_time()


# # 19
# # Create a function that returns how many days are left until Christmas
# #
# import datetime
#
#
# def days_until_xmas():
#     xmas_day = datetime.date(datetime.date.today().year, 12, 25)
#     today = datetime.date.today()
#     days_left = (xmas_day - today).days
#     return days_left
#
#
# print(days_until_xmas())

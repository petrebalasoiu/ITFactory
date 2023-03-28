# # 1
# # Create a 'Circle' class with 'colour' and 'radius' attributes and a constructor for each
# # Methods:
# # describe_circle() - prints the colour and radius
# # circle_area() - returns circle area
# # circle_diameter() - returns the circle diameter
# # circle_circumference() - returns the circle circumference
# #
# class Circle:
#     radius = 10
#     colour = 'Verde'
#
#     def __init__(self, radius, colour):
#         self.radius = radius
#         self.colour = colour
#
#     def describe_circle(self):
#         print(f'The circle\'s radius is: {self.radius} and it\'s colour is: {self.colour}')
#
#     def circle_area(self):
#         return 3.14 * (self.radius ** 2)
#
#     def circle_diameter(self):
#         return self.radius * 2
#
#     def circle_circumference(self):
#         return 2 * 3.14 * self.radius
#
#
# circle1 = Circle(15, 'Red')
# circle1.describe_circle()
# print('The circle\'s area is', circle1.circle_area())
# print('The circle\'s diameter is', circle1.circle_diameter())
# print('The circle\'s circumference is', round(circle1.circle_circumference(), 2))
# print('________________________________________________________________________________')
# circle2 = Circle(20, 'Blue')
# circle2.describe_circle()
# print('The circle\'s area is', circle2.circle_area())
# print('The circle\'s diameter is', circle2.circle_diameter())
# print('The circle\'s circumference is', round(circle2.circle_circumference(), 2))


# # 2
# # Create a 'Rectangle' class with 'length', 'width' and colour attributes and a constructor for each
# # Methods:
# # describe_rectangle() - prints the attributes
# # rectangle_area() - returns rectangle area
# # rectangle_perimeter() - returns rectangle perimeter
# # change_colour() - does not return, it only replaces the atribute with a parameter
# #
# class Rectangle:
#     length = 20
#     width = 10
#     colour = 'Mov'
#
#     def __init__(self, length, width, colour):
#         self.length = length
#         self.width = width
#         self.colour = colour
#
#     def describe_rectangle(self):
#         print(f'The current colour is {self.colour}')
#
#     def rectangle_area(self):
#         return self.length * self.width
#
#     def rectangle_perimeter(self):
#         return (self.length + self.width) * 2
#
#     def change_colour(self, new_colour):
#         self.colour = new_colour
#
#
# rectangle1 = Rectangle(24, 12, 'Red')
# rectangle1.describe_rectangle()
# print('The rectangle\'s area is', rectangle1.rectangle_area())
# print('The rectangle\'s perimeter is', rectangle1.rectangle_perimeter())
# rectangle1.change_colour('Green')
# rectangle1.describe_rectangle()
# print('________________________________________________________________________________')
# rectangle2 = Rectangle(34, 20, 'Blue')
# rectangle2.describe_rectangle()
# print('The rectangle\'s area is', rectangle2.rectangle_area())
# print('The rectangle\'s perimeter is', rectangle2.rectangle_perimeter())
# rectangle2.change_colour('Purple')
# rectangle2.describe_rectangle()


# # 3
# # Create an 'Employee' class with 'forename', 'surname' and 'salary' attributes and a constructor for each
# # Methods:
# # describe_employee() - prints the parameter that reflects the employee's department
# # full_name() - prints the employee's full name
# # monthly_salary() - prints the monthly salary
# # annual_salary() - calculates and prints the annual salary
# # salary_raise() - calculates and prints the salary raise per percentage
# #
# class Employee:
#     surname = 'Geo'
#     forename = 'Alex'
#     salary = 1500
#
#     def __init__(self, surname, forename, salary):
#         self.surname = surname
#         self.forename = forename
#         self.salary = salary
#
#     def describe_employee(self, department):
#         print('The employee\'s department is:', department)
#
#     def full_name(self):
#         print(f'The employee\'s full name is: {self.surname} {self.forename}.')
#
#     def monthly_salary(self):
#         print(f'The employee\'s monthly salary is {self.salary} USD/month.')
#
#     def annual_salary(self):
#         print(f'The emplyeee\'s annual salary is  {self.salary * 12} USD.')
#
#     def salary_raise(self, procent):
#         print(f'This employee\'s monthly salary has increased by: {round(procent / 100 * self.salary)} USD')
#
#
# employee1 = Employee('Popa', 'Ion', 3000)
# employee1.describe_employee('IT')
# employee1.full_name()
# employee1.monthly_salary()
# employee1.annual_salary()
# employee1.salary_raise(15)
# print('________________________________________________________________________________')
# employee2 = Employee('Nistor', 'Maria', 3500)
# employee2.describe_employee('HR')
# employee2.full_name()
# employee2.monthly_salary()
# employee2.annual_salary()
# employee2.salary_raise(10)


# # 4
# # Create an 'Account' class with 'IBAN', 'account holder', 'balance' attributes and a constructor for each
# # Methods:
# # display_balance() - Account holder 'x' has a current balance of 'y' USD
# # account_withdrawal() - withdrawals money and displays the remaining balance
# # account_deposit() - deposits money and displays the updated balance
# #
# class Account:
#     iban = 'BT'
#     account_holder = 'John Wayne'
#     balance = 2000
#
#     def __init__(self, iban, account_holder, balance):
#         self.iban = iban
#         self.account_holder = account_holder
#         self.balance = balance
#
#     def display_balance(self):
#         print(f'The holder {self.account_holder} of the account {self.iban} has a current balance of {self.balance} USD.')
#
#     def account_withdrawal(self, amount):
#         self.balance -= amount
#         print(f'The following amount {amount} has been withdrawal from the current account and the balance left is {self.balance} USD')
#
#     def account_deposit(self, amount):
#         self.balance += amount
#         print(f'The following amount {amount} has been deposited into the current account and the updated balance is {self.balance} USD')
#
#
# account1 = Account('RBS', 'Andrew Walker', 2000)
# account1.display_balance()
# account1.account_withdrawal(200)
# account1.account_deposit(500)
# print('________________________________________________________________________________')
# account2 = Account('RBS', 'Jane Walker', 2500)
# account2.display_balance()
# account2.account_withdrawal(500)
# account2.account_deposit(300)


# # 5
# # Create an 'Invoice' class with the following attributes: 'series' (constant), 'number', 'item_name', 'quantity', 'price_per_piece' with constructors for each except the series
# # Methods:
# # change_quantity(quantity) - changes the quantity
# # change_price(price) - changes the price
# # change_item_name(name) - changes the item's name
# # generate_invoice() - prints a table with the invoice
# #
# import TableIt
# from datetime import date
#
#
# class Invoice:
#     today = date.today().strftime('%d/%m/%Y')
#     series = 'ITF 2023'
#
#     def __init__(self, number, item_name, quantity, price_per_piece):
#         self.number = number
#         self.item_name = item_name
#         self.quantity = quantity
#         self.price_per_piece = price_per_piece
#
#     def change_quantity(self, quantity):
#         self.quantity = quantity
#         print(f'The quantity has changed to {quantity}')
#
#     def change_price(self, price):
#         self.price_per_piece = price
#         print(f'The price is now {price} USD')
#
#     def change_item_name(self, name):
#         self.item_name = name
#         print(f'The name of the item is {name}')
#
#     def generate_invoice(self):
#         invoice = Invoice
#         print(f'Invoice series: {invoice.series} \nNumber: {self.number}')
#         print(f'Date: {invoice.today}')
#         my_invoice = [
#             ['Item', 'Quantity', 'Price per piece', 'Total'],
#             [self.item_name, self.quantity, self.price_per_piece, self.quantity * self.price_per_piece],
#         ]
#         TableIt.printTable(my_invoice, useFieldNames=True)
#
#
# invoice1 = Invoice(1, 'PC', 8, 800)
# invoice1.change_quantity(9)
# invoice1.change_price(900)
# invoice1.change_item_name('Smartphone')
# invoice1.generate_invoice()
# print('________________________________________________________________________________')
# invoice2 = Invoice(2, 'Laptop', 10, 2500)
# invoice2.change_quantity(15)
# invoice2.change_price(2000)
# invoice2.change_item_name('Laptop Gaming')
# invoice2.generate_invoice()


# # 6
# # Create a 'Car' class with the following attributes: 'brand', 'model', 'max_speed', 'current_speed', 'colour', 'available_colours' (set), 'registered' (bool) with constructors only for 'brand' and 'max_speed'
# # Methods:
# # describe() - prints all attributes except 'available_colours'
# # registered() - changes the attribute to True
# # repaint() - changes the car's colour only if the paint is listed in the 'available_colours' otherwise it throws an error
# # accelerates() - accelerates to a certain speed - if the speed is negative it throws an error and if the speed is higher than the 'max_speed' it will accelerate to the max speed
# # break() - the car stops reaching 0 speed
# #
# class Car:
#     model = 'Dacia'
#     current_speed = 0
#     colour = 'grey'
#     available_colours = {'red', 'green', 'yellow', 'blue', 'purple'}
#     registered = False
#
#     def __init__(self, model, max_speed):
#         self.speed = None
#         self.model = model
#         self.max_speed = max_speed
#
#     def describe(self):
#         print(f'The car\'s model is {self.model}')
#         print(f'The current speed is {self.current_speed}')
#         print(f'The current colour is {self.colour}')
#         print(f'Is it registered? {self.registered}')
#
#     def register_car(self):
#         self.registered = True
#
#     def change_colour(self, colour):
#         self.colour = colour
#         if colour in self.available_colours:
#             self.colour = colour
#             print(f'The colour has been changed to {colour}')
#         else:
#             print('The chosen colour is not available')
#
#     def accelerates(self, speed):
#         self.speed = speed
#         if self.speed < 0:
#             print('The car cannot accelerate!')
#         elif self.speed > self.max_speed:
#             print(f'The car can only accelerate to {self.max_speed}')
#         else:
#             print(f'The car accelerates to {self.speed} km/h')
#
#     def hits_break(self):
#         self.speed = 0
#         print(f'The car has stopped and its current speed is now {self.speed} km/h')
#
#
# car1 = Car('Logan', 200)
# car1.describe()
# car1.register_car()
# car1.change_colour('rosu')
# car1.accelerates(150)
# car1.hits_break()


# # 7
# # Create a 'TodoList' class with a to.do attribute that is a dictionary with the key being the task's name and the value is the description.
# # At first there are no tasks so the dictionary is empty, and we don't need constructors
# # Methods:
# # add_task(name, description) - will be added to the dictionary
# # finish_task(name) - will be removed from the dictionary
# # display_more_info(task_name) - more info on certain task
# # # If the task is not in the list it asks the user if they want to add it
# # # If they decline it says 'Goodbye'
# # # If they accept it asks the user for the task details, and it saves the entry in the dictionary
# #
# import json
#
#
# class ToDoList:
#     todo = {}
#
#     def add_task(self, name, description):
#         self.name = name
#         self.description = description
#         self.todo[name] = description
#
#     def display_complete_list(self):
#         print(json.dumps(self.todo, indent=4))
#
#     def finish_task(self, name):
#         self.name = name
#         self.todo.pop(name)
#         print(json.dumps(self.todo, indent=4))
#
#     def display_task_only(self):
#         for keys, value in self.todo.items():
#             print(keys)
#
#     def display_more_info(self, task_name):
#         self.task_name = task_name
#         if task_name not in self.todo:
#             answer = input('The task is not in the ToDo list. Would you like to add it? \n')
#             if answer == 'no':
#                 print('Goodbye')
#             elif answer == 'yes':
#                 task_details = input('Please add a description: \n')
#                 self.todo[task_name] = task_details
#                 print(json.dumps(self.todo, indent=4))
#         else:
#             print('The task is already in the list')
#
#
# list1 = ToDoList()
# list1.add_task('Wash dishes', 'With plenty of detergent')
# list1.add_task('Run', 'five miles')
# list1.display_complete_list()
# list1.display_task_only()
# list1.display_more_info('Run')
# list1.finish_task('Wash dishes')
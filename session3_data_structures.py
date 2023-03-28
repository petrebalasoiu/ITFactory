# # 1
# # Declare a list musical_notes which includes the notes from do to do
# # a. Print it
# # b. Reverse the order using slicing and overwrite it then print the reversed version
# # c. Use a method to reverse the order to its original state
# #
# musical_notes = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(musical_notes)
# musical_notes = musical_notes[::-1]
# print(musical_notes)
# musical_notes.reverse()
# print(musical_notes)


# # 2
# # Print how many times the 'do' note appears in the list
# #
# print(musical_notes.count('do'))


# # 3
# # Having 2 lists, [3, 1, 0, 2] and [6, 5, 4], find 2 ways to merge them into one list
# #
# x = [3, 1, 0, 2]
# y = [6, 5, 4]
# z = x + y
# print(z)
# x.extend(y)
# print(x)


# # 4
# # Sort and print the list from the previous exercise. Remove the number 0 from the list using a function then print the list again
# #
# z = [3, 1, 0, 2, 6, 5, 4]
# z.sort()
# z.pop(0)
# print(z)


# # 5
# # Using an if statement, verify if the list generated at the exercise 3 is either empty or not
# #
# z = [3, 1, 0, 2, 6, 5, 4]
# if len(z) == 0:
#     print('The list is empty')
# else:
#     print('The list is not empty')


# # 6
# # Use a function to completely empty the list generated at the exercise 3
# #
# z = [3, 1, 0, 2, 6, 5, 4]
# z.clear()
# print(z)


# # 7
# # Reuse the code in the exercise 5 to verify again the result. Now it should print that the list is empty
# #
# z = [3, 1, 0, 2, 6, 5, 4]
# z.clear()
# if len(z) == 0:
#     print('The list is empty')
# else:
#     print('The list is not empty')


# # 8
# # Having the following dictionary dict1 = {'Mary' : 8, 'Andrew' : 10, 'John' : 5}, use a function to display the students (the Keys)
# dict1 = {
#     'Mary': 8,
#     'Andrew': 10,
#     'John': 5
# }
# print(dict1.keys())


# # 9
# # Print the students mentioned in the list above and their grades
# # i.e.: 'Mary received the grade: {x}'
# #
# dict1 = {
#     'Mary': 8,
#     'Andrew': 10,
#     'John': 5
# }
# x = dict1['Mary']
# y = dict1['Andrew']
# z = dict1['John']
# print(f'Mary received the grade: {x}')
# print(f'Andrew received the grade: {y}')
# print(f'John received the grade: {z}')


# # 10
# # John's grade was given in error, and he actually received a 6
# # Modify his grade and then print the new one
# #
# dict1 = {
#     'Mary': 8,
#     'Andrew': 10,
#     'John': 5
# }
# dict1.update({'John': 6})
# print(dict1['John'])


# # 11
# # John is then transferred to a different classroom
# # - Use a function to remove him from the dictionary
# # - A new student is transferred in John's palce, with the grade 9
# # - Print the updated dictionary that includes the new student
# #
# dict1 = {
#     'Mary': 8,
#     'Andrew': 10,
#     'John': 6
# }
# del dict1['John']
# dict1.update({'Mark': 9})
# print(dict1)


# # 12
# # There are 2 sets:
# # week_days = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
# # weekend = {'Saturday', 'Sunday'}
# # Try to add 'Monday' to the week_days set and see what happens
# # Print the week_days set and observe the behaviour
# #
# week_days = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
# week_days.add('Monday')
# print(week_days)
# # 'Monday' was not added because sets to not allow duplicates


# # 13
# # Use an if statement to verify if the weekend set is a subset of the week_days set or not
# #
# week_days = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
# weekend = {'Saturday', 'Sunday'}
# if weekend.issubset(week_days):
#     print(True)
# else:
#     print(False)


# # 14
# # Display the differences between these two sets (the elements that are in one set but not in the other and viceversa)
# #
# week_days = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
# weekend = {'Saturday', 'Sunday'}
# diff1 = week_days - weekend
# diff2 = weekend - week_days
# print(f'{diff1} are not in the weekend set')
# print(f'{diff2} is empty because the elements found in the weekend set can be also found in week_days set')


# # 15
# # Display the similarities between these two sets (the elements that can be found in both sets)
# #
# week_days = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
# weekend = {'Saturday', 'Sunday'}
# print(week_days.intersection(weekend))


# # 16
# # Imagine a sports team during a game. Only 3 changes are allowed.
# # - declare a list with 5 players on the field
# # - declare a list with 5 players on the bench
# # - declare an empy list which will collect the players removed from the field
# # - declare a variable for the changes made (can be any value since you will update it for every run)
# # - MAX_CHANGES will be a constant with a value of 3
# #
# # If the player X is on the field and there are enough changes left:
# # 	- The replacement takes place if the player Y is on the bench and cannot be found on the field
# # 	- Player X will then be removed from the field and added to the players' removed list
# # 	- Player Y will then be added on the field and removed from the bench
# # 	- The program prints: "X was replaced by Y on the field. There are N changes left"
# # Else if the player we want to replace is not on the field:
# # 	- The program prints: "the replacement cannot take place because X is not on the field"
# # Else, the program prints: "no more changes left"
# #
# #
# players_on_the_field = ['John', 'Tony', 'Alex', 'Greg', 'Bob']
# players_on_the_bench = ['Kevin', 'Frank', 'Will', 'Ryan', 'Joe']
# players_removed = []
# changes_made = 1
# MAX_CHANGES = 3
#
# removed_player = input('Choose a player to replace: \n')
# added_player = input('Choose a player from the bench: \n')
# changes_left = MAX_CHANGES - changes_made
#
# if removed_player in players_on_the_field and added_player in players_on_the_bench and changes_made <= MAX_CHANGES:
#     players_on_the_field.remove(removed_player)
#     players_on_the_bench.remove(added_player)
#     players_removed.append(removed_player)
#     players_on_the_field.append(added_player)
#
#     print(f'{added_player} has replaced {removed_player} on the field. There are {changes_left} changes left.')
#     print(f'Current players on the field: {players_on_the_field}')
#     print(f'Current players on the bench: {players_on_the_bench}')
#     print(f'Current players removed: {players_removed}')
#
# elif removed_player not in players_on_the_field and added_player not in players_on_the_bench:
#     print(f'The change cannot be fulfilled because the player [{removed_player}] is not on the field and player [{added_player}] is not on the bench')
# elif removed_player not in players_on_the_field:
#     print(f'The change cannot be fulfilled because the player {removed_player} is not on the field.')
# elif added_player not in players_on_the_bench:
#     print(f'The change cannot be fulfilled because the player {added_player} is not on the bench.')
# else:
#     print(f'There are no more changes available.')

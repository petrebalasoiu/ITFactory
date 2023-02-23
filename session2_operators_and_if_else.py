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
x = input('x = ')
if len(x) <= 4:
    print('The number has less than or 4 digits')
else:
    print('The number has more than 4 digits')


# # 12
# # Verifica daca x are exact 6 cifre
# x = input('Numar: ')
# if len(x) == 6:
#     print('ARE 6 cifre')
# else:
#     print('NU are 6 cifre')
#
# # 3 (optional)
# # Verifica daca x este numar par sau impar
# x = int(input('Numar: '))
# if x % 2 == 0:
#     print('par')
# else:
#     print('impar')
#
# # 4 (optional)
# # Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre ele
# x = int(input('x = '))
# y = int(input('y = '))
# z = int(input('z = '))
# if x > y and x > z:
#     print(f'dintre {x, y, z} cel mai mare numar este {x}')
# elif y > z:
#     print(f'dintre {x, y, z} cel mai mare numar este {y}')
# else:
#     print(f'dintre {x, y, z} cel mai mare numar este {z}')
#
# # 5 (optional)
# # Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca triunghiul este valid sau nu (un triunghi este valid daca suma tuturor unghiurilor este de 180 de grade sau daca suma lungimilor a oricare doua laturi este mai mare decat lungimea celei de-a treia laturi)
# a + b + c = 180 or a + b > c / a + c > b / b + c > a
# x = int(input('x = '))
# y = int(input('y = '))
# z = int(input('z = '))
# if x + y + z == 180:
#     print('Triunghi valid')
# elif x > z and y > z:
#     print('Triunghi valid')
# else:
#     print('Triunghi invalid')
#
# # 6 (optional)
# # Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de la tastatura un număr x de tip int și afișează stringul fără ultimele x caractere. ex: dacă ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the smarte'
# x = int(input('Cate caractere vrei sa scazi?: '))
# str = 'Coral is either the stupidest animal or the smartest rock'
# print(str[0:-x])
#
# # 7 (optional)
# # Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format din primele 5 caractere + ultimele 5
# x = 'Coral is either the stupidest animal or the smartest rock'
# y = x[0:5] + x[-5:]
# print(y)
#
# # 8 (optional)
# # Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza indexul de start al cuvântului rock - adică poziția in string la care începe cuvântul rock (hint: este o funcție care te ajuta sa faci asta). Folosind aceasta variabila + slicing, afișează tot stringul pana la acest cuvant. Output asteptat: 'Coral is either the stupidest animal or the smartest '
# x = 'Coral is either the stupidest animal or the smartest rock'
# y = len(x) - 4
# z = x[y:]
# print(x[:y])
#
# # 9 (optional)
# # Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se va folosi un assert. Atentie: se dorește ca programul sa fie case insensitive, adica 'apA' e acceptat ca un string in care primul si ultimul caracter este la fel (hint, te poti folosi de o functie pentru a face string-ul case insensitive)
# x = input('Scrie un cuvant: ').upper()
# assert x[0] == x[-1]
# print('corect')
#
# # 10 (optional)
# # Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare (hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)
# x = '0123456789'
# print(x[2::2], x[1::2])
# ______sau______ (limiteaza pana la 10 caractere, din 2 in 2)
# stringul = '0123456789'
# print(stringul[2:10:2])
# print(stringul[1:10:2])
#
#
# # 1 (bonus)
# # 1. Daca pers are varsta peste 18 ani si are pasaport
# # 2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
# # 3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la celalat parinte
# a = int(input('Varsta: '))
# b = input('Insotit de mama? (da/nu) ')
# c = input('Insotit de tata? (da/nu) ')
# d = input('Pasaport (da/nu) ')
# e = input('Act permisiune mama? (da/nu) ')
# f = input('Act permisiune tata? (da/nu) ')
# if a >= 18 and d.lower() == 'da':
#     print(f'Varsta {a} ani, am pasaport => Ma pot imbarca')
# elif a < 18 and d.lower() == 'da' and c.lower() == 'da' and b.lower() == 'da':
#     print(f'Varsta {a} ani, am pasaport, ambii parinti, fara acte de permisiune => Ma pot imbarca')
# elif a < 18 and d.lower() == 'da' and (b.lower() == 'da' or e.lower() == 'da') and (c.lower() == 'da' or f.lower() == 'da'):
#     print(f'Varsta {a} ani, am pasaport, cel putin un parinte si un actul de permisune al celuilalt => Ma pot imbarca')
# else:
#     print('Nu ma pot imbarca fie din lipsa pasaportului, a unui parinte sau a unui act de permisiune in cazul in care sunt minor/a')
#
# sau_________________________________________(fara .lower() si inversat al elif)
#
# a = int(input('Varsta: '))
# b = input('Insotit de mama? (da/nu) ')
# c = input('Insotit de tata? (da/nu) ')
# d = input('Pasaport (da/nu) ')
# e = input('Act permisiune mama? (da/nu) ')
# f = input('Act permisiune tata? (da/nu) ')
# if a >= 18 and d == 'da':
#     print(f'Varsta {a} ani, am pasaport => Ma pot imbarca')
# elif a < 18 and d == 'da' and c == 'da' and b == 'da':
#     print(f'Varsta {a} ani, am pasaport, ambii parinti, fara acte de permisiune => Ma pot imbarca')
# elif a < 18 and d == 'da' and (b == 'da' and f == 'da') or (c == 'da' and e == 'da'):
#     print(f'Varsta {a} ani, am pasaport, cel putin un parinte si actul de permisune al celuilalt => Ma pot imbarca')
# else:
#     print('Nu ma pot imbarca fie din lipsa pasaportului, a unui parinte sau a unui act de permisiune in cazul in care sunt minor/a')
#
#
# # 2 (bonus)
# # Joc de noroc
# import random
# dice_roll = (random.randint(1, 6))
# x = int(input('Alege un numar: '))
# if x == dice_roll:
#     print(f'Ai ghicit! Felicitari! Ai ales {x} si zarul a fost {dice_roll}')
# elif x > dice_roll:
#     print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {x} dar a fost {dice_roll}')
# else:
#     print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {x} dar a fost {dice_roll}')
#
# sau_________________________________________(cu limitare intre 1 si 6 numere la input)
#
# import random
# dice_roll = (random.randint(1, 6))
# x = int(input('Alege un numar: '))
# if x == dice_roll:
#     print(f'Ai ghicit! Felicitari! Ai ales {x} si zarul a fost {dice_roll}')
# elif x > dice_roll and x <= 6:
#     print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {x} dar a fost {dice_roll}')
# elif x < dice_roll and x <= 6:
#     print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {x} dar a fost {dice_roll}')
# else:
#     print('Alege doar numere intre 1 si 6')


















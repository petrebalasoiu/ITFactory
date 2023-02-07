# # 1
# # Briefly explain in your own words how does an if/else statement work.
# # An if/else statement runs a certain part of the code if the condition is True or a separate part of the code if the condition is False.
#########
# # 2
# # Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural daca este numar intreg mai mare ca 0)
# x = int(input('Introdu numar: '))
# if x >= 0:
#     print('Numarul este natural')
# else:
#     print('Numarul nu este natural')
#
# # 3
# # Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
# x = int(input('Introdu numar: '))
# if x < 0:
#     print('negativ')
# elif x == 0:
#     print('neutru')
# else:
#     print('pozitiv')
#
# # 4
# # Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).
# x = int(input('Introdu numar: '))
# if x in range(-2, 14):
#     print('Se afla in numerotare')
# else:
#     print('Nu se afla in numerotare')
# ______sau______
# x = int(input('Introdu numar: '))
# if x >= -2 and x <= 13:
#     print('Se afla in numerotare')
# else:
#     print('Nu se afla in numerotare')
#
# # 5
# # Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia abs()
# x = int(input())
# y = int(input())
# if abs(x) - abs(y) <= 5:
#     print('diferenta este 5 sau mai mica')
# else:
#     print('diferenta este mai mare')
#
# # 6
# # Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
# x = int(input('Insert number: '))
# if x not in range(5, 28):
#     print(x, 'nu este in interval')
# else:
#     print(x, 'se afla in interval')
# ______sau______
# x = int(input('Introdu numar: '))
# if not (x >= 5 and x <= 27):
#     print(x, 'nu este in interval')
# else:
#     print(x, 'se afla in interval')
#
# # 7
# # Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale, daca nu, afiseaza care din ele este mai mare
# x = int(input('x = '))
# if not (x >= 5 and x <= 27):
#     print(x, 'nu este in interval')
# else:
#     print(x, 'se afla in interval')
# y = int(input('y = '))
# if x == y:
#     print('sunt egale')
# elif x > y:
#     print(f'{x} este mai mare')
# else:
#     print(f'{y} este mai mare')
#
# # 8
# # Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau oarecare (nicio latura nu e egala).
# x = int(input('Latura x: '))
# y = int(input('Latura y: '))
# z = int(input('Latura z: '))
# if x == y == z:
#     print('Echilateral')
# elif x != y != z:
#     print('Oarecare')
# else:
#     print('Isoscel')
#
# # 9
# # Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie! Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.
# x = str(input('Introdu litera: '))
# if x == 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U':
#     print('vocala')
# else:
#     print('consoana')
# ______sau______
# x = str(input('Introdu litera: ')).lower()
# if x == 'a' or 'e' or 'i' or 'o':
#     print('vocala')
# else:
#     print('consoana')
#
# # 10
# # Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza:
# # Peste 9 => A
# # b. Peste 8 => B
# # c. Peste 7 => C
# # d. Peste 6 => D
# # e. Peste 4 => E
# # f. 4 sau sub => F
# x = int(input('Introdu cifra: '))
# if x <= 4:
#     print('F')
# elif x == 5:
#     print('E')
# elif x == 6:
#     print('D')
# elif x == 7:
#     print('C')
# elif x == 8:
#     print('B')
# elif x <= 10:
#     print('A')
# else:
#     print('Numar prea mare')
#
# # 1 (optional)
# # Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
# x = input('Numar: ')
# if len(x) <= 4:
#     print(x, 'are pana in 4 cifre')
# else:
#     print(x, 'are mai mult de 4 cifre')
#
# # 2 (optional)
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


















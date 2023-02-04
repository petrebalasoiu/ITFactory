# # 1
# # In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila
# # O variabila este un spatiu de stocare (in memorie) pe care il putem eticheta (initializa) si in care putem adauga diverse tipuri de date (sau sa-i dam valori)
#
# # 2
# # Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri:
# # string, int, float, bool
# #  Valorile le alegeti voi dupa preferinte
# concurent = "Horia"
# varsta = 36
# scor = 8.6
# medalie = True
#
# # 3
# # Utilizat functia type pentru a verifica daca au tipul de date asteptat
# print(type(concurent))
# print(type(varsta))
# print(type(scor))
# print(type(medalie))
# sau:
# print(type(concurent), type(varsta), type(scor), type(medalie))
#
# # 4
# # Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
# # Verificati tipul acesteia
# scor = round(scor)
# print(type(scor))
#
# # 5
# # folositi print() si printati in consola 4 propozitii folosind cele 4 variabile.
# # (rezolvati nepotrivirile de tip prin ce modalitate doriti)
# print(f'Numele concurentului de astazi este {concurent}.')
# print(f'El are varsta de {varsta} de ani.')
# print(f'Scorul lui pana in prezent este de {scor} din 10.')
# print(f'Anul trecut a castigat o medalie de aur? {medalie}!')
#
# # 6
# # citeste de la tastatura numele
# # citeste de la tastatura prenumele
# # afiseaza 'Numele complet are x caractere'
# nume = input('Introduceti numele:\n')
# prenume = input('Introduceti prenumele:\n')
# print(f'Numele complet are {len(nume) + len(prenume)} caractere.')
# sau
# numar_caractere = len(nume) + len(prenume)
# print(f'Numele complet are {numar_caractere} caractere.')
#
# # 7
# # citeste de la tastatura lungimea
# # citeste de la tastatura latimea
# # afiseaza 'Aria dreptunghiului este x'
# lungimea = int(input('Lungimea: '))
# latimea = int(input('Latimea: '))
# print(f'Aria triunghiului este de {lungimea * latimea} cm.')
# sau
# aria_triunghiului = lungimea * latimea
# print(f'Aria triunghiului este de {aria_triunghiului} cm.')
#
# # 8
# # Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
# # afisati de cate ori apare cuvantul 'the'
# sentence = 'Coral is either the stupidest animal or the smartest rock'
# print(sentence.count('the'))
#
# # 9
# # acelasi string
# # inlocuieste the cu THE peste tot
# # printeaza rezultatul
# sentence = 'Coral is either THE stupidest animal or THE smartest rock'
# print(sentence.replace("the", "THE"))
#
# # 10
# # acelasi string de mai sus
# # folositi un assert ca sa verificati daca acest string contine doar numere
# sentence = 'Coral is either the stupidest animal or the smartest rock'
# assert sentence == int(sentence)
# print('Contine numere')
#
# # 1 (optional)
# # citeste de la tastatura un string de dimensiune impara
# # afiseaza caracterul din mijloc
# # ___Rezolvare A___:
# # paranteze = {x[(len(x)//2)]}
# # {} - reprezinta "integrarea" cu f'{}'
# # [] - reprezinta indexul din input pe care vreau sa il afisez
# # () - reprezinta integrarea functiei len() in indexul care vrem sa il afisam x[(len(x))]
# x = input('Introdu string: \n')
# print(f'Caracterul din mijloc este: {x[(len(x) // 2)]}')
# # optional:
# y = len(x)
# print(f'Sirul are {y} caractere')
# mijloc = y / 2
# print(f'Mijlocul sirului reprezinta {mijloc}')
# mijloc2 = int(mijloc)
# print(f'Partea intreaga din caracterul din mijloc reprezinta {mijloc2}')
# print(f'Caracterul din mijloc este: {x[mijloc2]}')
#
# # ___Rezolvare B___:
# input_string = str(input('Insert string with odd character length: '))
# length_string = len(input_string)
# if length_string % 2 != 0:
#     divide_string = length_string // 2
#     print('The middle character is:', input_string[divide_string])
# else:
#     print('Only strings with odd character length are accepted! Rerun script!')
#
# # 2 (optional)
# # Folosind assert, verificati daca un string este palindrom
# # ___Assert method___
# string = input('Enter string: \n')
# assert string == string[::-1]
# print('Yes it is!')
# #
# # ___if/else method___
# string = input("Enter string: \n")
# if string == string[::-1]:
#     print(Yes it is!')
# else:
#     print('No, it is not!')
#
# # 3 (optional)
# # folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
# # si salveaza fiecare cuvant intr-o variabila
# # acum printeaza ambele variabile pentru verificare
# user_input = str(input('Baga aici: '))
# separate = user_input.split(' ')
# var1 = separate[0]
# var2 = separate[1]
# print(var1)
# print(var2)
# # sau
# x = str(input('Baga aici bossule: '))
# y, z = x.split()
# print(f"Primul cuvant este '{y}'.")
# print(f"Al doilea cuvant este '{z}'.")
#
# # 4 (optional)
# # citeste un string de la tastatura (eg: alabala portocala)
# # salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite)
# # capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
# # => alAbAlA portocAla
# str = input('Citeste un string de la tastatura: ')
# char_top = str[0]
# char_bot = str[-1]
# char_mid = str[1:-1]
# print(char_top)
# print(char_bot)
# print(char_mid)
# print(f'Stringul modificat este {char_top}{char_mid.upper()}{char_bot}')
# print(f'Stringul modificat este {char_top}{char_mid.replace(char_top, char_top.upper())}{char_bot}')  # fara count
# print(f'Stringul modificat este {char_top}{char_mid.replace(char_top, char_top.upper(), 2)}{char_bot}')  # folosind count
#
# # 5 (optional)
# # citeste un user de la tastatura
# # citeste o parola
# # afiseaza: 'Parola pt user x este ***** si are x caractere'
# # ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
# # eg: parola abc => ***
# # parola abcd => ****
# x = input('ia user')
# y = input('ia parola')
# print(f'Parola pt user {x} este {len(y) * "*"} si are {len(y)} caractere.')
# sau
# stars = len(y) * '*'
# show = print(f'Parola pt user {x} este {stars} si are {len(y)} caractere.')









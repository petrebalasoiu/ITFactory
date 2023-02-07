# # 1
# # Declara o lista note_muzicale in care sa pui do re mi etc pana la do
# # a. Afiseaz-o
# # b. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza varianta actuala (inversata)
# # c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii inverseze ordinea (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face asta automat) si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la varianta inițială
# # Concluzii: slicing e temporar, dacă vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi intr-o listă nouă. Metoda gasita de tine face suprascrierea automat și permanentizeaza aceste modificări. Ambele variante își găsesc utilitatea în funcție de ce ne dorim in acel moment.
# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(note_muzicale)
# note_muzicale = note_muzicale[::-1]
# print(note_muzicale)
# note_muzicale.reverse()
# print(note_muzicale)
#
# # 2
# # Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.
# print(note_muzicale.count('do'))
#
# # 3
# # Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante sa le unesti intr-o singura lista.
# x = [3, 1, 0, 2]
# y = [6, 5, 4]
# z = x + y
# print(z)
# x.extend(y)
# print(x)
#
# # 4
# # Sorteaza si afiseaza lista generata la exercitiul anterior. Sterge numarul 0 din lista folosind o functie si apoi afiseaza din nou lista
# z = [3, 1, 0, 2, 6, 5, 4]
# z.sort()
# z.pop(0)
# print(z)
#
# # 5
# # Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura urmatoarele:
# # - Lista este goala (IF)
# # - Lista nu este goala (ELSE)
# z = [3, 1, 0, 2, 6, 5, 4]
# if len(z) == 0:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')
#
# # 6
# # Foloseste o functie care sa goleasca lista de la exercitiul 3
# z = [3, 1, 0, 2, 6, 5, 4]
# z.clear()
# print(z)
#
# # 7
# # Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se afiseze ca lista e goala
# z = [3, 1, 0, 2, 6, 5, 4]
# z.clear()
# if len(z) == 0:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')
#
# # 8
# # Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, foloseste o functie ca sa afisezi Elevii (cheile)
# dict1 = {
#     'Ana': 8,
#     'Gigel': 10,
#     'Dorel': 5
# }
# print(dict1.keys())
#
# # 9
# # Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
# # Ex: ‘Ana a luat nota {x}’.
# # Doar nota o vei lua folosindu-te de cheie
# dict1 = {
#     'Ana': 8,
#     'Gigel': 10,
#     'Dorel': 5
# }
# x = dict1['Ana']
# y = dict1['Gigel']
# z = dict1['Dorel']
# print(f'Ana a luat nota {x}.')
# print(f'Gigel a luat nota {y}.')
# print(f'Dorel a luat nota {z}.')
#
# # 10
# # Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
# # - Modifica nota lui Dorel in 6
# # - Printeaza nota lui dupa modificare
# dict1 = {
#     'Ana': 8,
#     'Gigel': 10,
#     'Dorel': 5
# }
# dict1.update({'Dorel': 6})
# print(dict1['Dorel'])
#
# # 11
# # Imagineaza-ti ca Gigel se transfera din clasa.
# # - Cauta o functie care sa il stearga
# # - Vine un coleg nou. Adaugati-l in lista pe Ionica, cu nota 9
# # - Printati dictionarul cu noii elevi
# dict1 = {
#     'Ana': 8,
#     'Gigel': 10,
#     'Dorel': 5
# }
# del dict1['Gigel']
# dict1.update({'Ionel': 9})
# print(dict1)
#
# # 12
# # Ai urmatoarele seturi:
# # zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# # weekend = {'sambata', 'duminica'}
# # - Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
# # - Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# zile_sapt.add('luni')
# print(zile_sapt)
# # string-ul 'luni' nu a fost adaugat doarece set-urile nu accepta duplicate
#
# # 13
# # Foloseste un if si verifica daca:
# # - Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se regasesc intre elementele din setul zile_sapt)
# # - Weekend nu este un subset al zilelor din sapt
# # Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. Rezultatul fiecarui punct de mai sus va fi un boolean
# zile_sapt = {'sambata', 'duminica',}
# weekend = {'sambata', 'duminica'}
# if weekend < zile_sapt: # de ce operatorul asta?
#     print(True)
# else:
#     print(False)
# if weekend.issubset(zile_sapt):
#     print(True)
# else:
#     print(False)
#
# # 14
# # Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu sunt in weekend si invers)
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# x = zile_sapt - weekend
# y = weekend - zile_sapt
# print(x)
# print(y)
#
# # 15
# # Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in ambele seturi). Hint: Va puteti folosi de o functie
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# print(zile_sapt.intersection(weekend))
#
# # 1 (optional)
# #
# lista_jucatori_teren = ['Marius', 'Adi', 'Dan', 'Alex', 'Bubu']
# lista_jucatori_rezerva = ['Vlad', 'Gigi', 'Mihai', 'Dorin', 'Alin']
# lista_jucatori_scosi = []
# schimbari_efectuate = 1
# SCHIMBARI_MAX = 3
#
# x = str(input('Iese de pe teren: \n'))
# y = str(input('Intra pe teren: \n'))
# z = SCHIMBARI_MAX - schimbari_efectuate
#
# if x in lista_jucatori_teren and y in lista_jucatori_rezerva and schimbari_efectuate <= SCHIMBARI_MAX:
#     lista_jucatori_teren.remove(x)
#     lista_jucatori_rezerva.remove(y)
#     lista_jucatori_scosi.append(x)
#     lista_jucatori_teren.append(y)
#
#     print(f'A intrat {y}, a iesit {x}, mai aveti {z} schimari.')
#     print(f'Jucatori pe teren: {lista_jucatori_teren}')
#     print(f'Jucatori in rezerva: {lista_jucatori_rezerva}')
#     print(f'Jucatori scosi: {lista_jucatori_scosi}')
#
# elif x not in lista_jucatori_teren:
#     print(f'Nu se poate efectua schimbarea deoarece jucatorul {x} nu este pe teren.')
#
# elif y not in lista_jucatori_rezerva:
#     print(f'Nu se poate efectua schimbarea deoarece jucatorul {y} nu este rezerva.')
#
# else:
#     print(f'Limita de schimari a fost atinsa')

#_______________________________________________________________________________________________________

# Tentativa de For loop cu BUG
#
# lista_jucatori_teren = ['Marius', 'Adi', 'Dan', 'Alex', 'Bubu']
# lista_jucatori_rezerva = ['Vlad', 'Gigi', 'Mihai', 'Dorin', 'Alin']
# lista_jucatori_scosi = []
# schimbari_efectuate = 0
# SCHIMBARI_MAX = 3
#
# for i in range(3):
#     x = str(input('Iese de pe teren: \n'))
#     y = str(input('Intra pe teren: \n'))
#
#     schimbari_efectuate +=1
#     z = SCHIMBARI_MAX - schimbari_efectuate
#
#     if x in lista_jucatori_teren and y in lista_jucatori_rezerva and schimbari_efectuate <= SCHIMBARI_MAX:
#         lista_jucatori_teren.remove(x)
#         lista_jucatori_rezerva.remove(y)
#         lista_jucatori_scosi.append(x)
#         lista_jucatori_teren.append(y)
#
#         print(f'A intrat {y}, a iesit {x}, mai aveti {z} schimari.')
#         print(f'Jucatori pe teren: {lista_jucatori_teren}')
#         print(f'Jucatori in rezerva: {lista_jucatori_rezerva}')
#         print(f'Jucatori scosi: {lista_jucatori_scosi}')
#
#     elif x not in lista_jucatori_teren:
#         print(f'Nu se poate efectua schimbarea deoarece jucatorul {x} nu este pe teren.')
#
#     elif y not in lista_jucatori_rezerva:
#         print(f'Nu se poate efectua schimbarea deoarece jucatorul {y} nu este rezerva.')
#
#     else:
#         print(f'Limita de schimari a fost atinsa')

#_______________________________________________________________________________________________________

# Corectare cu While loop fara BUG

# lista_jucatori_teren = ['Marius', 'Adi', 'Dan', 'Alex', 'Bubu']
# lista_jucatori_rezerva = ['Vlad', 'Gigi', 'Mihai', 'Dorin', 'Alin']
# lista_jucatori_scosi = []
# schimbari_efectuate = 0
# SCHIMBARI_MAX = 3
#
# while len(lista_jucatori_scosi) < 3:
#     x = str(input('Iese de pe teren: \n'))
#     y = str(input('Intra pe teren: \n'))
#
#     if x in lista_jucatori_teren and y in lista_jucatori_rezerva:
#         lista_jucatori_teren.remove(x)
#         lista_jucatori_rezerva.remove(y)
#         lista_jucatori_scosi.append(x)
#         lista_jucatori_teren.append(y)
#
#         schimbari_efectuate += 1
#         z = SCHIMBARI_MAX - schimbari_efectuate
#
#         print(f'A intrat [{y}], a iesit [{x}], mai aveti [{z}] schimari.')
#         print(f'Jucatori pe teren: {lista_jucatori_teren}')
#         print(f'Jucatori in rezerva: {lista_jucatori_rezerva}')
#         print(f'Jucatori scosi: {lista_jucatori_scosi}')
#
#     elif x not in lista_jucatori_teren and y not in lista_jucatori_rezerva:
#         print(f'Nu se poate efectua schimbarea deoarece jucatorul [{x}] nu este pe teren,\nsi nici jucatorul [{y}] nu este rezerva.')
#
#     elif x not in lista_jucatori_teren:
#         print(f'Nu se poate efectua schimbarea deoarece jucatorul [{x}] nu este pe teren.')
#
#     elif y not in lista_jucatori_rezerva:
#         print(f'Nu se poate efectua schimbarea deoarece jucatorul [{y}] nu este rezerva.')
#
#     else:
#         print(f'Limita de schimari a fost atinsa')
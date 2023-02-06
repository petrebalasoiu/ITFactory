# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# # 1
# # Folosește un for că să iterezi prin toată lista și să afișezi: ‘Mașina mea preferată este x’
# for i in range(len(masini)):
#     print(f'Masina mea preferata este {masini[i]}')
# # Folosește un for each că să iterezi prin toată lista și să afișezi: ‘Mașina mea preferată este x’
# for masina in masini:
#     print(f'Masina mea preferata este {masina}')
# # Folosește un while că să iterezi prin toată lista și să afișezi: ‘Mașina mea preferată este x’
# i = 0
# while i < len(masini):
#     print(f'Masina mea preferata este {masini[i]}')
#     i += 1

# # 2 - Aceeasi lista
# # Folosește un for else
# # În for: Modifică elementele din listă astfel încât să fie scrie cu majuscule, exceptând primul și ultimul.
# # În else: Printează lista.
# new_list = []
# for masina in masini[1:-1]:
#     masina = masina.upper()
#     new_list.append(masina)
# else:
#     print(new_list)

# # 3 - Aceeasi lista
# # Vine un cumpărător care dorește să cumpere un Mercedes.
# # Itereaza prin ea prin modalitatea aleasă de tine.
# # Dacă mașina e mercedes:
# # - Printează ‘am găsit mașina dorită de dvs’
# # - Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# # Altfel:
# # - Printează ‘Am găsit mașina X. Mai căutam‘
# for masina in masini:
#     if masina == 'Mercedes':
#         print('Am gasit masina dorita de dumneavoastra.')
#         break
#     else:
#         print(f'Am gasit masina {masina}. Mai cautam')

# # 4 - Aceeasi lista
# # Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
# # - Dacă mașina e Trabant sau Lăstun:
# # Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
# # Printează S-ar putea să vă placă mașina x.
# for masina in masini:
#     if masina == 'Trabant' or masina == 'Lastun':
#         continue
#     print(f'S-ar putea sa va placa masina {masina}.')

# # 5 - Modernizeaza parcul de masini
# # ● Creaza o listă goală, masini_vechi.
# # ● Itereaza prin mașini.
# # ● Cand găsesti Lăstun sau Trabant:
# # - Salvează aceste masini în masini_vechi.
# # - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# # ● Printează Modele vechi: x.
# # ● Modele noi: x.
# masini_vechi = []
# for masina in masini:
#     if masina == 'Trabant' or masina == 'Lastun':
#         masini.remove('Trabant')
#         masini.remove('Lastun')
#         masini.append('Tesla')
#         masini_vechi.append('Trabant')
#         masini_vechi.append('Lastun')
#         print(f'Modele vechi: {masini_vechi}')
#         print(f'Modele noi: {masini})

# # 6 - Avand dict:
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
#     }
# buget = 15000
# # Prezintă doar mașinile care se încadrează în acest buget.
# # Itereaza prin dict.items() și accesează mașina și prețul.
# # Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
# # Iterează prin listă.
#
# for masini in pret_masini:
#     if pret_masini[masini] < buget:
#         print(masini)
#
# for masini in pret_masini.items():
#     print(masini)
#
# for masini in pret_masini:
#     if pret_masini[masini] < buget:
#         print(f'Pentru un buget de sub 15,000 euro puteti alege masina {masini}')
#
# for masini in pret_masini:
#     print(masini)

# # 7 - Avand lista:
# # ● Iterează prin ea.
# # ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# duplicate = []
# for numar in numere:
#     if numar == 3:
#         duplicate.append(1)
# print(len(duplicate))
# # ___ sau ___
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# duplicate = 0
# for numar in numere:
#     if numar == 3:
#         duplicate += 1
# print(duplicate)

# # 8 - Avand lista:
# # ● Iterează prin ea
# # ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# suma = 0
# for numar in numere:
#     suma += numar  #  nimic = nimic + numar
# print(suma)

# # 9 - Avand lista:
# # ● Iterează prin ea.
# # ● Afișază cel mai mare număr (nu ai voie să folosești max).
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# maxim = 0
# for numar in numere:
#     if numar > maxim:
#         maxim = numar
# print(maxim)

# # 10. Aceeași listă:
# # ● Iterează prin ea.
# # ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# # Ex: dacă e 3, să devină -3
# # ● Afișază noua listă.
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# negative = []
# for numar in numere:
#     if numar > 0:
#         numar = -abs(numar)
#         negative.append(numar)
# print(negative)

# # 11 sau 1 (optional)
# # Itereaza prin listă alte_numere
# # Populează corect celelalte liste
# # Afișeaza cele 4 liste la final

# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for numar in alte_numere:
#     if numar > 0:
#         numere_pozitive.append(numar)
#     if numar < 0:
#         numere_negative.append(numar)
#     if numar % 2 == 0:
#         numere_pare.append(numar)
#     if numar % 2 != 0:
#         numere_impare.append(numar)
# print(f'Numere pare: {numere_pare}')
# print(f'Numere impare: {numere_impare}')
# print(f'Numere pozitive: {numere_pozitive}')
# print(f'Numere negative: {numere_negative}')

# # 12 sau 2 (optional)
# # Ordonează crescător lista fară să folosești sort.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_ordonate = []
# while alte_numere:
#     minimum = alte_numere[0]
#     for numar in alte_numere:
#         if numar < minimum:
#             minimum = numar
#     numere_ordonate.append(minimum)
#     alte_numere.remove(minimum)
# print(numere_ordonate)

# # 13 sau 3 (optional)
# Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
# Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!
# import random
# numar_secret = random.randrange(1, 30)
# numar_ghicit = int(input("Alege numar: "))
# while numar_secret != numar_ghicit:
#     if numar_secret > numar_ghicit:
#         print("Numarul secret este mai mare")
#         numar_ghicit = int(input("Alege alt numar: "))
#     elif numar_secret < numar_ghicit:
#         print("Numarul secret este mai mic")
#         numar_ghicit = int(input("Alege alt numar: "))
#     else:
#         break
# print("Felicitari! Ai ghicit!")

# # 14 sau 4 (optional)
# # Scrie un program care să genereze în consolă următoarea piramidă
# # Ex:3
# # 1
# # 22
# # 333
# x = int(input("Alege un numar: "))
# for i in range(x + 1):
#     for j in range(i):
#         print(i, end='')
#     print('')

# # 15 sau 5 (optional)
# tastatura_telefon = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# for list in tastatura_telefon:
#     for number in list:
#         print(f'Cifra curenta este {number}')
#
#
# test





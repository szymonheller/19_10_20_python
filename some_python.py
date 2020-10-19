# try:
#     print("Dzień dobry")
# except:
#     print("Coś poszło nie tak")
# else:
#     print("Nic nie poszło źle")

# try:
#     print("x")
#     a = 5 / 0
# except:
#     print("Coś poszło nie tak")
# finally:
#     print("Klauzula try-except jest zakończona")


# def division(a, b):
#     result = 0
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         result = "Błąd - nie można dzielić przez 0"
#     finally:
#         print("Zawsze się wypisze")
#     print(result)
#
#
# division(4, 5)
# division(4, 50)
# division(431, 2)
# division(0, 0)


# import sys
# args = sys.argv[1:]
# for arg in args:
#     print(f"Aktualnie przetwarzany plik to {arg}")
#     try:
#         plik = open(arg, "r")
#     except IOError:
#         print(f"Nie mogę otworzyć pliku {arg}")
#     else:
#         print(f"Nazwa pliku to {arg}, liczba wierszy{len(plik.readlines())}")
#         plik.close()
#     finally:
#         if not plik.closed:
#             plik.close()


# x = -1
# if x < 0:
#     raise Exception("Przepraszamy, brak liczb poniżej zera")
#
# print(x)


# x = 1.5
# if not type(x) is int:
#     raise TypeError("Dozwolone są tylko liczby całkowite")
#
# print(x)


# a = open("text.txt", "r")
# tekst =a.read()
# print(tekst)


# a = open("text.txt", "r")
# content_list = a.readlines()
# for x in content_list:
#     print(x)


# f = open("text.txt", "r")
# content_list = f.readlines()
# x = "ddd".join(content_list)
# print(x)


# l = []
# f = open("text.txt", "r")
# for line in f:
#     l.append(line)
# print(l)


# f = open("nowy_plik.txt", "w")
# lista = ["zielony", "bialy", "czarny", "zolty"]
# f.write(" ".join(lista))
# f.close()
# f = open("nowy_plik.txt", "r")
# odczytany_plik = f.read()
# print(odczytany_plik)
# f.close()

fo = open("text.txt", "r")
print("Nazwa pliku: ", fo.name)

line = fo.readline()
print("Czytaj linie: ", line)

fo.seek(4)
line = fo.readline()
print("Czytaj linie: ", line)

fo.close()

# zad 2

# a = 5
# b = "tekst"
# try:
#     result = a + b
# except Exception:
#     result = "Nie możesz dodać int do string"
# print(result)

# zad 3

# lista = [1, 2, 3]
# try:
#     print(lista[5])
# except IndexError:
#     msg = "Jesteś poza zakresem listy"
# print(msg)


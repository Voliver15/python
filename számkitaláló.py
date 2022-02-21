#Készitette: Kovács Patrik, Szabó Zétény, Vucskics Olivér
#2021. 12. 13
import random
szamok=random.randint(1,99)
print(szamok)
#kitalalas=int(input("első játékos: Írj be egy egész számot 1 és 99 között: "))
kitalalas=100
while szamok != "kitalalas":
    print
    kitalalas=int(input("első játékos: Írj be egy egész számot 1 és 99 között: "))
    kitalalas1=int(input("második játékos: Írj be egy egész számot 1 és 99 között: "))
    if kitalalas < szamok or kitalalas1 < szamok:
        print("A választott számod kisebb mint a kitalált szám")
        kitalalas=int(input("első játékos: Írj be egy egész számot 1 és 99 között: "))
        kitalalas1=int(input("második játékos: Írj be egy egész számot 1 és 99 között: "))
    elif kitalalas > szamok or kitalalas1 > szamok:
        print("A választott számod nagyobb mint a kitalált szám")
        kitalalas=int(input("első játékos: Írj be egy egész számot 1 és 99 között: "))
        kitalalas1=int(input("második játékos: Írj be egy egész számot 1 és 99 között: "))
    else:
        print("Kitaláltad!")
        break
    print



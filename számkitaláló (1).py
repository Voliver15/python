#Készitette: Kovács Patrik, Szabó Zétény, Vucskics Olivér
#2021. 12. 13
import random
szamok=random.randint(1,99)
#kitalalas=int(input("Írj be egy egész számot 1 és 99 között: "))
kitalalas=100
#Egyjátékos
while szamok != "kitalalas":
    kitalalas=int(input("Írj be egy egész számot 1 és 99 között: "))
    if kitalalas < szamok:
        print("A választott számod kisebb mint a kitalált szám")
    elif kitalalas > szamok:
        print("A választott számod nagyobb mint a kitalált szám")
    else:
        print("Kitaláltad!")
        break
    
#Többjátékos
    kitalalas=int(input("Első játékos: Írj be egy egész számot 1 és 99 között: "))
    if kitalalas < szamok:
        print("Első játékos: A választott számod kisebb mint a kitalált szám")
    elif kitalalas > szamok:
        print("Első játékos: A választott számod nagyobb mint a kitalált szám")
    else:
        print("Első játékos Kitalálta!")
        break
    
    kitalalas1=int(input("Második játékos: Írj be egy egész számot 1 és 99 között: "))
    if kitalalas1 < szamok:
        print("Második játékos:A választott számod kisebb mint a kitalált szám")
    elif kitalalas1 > szamok:
        print("Második játékos:A választott számod nagyobb mint a kitalált szám")
    else:
        print("Második játékos Kitalálta!")
        break


import dolgozatmodul1

f=open("szavazatok.txt")
sorok=f.read().split("\n")[:-1]
kepviselok=0
for e in sorok:
    if e != "\n":
        kepviselok+=1
f.close()

print("2.feladat")
print("A helyhatósági választáson {} képviselőjelölt indult.".format(kepviselok))

print("3.feladat")
beker=input("Kérek egy kipviselő vezetéknevét: ")
knev=[]
knev.append(dolgozatmodul1.adatok())
print(f"{knev.keresztnev}")
    

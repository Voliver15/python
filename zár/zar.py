import random

f=open("ajto.txt")

kodok=[]
for egysor in f:
    kodok.append(egysor[:-1])

f.close()

print(kodok)

#239451
print("2. feladat")

be=input("Adja meg, mi nyitja a zárat!: ")

print("3. feladat")
sorszam=1
talalat=[]
for kod in kodok:
    if kod ==be:
        talalat.append(sorszam)
        
    sorszam += 1

#szám lista összefűzése
print("A nyitó kódszámok sorai:" + " ".join(str(szam)for szam in talalat))



#kicsit más megoldás
talalat=[]
for index,kod in enumerate(kodok,1):
    if kod ==be:
        talalat.append(index)
        
    sorszam += 1

#szám lista összefűzése
print("A nyitó kódszámok sorai:" + " ".join(str(szam)for szam in talalat))

dupla=[]
for index,kod in enumerate(kodok,1):
    for karakter in kod:
        if kod.count(karakter)>1:
            dupla.append(index)
print("4. feladat")
if len(dupla)>0:
    print(dupla[0])
else:
    print("Nem volt")
    
#5. feladat
ujkod=""
valaszthato=["0","1","2","3","4","5","6","7","8","9"]
while len(ujkod)<len(be):
        szam=random.randint(0,len(valaszthato)-1)
        ujkod+=valaszthato[szam]
        valaszthato.pop(szam)

print("5. feladat")
print("Egy" + str(len(ujkod)) + "hosszú kódszám: " + ujkod)

def nyit(jo,proba):
    egyezik=len(jo)==len(proba)
    if egyezik:
        elteres=ord(jo[0])-ord(proba[0])
        for i in range(1,len(jo)):
            if (elteres-(ord(jo[i])-ord(proba[i]))) % 10 != 0:
                egyezik=False
    return egyezik
nyit()
            















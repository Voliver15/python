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

if len(dupla)>0:
    print(dupla[0])
else:
    print("Nem volt")
            





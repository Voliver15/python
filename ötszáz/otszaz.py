f=open("penztar.txt")
kosar=[]
#szoveg=f.read()
#print(szoveg)
for sor in f:
    kosar.append(sor.strip())
f.close()

print("2. feladat")
print("A fizetések száma: " + str(kosar.count("F")))

print("3. feladat")
print("Az első vásárló " + str(kosar.index("F")) + " darab árucikket vásárolt.")

print("4. feladat")
sorszam=int(input("Vásárlás sorszáma: "))
arunev=input("Árucikk neve: ")
darab=int(input("Darabszám: "))

#a termék első indexe
aruindex=kosar.index(arunev)
darablista=kosar[:aruindex]
#print(darablista)
vasarlasdb=darablista.count("F") +1
#print(vasarlasdb)

print("5. feladat")
print("Az első vásárlás sorszáma: " + str(vasarlasdb))

#a termék utolsó indexe
utolsoindex=0
for i in range(0,len(kosar)):
    if kosar[i*-1-1]==arunev:
        utolsoindex=len(kosar)-i
        break
darablista=kosar[:utolsoindex]
vasarlasdb=darablista.count("F") +1
print("Az utolsó vásárlás sorszáma: " + str(vasarlasdb))

voltF=False
szam=0

for e in kosar:
    if e == arunev:
        



    

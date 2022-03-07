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


aruindex=kosar.index(arunev)
darablista=kosar[:aruindex]
print(darablista)
vasarlasdb=darablista.count("F") +1
print(vasarlasdb)

print("5. feladat")
print("Az első vásárlás sorszáma: " + str(vasarlasdb))

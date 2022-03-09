def ertek(darab):
    if darab==1:
        return 500
    else:
        return darab*400+150



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
        if not voltF:
            szam=szam+1
            voltF=True
    if e=="F":
        voltF=False
print(str(szam)+" vásárlás során vettek belőle.")


print("6. feladat")
print(str(vasarlasdb)+" darab vételekor fizetendő: "+str(ertek(vasarlasdb)))


print("7. feladat")
darabF=0
elozoindex=0
keresettindex=0

for i in range(0,len(kosar)):
    if kosar[i]=="F":
        darabF+=1
        elozoindex=keresettindex
        keresettindex=i
    if darabF==sorszam:
        break
print(kosar[elozoindex+1:keresettindex])
if sorszam>1:
    darabkosar=kosar[elozoindex+1:keresettindex]
else:
    darabkosar=kosar[elozoindex:keresettindex]
    
stat={}
for e in darabkosar:
    if e in stat.keys():
        stat[e]+=1
    else:
        stat[e]=1
print(stat)





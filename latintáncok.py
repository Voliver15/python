#1.feladat
f=open("tancrend.txt")
sorok=f.read().split("\n")[:-1]
f.close()
#print(sorok)
print("2. feladat")
tancok=[]
for i in range(0,len(sorok),3):
    tancok.append(sorok[i:i+3])


#print(tancok)
print("A " + tancok[0][0] + " és a " + tancok[-2][0] + " volt az első és utolsó tánc")
    
print("3.feladat")
samba=sorok.count("samba")
print(str(samba) + " pár mutatta be a sambát")

print("4.feladat")

for e in tancok:
    if e[1]=="Vilma":
        print(e[0])

be=input("Tánc neve: ")
for e in tancok:
    if e[0]==be and e[1]=="Vilma":
        print("A "+be +" bemutatóján Vilma párja " +e[2]+" volt")



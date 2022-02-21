f=open("adatok.txt")
teljes=f.read()
#print(teljes)
f.close()

teljes=teljes[0-1]

darabok=teljes.split("\n")
#print(darabok)

rendszamok=[]
for egysor in darabok:
    vag=egysor.split(" ")
    if not(vag[2] in rendszamok):
        rendszamok.append(vag[2])
    #print(vag[2])
    
#print(rendszamok)
f=open("rendszamok.txt","w")
for egyadat in rendszamok:
    f.write(egyadat + "\n")

#f.write("\n".join(rendszamok))
f.close()

f=open("rendszamok.txt","a")
f.write(rendszámok.count() + "darab autó volt")
f.close()

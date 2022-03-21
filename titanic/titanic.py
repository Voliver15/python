f=open("titanic.txt")
adatok=f.read().split("\n")
f.close()

print("2.feladat: "+ str(len(adatok)) +" darab")

print("3.feladat: "+str(sum([int(e.split(";")[1])+ int(e.split(";")[2]) for e in adatok]))+ " fő")

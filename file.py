#f=open("proba.txt","w")
#f.write("Hello")
#f.close()

def file_kiir(file_nev):
    f=open(file_nev)
    
    print(f.read())
    f.close()




f=open("adatok.txt","a")

be="qwe"
while be != "":
    be=input("Kérek egy szöveget: ")
    if be != "":
        f.write(be+"\n")
f.close()

file_kiir("adatok.txt")

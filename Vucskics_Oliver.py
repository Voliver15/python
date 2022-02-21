#kérj be egy szót amig ez a szó nem üres addig rakd bele a szót a listába és kérj be egy szót
lista=[]
szo=input("kérek egy szót: ")
print(szo)
while szo != "":
    lista.append(szo)
    szo=input("kérek egy szót: ")


def forditott(lista):
    lista.reverse()
    print(lista)
    for i in lista:
        print(i)

forditott(lista)

def nagyb(szo):
    x=szo.title()
    return x
nagyb("")

def felhasznalas(kezdo, darab):
    lista1=[]
    

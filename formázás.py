f1="ide jön a szám: {}"

print(f1.format(123))
szam=input("Kérek egy számot: ")
print(f1.format(szam))

f2="ide is jön valami {0}, ide meg más {1}"
print(f2.format(123,321))


f3="My name is {surname}. {firstname} {surname}."
print(f3.format(firstname="James",surname="Bond"))
f4="Az én nevem {surname}. {surname} {firstname}"
print(f4.format(firstname="James",surname="Bond"))
print(f4.format(firstname="Jakab",surname="Kötés"))

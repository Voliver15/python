szam1=""
szam2=""
while szam1 =="":
    elso=input("Kérem az első számot: ")
    try:
        szam1=int(elso)
    except:
        print("ez nem szám")
while szam2=="":        
    masodik=input("kérem a második számot: ")
    try:
        szam2=int(masodik)
    except:
        print("ez nem szám")
    
#elso=(input("Kérem az első számot: "))
#masodik=(input("kérem a második számot: "))

if elso > masodik:
    print("A nagyobb szám {}, a kisebb szám {}".format(elso,masodik))
elif masodik > elso:
    print("A nagyobb szám {}, a kisebb szám {}".format(masodik,elso))
else:
    print("A két szám egyenlő")

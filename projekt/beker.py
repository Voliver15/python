#adatbekérővlass
#rendszám, sofőr, indulkm, megállkm, tankolás

class beker:
    def __init__(self):
        pass
    def form(self):
        self.rendszam=input("Rendszám: ")
        self.sofőr=input("Sofőr: ")
        self.indulkm=int(input("Indul(km): "))
        self.megallkm=int(input("Megall(km): "))
        self.tankol=int(input("Tankolt liter (0, ha nem): "))

if __name__=="__main__":
    adat=beker()
    adat.form()
    print("megtett km: "+str(adat.megallkm-adat.indulkm))
else:
    print("Ez egy modul")

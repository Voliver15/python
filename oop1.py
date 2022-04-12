#osztály definíció
class Kutya:
    #konstruktor
    def __init__(self,nev):
        self.nev=nev
    #osztályfüggvény
    def ugat(self):
        print("VAU-VAU ("+self.nev+")")
        
#példányosítás
        
egyKutya=Kutya("Armageddon")
egyKutya.ugat()
print(egyKutya.nev)
#osztályváltozó értékadása

egyKutya.nev="Bruno"
print(egyKutya.nev)
#öröklés,leszármaztatás

class NemetJuhasz(Kutya):
    #újfüggvény
    def pitiz(self):
        print(self.nev+": nein!")
    #függvény felülírás
    def ugat(self):
        print("WAU-WAU")

n=NemetJuhasz("Rex")
n.ugat()
n.pitiz()
n2=NemetJuhasz("Kondér")
n2.pitiz()
n2.ugat()

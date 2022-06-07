class adatok:
    def __init__(self,sor):
        vag=sor.split(" ")
        self.valasztokerulet=vag[0]
        self.szavazatok=vag[1]
        self.vezeteknev=vag[2]
        self.utonev=vag[3]
        self.part=vag[4]

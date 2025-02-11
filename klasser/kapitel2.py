class Karaktär:
    def __init__(self,namn,hälsa):
        self.namn = namn
        self.hälsa = hälsa

    def köra(self,position):
        print(f"{self.namn} kör till position {position}")

karaktär1=Karaktär("Melker",11)
karaktär2=Karaktär("Messi",10)

print(karaktär1.namn , karaktär1.hälsa ,"\n", karaktär2.namn , karaktär2.hälsa)



karaktär1.köra("märsta")

    
    
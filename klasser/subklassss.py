class Djur():
    def __init__(self,namn):
        self.namn=namn


    def läte(self):
        print(f"Djuret {self.namn} låter!!!")


class Hund(Djur):
    def läte(self):
        print(f"Hunden {self.namn} säger voff!!!")


class Katt(Djur):
    def läte(self):
        print(f"Katten {self.namn} säger mjau!!!")


djur=Djur("vet ej")
hund=Hund("Melker")
katt=Katt("Forberg")


djur.läte()
hund.läte()
katt.läte()
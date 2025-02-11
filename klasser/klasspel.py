class Karaktär():
    def __init__(self,namn,hälsa,attackkraft):
        self.namn = namn
        self.hälsa = hälsa
        self.attackkraft = attackkraft

    def ta_skada(self,skada):
        self.hälsa -= skada
        print(f"{self.namn} har {self.hälsa} hälsa kvar")
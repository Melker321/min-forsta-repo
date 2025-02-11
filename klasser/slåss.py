import random

class Karaktär: #karaktär är superklassen
    def __init__(self, namn, hp):
        self.namn = namn
        self.__hp = hp # ger privat attribut, så det blir säkrare. får hp genom getter


    def get_hp(self): #skapar metod så man kan nå värdet hp
        return self.__hp

    def set_hp(self, värde):
        if värde < 0:  # om värde(hp) är under 0 så sätter man det till noll igen genom set.
            self.__hp = 0
        else:
            self.__hp = värde #om värdet är rätt, alltså över noll så händer inget

    def ta_skada(self, skada):
        self.set_hp(self.get_hp() - skada)# tar bort skadan med get som är hp nu och set ändrar hpt
        print(f"{self.namn} har {self.get_hp()} hälsa kvar.\n")#visar hälsan genom metoden get_hp

    def attackera(self, annan_karaktär):
        if self.get_hp() <= 0:
            #print(f"{self.namn} har noll hp kvar och kan inte attackera")
            return False #gör så att koden slutar eftersom någon har 0 hp
        if annan_karaktär.get_hp() <= 0:
            #print(f"{annan_karaktär.namn} är redan död")
            return False

        val = "" # gav val en sträng för om man fick under 31 hp så fick man felmedelande. 

        if self.get_hp() >= 31 and annan_karaktär.get_hp() >= 31: #om hp är 31 eller mer så kan karaktärerna använda dubbel attack
            val = input(f"\nVill du med {self.namn} karaktären göra ett dubbelslag mot {annan_karaktär.namn}? Detta kostar 30 hp. ja eller nej: ").lower()
        if val == "ja": # om man svarar ja så dubbel attackerar man
            self.dubbelslag(annan_karaktär)
            return True #visar att man kunde utföra attacken
        
        if isinstance(self, Mage):  #tittar så att  karaktären är har Mage och har den subklassen

            val = input(f"\nVill du att {self.namn} använder mana för en magisk attack ja eller nej? pris 20 mana: ").lower()
            if val == "ja":
                mana_kostnad = 20
                if self.get_mana() >= mana_kostnad: #om man har mer än 20 mana så kan man köpa
                    self.använd_mana(mana_kostnad)
                    magisk_skada = random.randint(30, 50) #skadar mellan 30 till 50 hp
                    print(f"\n{self.namn} använder en magisk attack och gör {magisk_skada} skada!\n")
                    annan_karaktär.ta_skada(magisk_skada) # skadar andra spelaren
                    return True

        skada = random.randint(10, 30) #om man inte använder attacken så skadar  man mellan 10 till 30 hp

        print(f"\n{self.namn} attackerar {annan_karaktär.namn} och gör {skada} skada")
        annan_karaktär.ta_skada(skada)
        return True

    def dubbelslag(self, annan_karaktär): # skapar metoden som användes innan
        if self.get_hp() <= 30:
            print(f"{self.namn} har inte tillräckligt med HP för dubbelslag.\n")
            return # slutar metoden för man man inte hade tillräckligt med hp

        self.set_hp(self.get_hp() - 30) # ändrar get värdet med hjälp av set. - 30 hp
        dubbelslag_skada = random.choice([5, 50]) # skadar 5 eller 50 hp
        print(f"\n{self.namn} gör ett dubbelslag mot {annan_karaktär.namn}, kostar 30 HP och gör {dubbelslag_skada} skada\n")
        annan_karaktär.ta_skada(dubbelslag_skada)

class Mage(Karaktär): # skapar subklassen Mage som är ärver från superklassen karaktär

    def __init__(self, namn, hp, mana): # skapar atribut
        super().__init__(namn, hp) #ärver metoder från superklassen
        self.__mana = mana #skapar privart värde som bara nås med hjälp ut av en metod

    def get_mana(self):
        return self.__mana #  returnerar värdet på mana till metoden


    def set_mana(self, mängd_mana): # skapar metod för mana
        if mängd_mana >= 0: # ser till att värdet blir rätt
            self.__mana = mängd_mana
        else:
            print(f"Mana kan inte vara negativt. {self.namn} har fortfarande {self.get_mana()} mana.")

    def använd_mana(self, mängd_mana):
        if self.get_mana() >= mängd_mana:#tittar så man har tillräckligt med mana
            self.set_mana(self.get_mana() - mängd_mana) #ändrar värdet på mana med hjälp av set
            print(f"{self.namn} har använt {mängd_mana} mana, {self.get_mana()} mana kvar.\n")
        else:
            print(f"{self.namn} har inte tillräckligt med mana för detta.\n")

class Arena:
    def __init__(self):
        pass#

    def starta_fight(self, spelare1, spelare2):
        print(f"\n\n{spelare1.namn} med {spelare1.get_hp()} HP och {spelare2.namn} med {spelare2.get_hp()} HP börjar slåss")
        while spelare1.get_hp() > 0 and spelare2.get_hp() > 0: #när spelarna har mer än 0 hp så kan de attackera varandra.
            spelare1.attackera(spelare2)
            if spelare2.get_hp() <= 0:
                print(f"{spelare2.namn} har dött! {spelare1.namn} har vann!\n")
                break # när spelare2 har 0 hp så slutar spelet


            spelare2.attackera(spelare1)
            if spelare1.get_hp() <= 0:
                print(f"{spelare1.namn} har dött! {spelare2.namn} har vann!\n") 
                break # när spelare1 har 0 hp så slutar spelet


spelare1 = Mage("Superman", 100, 50)# objekt skapas, denna är insats ut av Mage. med 2 parametrar hp och mana. går på grund ut av __init__, skapar de...
spelare2 = Karaktär("Batman", 120) # samma här men insats av karaktär och en parameter hp

arena = Arena() #objekt arena skapas av klassen Arena
arena.starta_fight(spelare1, spelare2)#metoden anropas

print()
spelare1.attackera(spelare2)
print()
spelare2.attackera(spelare1)
print()


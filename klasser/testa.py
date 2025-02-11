import random

class Karaktär:
    def __init__(self, namn, hp):
        self.namn = namn
        self.__hp = hp  # privat

    def get_hp(self):
        return self.__hp

    def set_hp(self, värde):
        if värde < 0:
            self.__hp = 0  # Sätt HP till 0 om det är negativt
        else:
            self.__hp = värde

    def ta_skada(self, skada):
        # Ta skada och sätt HP till 0 om det blir negativt
        self.set_hp(self.get_hp() - skada)
        print(f"{self.namn} har {self.get_hp()} hälsa kvar")

    def attackera(self, annan_karaktär):
        if self.get_hp() <= 0:
            print(f"{self.namn} har noll hp kvar och kan inte attackera")
            return False  # Returnera False om spelaren inte kan attackera
        if annan_karaktär.get_hp() <= 0:
            print(f"{annan_karaktär.namn} är redan död")
            return False  # Returnera False om den andra spelaren är död

        val = ""  # Gör så valet alltid är definierat
        if self.get_hp() >= 31 and annan_karaktär.get_hp() >= 31:
            val = input(f"Vill du med {self.namn} karaktären utföra ett dubbelslag mot {annan_karaktär.namn}? Detta kostar 30 hp. (ja/nej): ").lower()
        if val == "ja":
            self.dubbelslag(annan_karaktär)
            return True  # Returnera True om dubbelslaget utfördes
        
        if isinstance(self, Mage):  # Kollar om spelaren är en Mage
            val = input(f"Vill du att {self.namn} använder mana för en magisk attack (ja/nej)? ").lower()
            if val == "ja":
                mana_kostnad = 20
                if self.get_mana() >= mana_kostnad:
                    self.använd_mana(mana_kostnad)  # Använd mana
                    magisk_skada = random.randint(30, 50)  # Magisk attack gör mer skada
                    print(f"{self.namn} använder en magisk attack och gör {magisk_skada} skada!")
                    annan_karaktär.ta_skada(magisk_skada)
                    return True  # Returnera True för en magisk attack
                else:
                    print(f"{self.namn} har inte tillräckligt med mana.")
                    # Om inte tillräcklig mana finns, fortsätt med fysisk attack

        # Om ingen magisk attack används, fortsätt med fysisk attack
        skada = random.randint(10, 30)
        print(f"{self.namn} attackerar {annan_karaktär.namn} och gör {skada} skada")
        annan_karaktär.ta_skada(skada)
        return True  # Returnera True om attacken genomfördes

    def dubbelslag(self, annan_karaktär):
        if self.get_hp() <= 30:
            print(f"{self.namn} har inte tillräckligt med HP för att utföra ett dubbelslag.")
            return

        self.set_hp(self.get_hp() - 30)
        dubbelslag_skada = random.choice([5, 50])  # Skada blir antingen 5 eller 50
        print(f"{self.namn} utför dubbelslag mot {annan_karaktär.namn}, kostar 30 HP och gör {dubbelslag_skada} skada")
        annan_karaktär.ta_skada(dubbelslag_skada)

class Mage(Karaktär):
    def __init__(self, namn, hp, mana):
        super().__init__(namn, hp)  # Ärver från Karaktär
        self.__mana = mana  # Privat mana

    def get_mana(self):
        return self.__mana

    def set_mana(self, mängd_mana):
        if mängd_mana >= 0:
            self.__mana = mängd_mana
        else:
            print(f"Mana kan inte vara negativt. {self.namn} har fortfarande {self.get_mana()} mana.")

    def använd_mana(self, mängd_mana):
        if self.get_mana() >= mängd_mana:  # Säkerställer att det finns tillräckligt med mana
            self.set_mana(self.get_mana() - mängd_mana)
            print(f"{self.namn} har använt {mängd_mana} mana, {self.get_mana()} mana kvar.")
        else:
            print(f"{self.namn} har inte tillräckligt med mana för detta.")

class Arena:
    def __init__(self):
        pass

    def starta_fight(self, spelare1, spelare2):
        print(f"{spelare1.namn} och {spelare2.namn} börjar slåss")
        while spelare1.get_hp() > 0 and spelare2.get_hp() > 0:
            # Spelare 1 attackerar spelare 2
            spelare1.attackera(spelare2)

            # Kontrollera om spelare 2 har dött efter spelare 1's attack
            if spelare2.get_hp() <= 0:
                print(f"{spelare2.namn} har dött! {spelare1.namn} har vunnit!\n")
                break

            # Spelare 2 attackerar spelare 1
            spelare2.attackera(spelare1)

            # Kontrollera om spelare 1 har dött efter spelare 2's attack
            if spelare1.get_hp() <= 0:
                print(f"{spelare1.namn} har dött! {spelare2.namn} har vunnit!\n")
                break

# Skapa spelare
spelare1 = Mage("Superman", 100, 50)
spelare2 = Karaktär("Batman", 115)

# Starta arena och strid
arena = Arena()
arena.starta_fight(spelare1, spelare2)

# Extra exempel på användning
print()
spelare1.attackera(spelare2)
print()
spelare2.attackera(spelare1)
print()


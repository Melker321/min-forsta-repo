class Pet:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self): 
        return self.__age

    def set_age(self, värde):
        if värde < 0:  
            self.__age = 0
        else:
            self.__age = värde 

    def speak(self):
        print("Djuret pratar")


class Cat(Pet):  # Ärver från Pet
    def __init__(self, name, age):
        super().__init__(name, age)  # Använd basklassens konstruktor

    def speak(self):
        print(f"{self.name} säger: Mjau!")


# Exempel på hur klasserna används
min_katt = Cat("Misse", 3)
min_katt.speak()  # Skriver ut: Misse säger: Mjau!
print("Ålder:", min_katt.get_age())
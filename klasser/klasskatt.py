class Pet:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def get_age(self): 
        return self.__age

    def set_age(self, värde):
        if värde < 0:  
            self.__age = 0
        else:
            self.__age = värde 

    def speak(self,):
        print("Djuret pratar")


class Cat(Pet):
    def __init__(self,name,age):
        super().__init__(name, age)

    def speak(self):
        print(f"{self.name} säger: Mjau!")




min_katt = Cat("Misse", 88)
min_katt.speak() 
print("Ålder:", min_katt.get_age())





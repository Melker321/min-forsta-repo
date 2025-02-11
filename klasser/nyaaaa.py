class Person:
    def __init__(self,namn,ålder):
        self.__namn = namn
        self.__ålder = ålder

    def get_namn(self):
        return self.__namn
    
    def set_namn(self,namn):
        self.__namn = namn


    def get_ålder(self):
        return self.__ålder
    
    def set_ålder(self,ålder):
        self.__ålder = ålder 


class Student(Person):
    def __init__(self, namn, ålder, _studieprogram):
        super().__init__(namn, ålder)
        self._studieprogram = _studieprogram
        

    def visa_info(self):
        print(f"Jag heter {self.get_namn} och min ålder är {self.get_ålder} och mitt studieprogram är {self._studieprogram}")



person = Person("HANS", 34,)
student = Student("Någon", 46, "simma")




student.visa_info()
person.visa_info()

class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
    def tanishtir(self):
        print(f"assalomu alaykum mening ismin {self.ism} familiyam {self.familiya} , yoshim {self.tyil}")
    def get_name(self):
        return self.ism
    def get_age(self,yil):
        return yil - self.tyil
talaba1=Talaba("Hojiakbar","Azimov",2005)
talaba2=Talaba("Ozodbek","Nematov",1998)
talaba3=Talaba("Doniyorbek","Najmiddinov",2001)
print(talaba2.get_name())
print(talaba2.get_age(2023 ))

        
    
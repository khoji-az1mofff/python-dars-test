# class Talaba:
#     def __init__(self,ism,familiya,tyil):
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil
#     def tanishtir(self):
#         print(f"assalomu alaykum mening ismin {self.ism} familiyam {self.familiya} , yoshim {self.tyil}")
#     def get_name(self):
#         return self.ism
#     def get_age(self,yil):
#         return yil - self.tyil
# talaba1=Talaba("Hojiakbar","Azimov",2005)
# talaba2=Talaba("Ozodbek","Nematov",1998)
# talaba3=Talaba("Doniyorbek","Najmiddinov",2001)
# print(talaba2.get_name())
# print(talaba2.get_age(2023 ))

# class Fan():
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni=0
#         self.talabalar=[]
#     def add_talabalar(self,talaba):
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
#     def get_name(self):
#         return self.nomi
#     def get_students(self):
#         return []


# class Shaxs:
#     def __init__(self,ism,familiya,passport,tyil):
#         self.ism=ism
#         self.familiya=familiya
#         self.passport=passport
#         self.tyil=tyil
#     def get_info(self):
#         info=f" Ism : {self.ism}\n Familya : {self.familiya}\n Passport seriya : {self.passport}\n Tug'ulfan yil : {self.tyil}"
#         return info
#     def get_age(self,yil):
#         return f"{self.ism} {self.familiya} hozirda {yil - self.tyil} yoshda" 


# class Talaba(Shaxs):
#     def __init__(self, ism, familiya, passport, tyil,idraqam,manzil):
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam=idraqam
#         self.bosqich=1
#         self.manzil=manzil 
#     def get_id(self):
#         return f"{self.ism} {self.familiya} ning ID raqami : {self.idraqam}" 
#     def get_bosqich(self):
#         return f"{self.ism} {self.familiya} {self.bosqich}-da" 
#     def get_info(self):
#         info=f" Ism : {self.ism}\n Familya : {self.familiya}\n Passport seriya : {self.passport}\n Tug'ulfan yil : {self.tyil}\n ID raqami : {self.idraqam}\n Bosqich : {self.bosqich}"
#         return info
# class Manzil:
#     def __init__(self,uy,kocha,tuman,viloyat):
#         self.uy=uy
#         self.kocha=kocha
#         self.tuman=tuman
#         self.viloyat=viloyat
#     def get_manzil(self):
#         manzil=f"{self.viloyat} viloyati {self.tuman} tumani {self.kocha} ko'chasi {self.uy}-uy"
#         return manzil

# talaba1_manzil=Manzil(221,"Dulkushod","Baliqchi","Andijon")
# talaba1=Talaba("Hojiakbar","Azimov","AD1234567",2005,"NO1234567",talaba1_manzil)
# print(talaba1.get_info())

class Qidir:
    def __init__(self,name,lastname,tyil,passport_id,id_raqam):
        self.name=name
        self.lastname=lastname
        self.tyil=tyil
        self.passport_id=passport_id
        self.id_raqam=id_raqam
    def get_info(self):
        info=f" Ism : {self.name}\n Familiya : {self.lastname}\n Tug'ulgan yil : {self.tyil}\n Passport ID : {self.passport_id}\n ID raqam : {self.id_raqam}"
        return info
    def get_age(self,yil):
        return yil - self.tyil
    def qidiruv(self):
        idRaqam=input("ID raqam kiriting: ")
        if idRaqam == self.id_raqam:
            print(talaba2.get_info())
        else:
            print("Bunday ID raqamga ega talaba topilmadi!!!")
talaba1=Qidir("Hojiakbar","Azimov",2005,"AD1234567","N%1234567")
talaba2=Qidir("Husniddin","Sadriddinov",2005,"AD7654321","N%7654321")
print(talaba2.qidiruv())

        

        
    
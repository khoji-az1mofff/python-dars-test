# if else
# avtolar=["naxia","audi","mers","tayota"]
# for avto in avtolar:
#     if avto == "mers":
#         print(avto.upper())
#     else:
#         print(avto.title())

# mevalar=["olma","bexi","nok","banan","tarvuz"] 
# for meva in mevalar:
#     if meva == "olma":
#         print("men mazzali "+meva+" yeyishni hohlayman")

# if 12 == 12:
#     for i in range(12):
#         print(i+1)
# else:
#     print("yo'q")

# son=45
# if 44+1 >=son and 15==15:
#     print("ha")
# else:
#     print("yo'q")
# il elif
# yosh= int(input("yoshingizni kiriting = "))
# if yosh <= 4:
#     print("sizning yoshingiz "+str(yosh)+" da sizga kirish bepul.")
# elif yosh <= 12:
#     print("sizning yoshingiz "+str(yosh)+" da sizga kirish 5000 so'm.")
# else:
#     print("sizga kirish 10000 so'm.")

# if 12==11 and 12<=12:
#     print("12 = 12 ga")
# else:
#     print("12 katta 12 dan")


# print("hammaga salom")

# 14 - dars lug'atlar bilan ishlash

# cars={
#       "model":"ferrari",
#       "tur":"sport car",
#       "rangi":"qizil"
#       }
# print(cars["rangi"])

# mevalar_narxi={'olma':5000,
#                "o'rik":7000,
#                "shaftoli":12000,
#                "apelsin":14000,
#                "nok":7000
#                }
# print(mevalar_narxi)

# for meva in mevalar_narxi:
#     print(meva)
# mevalar_narxi["olcha"]=17000
# print(mevalar_narxi )
# del mevalar_narxi["apelsin"]
# print(mevalar_narxi)

# print("mana yana boshladik azizlar ")

# lug'atlar bilan ishlash 2- qism

# talaba={
#     "ism":"Hojiakbar",
#     "familiya":"Azimov",
#     "fakultet":"ISE_N-23UA",
#     "yosh":18,
#     "kurs":4
# }
# print(talaba.values())

# for kalit,qiymat in talaba.items():
#     print(f"kalit: {kalit}")
    # print(f"Key:{key}")
    # print(f"Value:{value}\n")
    
# telefonlar={
#     "ali":"iphone x",
#     "orif":"samsung S10",
#     "sobir":"nokia 1110",
#     "vali":"lg x5 cam"
# }
# print(telefonlar)

# for  tel in telefonlar.values ():
#     print(tel.title())

# NESTING

# son= int(input("son kirit : "))
# print(son)

# ism="hojiakbar"
# familiya="azimov"
# print(f"{ism} ning familiyasi {familiya}")

# son=1
# while son<=5:
#     print(son,end=' ')
#     son+=1
   
# va nihoyat muommolarni hal qildim va yana boshladik
# print("hammaga salom men qaytdim")
# son=1
# while son<=5:
#     print(son, end=" ")
#     son=son+1
# print("dastur tugadi ")

# print("Kiritilgan soni kivadratini aniqlovchi dastur:  ")
# savol="istalgan son kiriting"
# savol+=("dasturni to'xtatish uchun 'exit' deb yozing: ")
# qiymat=''
# while qiymat != 'exit':
#     qiymat=input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

# whileni keyinroq kerak bolganda qilamiz zerikarli ekan shunchun endi functionga o'tamiz
# FUNCTION

# def salom_ber():
#     """salom beruvchi function"""
#     print("assalomu alaykum")
# salom_ber()

# def daraja(son):
#     """kiritilgan soni darajasini aniqlovchi function"""
#     print(f"{son} ning darajasi {son**2} ga teng")
# daraja(float(input("bu yerga son kiriting : ")))

# def ism_familiya_age(ism,familiya,age):
#     """foydalanuvchining ism va familiyasini jamlab chiqaruvchi function"""
#     print(f"Foydalanuvchiling ismi : {ism.title()}\n"
#           f"Foydalanuvchining familiyasi : {familiya.title()}\n"
#           f"Foydalanuvchining yoshi : {age}")
# ism_familiya_age("hasan","odilov",18)

# def yosh_aniqla(ism,tugulgan_yil):
#     """foydalanuvchuning ismi tug'ulgan yilini oladi va ism,yil va yoshni chiqaradi"""
#     print(f"foydalanuvchining ismi : {ism.title()}\n"
#           f"foydalanuvchining tug'ulgan yili : {tugulgan_yil}\n"
#           f"foydalanucvhining yoshi : {2023-tugulgan_yil}")
# yosh_aniqla(input("ismongizni kiriting : "),int(input("tug'ulgan yilingizni kiriting : ")))

# def toliq_ism_yasa(ism,familiya):
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
# talaba=toliq_ism_yasa("olim","hasanov")
# print(talaba)

# def massiv_ortacha_qiymat(massiv, k, l):
#     if k < 0 or l >= len(massiv) or k > l:
#         return None
#     total = 0
#     count = 0
#     for i in range(k, l + 1):
#         total += massiv[i]
#         count += 1

#     if count == 0:
#         return None

#     ortacha_qiymat = total / count
#     return ortacha_qiymat
# massiv = range(101)
# k = int(input("K elementini kitiring : "))
# l = int(input("L elementini kitiring : "))
# natija = massiv_ortacha_qiymat(massiv, k, l)

# if natija is not None:
#     print(f"{k}-dan {l}-gacha bo'lgan elementlar ortacha qiymati: {natija}")
# else:
#     print("Xato!")

# def toliq_ism_yasa(ism,familiya):
#     """toliq ism va familiyani oladigon function"""
#     toliq_ism=f"{ism} {familiya}"
#     return toliq_ism
# talaba1=toliq_ism_yasa("odilov","alisher")
# talaba2=toliq_ism_yasa("odilov","ozodbek")
# print(talaba2)


# def hisobla(son):
#     print(son**2)
# hisobla(float(input("son kiriting: ")))

# def ism_familiya_age(ism,familiya,age):
#     """foydalanuvchining ismi , familiyasi va age sini chiqaruvchi function"""
#     print(f"Foydalanuvchining ismi : {ism}\n"
#           f"Foydalanuvchingnin familiyasi : {familiya}\n"
#           f"Foydalanuvchining yoshi : {age}")
# ism_familiya_age("Hojikabr","Azimov",18)

# def toliq_ism_yarat(ism,familiya,otasining_ismi=''):
#     """  """
#     if otasining_ismi:
#         toliq_ism=f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism=f"{ism} {familiya}"
#     return toliq_ism
# talaba1=toliq_ism_yarat("Hojiakbar","Azimov","Oybek o'g'li")
# talaba2=toliq_ism_yarat("Hojiakbar","Azimov")
# print(talaba2)
        

# def avto_info(kompaniya,model,rangi,korobka,yili,narxi):
#     avto={
#         "kompaniya":kompaniya,
#         "model":model,
#         "rangi":rangi,
#         "korobka":korobka,
#         "yili":yili,
#         "narxi":narxi
#     }
#     return avto
# mashina1=avto_info("GM","Gentra","qora","mexanika",2005,30000)
# mashina2=avto_info("GM","Lasetti","oq","avto",1999,34000)
# mashinalar=[mashina1,mashina2]
# print("bizning online bozorda mavjuda mashinalar : ")

#  

# def avto_info(kompaniya,model,rangi,korobka,yili,narxi):
#     avto={
#         "kompaniya":kompaniya,
#         "model":model,
#         "rangi":rangi,
#         "korobka":korobka,
#         "yili":yili,
#         "narxi":narxi
#     }
#     return avto
# print("Saytimizda avtolar ro'yxatini shakillantiramiz.")
# avtolar=[]
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting: \n",end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")        
#     model=input("Mashina turi: ")        
#     rangi=input("Mashina rangi: ")        
#     korobka=input("Avto yoki mexanika: ")        
#     yili=int(input("Yilini kiriting: "))      
#     narxi=int(input("Narxini kiriting: "))   
#     avtolar.append(avto_info(kompaniya,model,rangi,korobka,yili,narxi))
#     javob=input("Yana Mashina qo'shasizmi ? (ha/yo'q): ")
#     if javob=="yo'q":
#         break
# print("\nSalonimizdagi mashinalar: ")
# for avto in avtolar:
#     if avto["narxi"]:
#         narh=avto["narxi"]
#     else:
#         narh="Noma'lum"
#     print(f"Mashinaning rangi: {avto['kompaniya'].title()}\n"
#           f"Mashinaning turi: {avto['model'].title()}\n"
#           f"Mashinaning rangi: {avto['rangi']}\n"
#           f"Mashina mexanika yoki avto: {avto['korobka'].title()}\n"
#           f"Mashina ishlab chiqarilgan yili: {avto['yili']}\n"
#           f"Mashinaning narxi: {avto['narxi']}$")


# def bahola(ismlar):
#     baholar={}
#     while ismlar:
#         ism=ismlar.pop()
#         baho=input(f"Talaba {ism.title()} ning bahosini kiriting: ")
#         baholar[ism]=int(baho)
#     return baholar
# talabalar=['ozodbek','doniyor','oyatillo','hojiakbar']
# baholar=bahola(talabalar)
# print(baholar)

# def summa(*sonlar):
#     yigindi=0
#     for son in sonlar:
#         yigindi+=son
#     return yigindi
# print(summa(2,4394234023985174391342875874361973497381))
# def summa(*sonlar):
#     return sum(sonlar)
# print(summa(2,4394234023985174391342875874361973497381))
#  
# import salom as s

# salom_ber_=s.salom_ber('muhammadmirzo')
# from salom import *

# salom_ber("muqaddam ")

# import math

# print(math.pow(5,2))

import random as r

# son=r.randint(1,100)
# print(son)

ismlar=['94','95','99','91']
ism=r.choice(ismlar)
print(ism)

  
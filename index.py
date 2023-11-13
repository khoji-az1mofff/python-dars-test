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
    
telefonlar={
    "ali":"iphone x",
    "orif":"samsung S10",
    "sobir":"nokia 1110",
    "vali":"lg x5 cam"
}
print(telefonlar)

for ism , tel in telefonlar.items():
    print(f"{ism.title()}ning telefoni {tel}")
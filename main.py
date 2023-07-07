name = input("isminizi giriniz:")
print(f"hoşgeldiniz   sayın {name} ".upper())

acıklama = """oyunumuz iki sayı arasındaki sayılar kümesinde seçtiğimiz sayıyı tutturabilme oyunudur ilk önce sizlerden hangi iki
          sayı arasında  küme oluşturup sayı seçelim onu soracağız ardından istediğiniz sayı aralıklarındaki seçtiğimiz sayıyı
          tahmin etmenizi sizlerden isteyeceğiz """
print(acıklama)

number1 = int(input("başlangıç sayınızı giriniz :"))
number2 = int(input(" bitmesini istediğiniz,son sayıyı giriniz :"))
from random import shuffle
from random import randint

sayı = list(range(number1, number2 + 1))
print(sayı)

shuffle(sayı)

choise = float(input(f"seçiminizi bu sayılar {sayı} arasından birini seçerek yapınız :"))

print("seçimimiz yapılıyor ....")

computer = randint(number1, number2)
print(f"seçimimiz : {computer}")

if choise == computer:
    print("tebrikler bildiniz ...")
    print(f"sayımız {computer} ve seçiminiz ile eşleşmiştir  :-  )")

else:
    print("maalesef bilemediniz tekrar deneyiniz ")
    print(f"sayımız {computer} ...")




import random

karakterler = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
uzunluk = int(input('uzunluk girin lütfen : '))
parola=''
for i in range(uzunluk):
    sellected=random.choice(karakterler)
    parola+=sellected
print(parola)

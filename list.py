import random

bilangan = random.randint(100,999)
print(bilangan)
digit1 = int(bilangan/100)
digit2 = int((bilangan%100)/10)
digit3 = bilangan%10


if digit1 == digit1 and digit2 == digit3 and digit1 == digit3 :
    print("Tuan Mik mendapatkan JACKPOT")
elif digit1 == digit2 or digit2 == digit3 or digit1 == digit3 :
    print("tuan mik mendapatkan kembali uangnya")
elif digit1 != digit2 and digit2 != digit3 and digit1 != digit3:
    print("tuan mik kehilangan seluruh uangnya")
"""b = "9"
print(type(b))

A=9
B=3
print(A/B)"""

"""birth_year=int(input())
print("birth tear:",birth_year)
print(type(birth_year))

print(type(30<25))"""

#repeat command
for something in range(10): #using (while) can be use as repeate to but in a condition. this command more useable in industry
    print("Hello")

seats = int(input())
while seats > 0 : #while
    print("sell tickets")
    seats = seats  -1
 
password = "wkwkkwkwkwkkw"
guess = "1234"
print(guess != password) # (==) : equal to, (!=) : not equal

pw = "Haiki" #contoh password section
tebakan = input("masukkan password :")
while tebakan != pw :
    tebakan = input("masukkan password :")
print("access granted")

game = ["valorant", "assetto corsa", "albion" ] 
choice = int(input("berikan pilihan mu : "))
print(game[choice])
print(game[1:3])

import random
PlayerIn = True
DealerIn = True

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A','J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
player = []
dealer = []

def dealcard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

#jumlah kartu
def total(turn):
    total = 0
    face = ['J','K','Q']
    for card in turn :
        if card in range(1,11):
             total += card
        elif card in face : 
            total += 10
        else:
            if total > 11:
                total += 1
            else :
                total += 11
    return total

#check for winner
def revealDealerHand():
    if len(dealer)==2:
        return dealer[0]
    elif len(dealer)>2 :
        return dealer[0], dealer[1]

#Main Program
for _ in range (2):
    dealcard(dealer)
    dealcard(player)

print("dealer : ",dealer)
print("player :", player)

while PlayerIn or DealerIn :
    print(f"dealer had {revealDealerHand()} and X")
    print(f"you have {player} for a total of {total(player)}")
    if PlayerIn :
        StayorHit = input("1: Stay\n2: Hit\n")
        while StayorHit not in ['1','2']:
            StayorHit = input("error ")
    if total(dealer) > 16 :
        DealerIn = False
    else :
        dealcard(dealer)
    if StayorHit == '1':
        PlayerIn = False
    
    elif StayorHit == '2':
        dealcard(player)

    if total(player) >= 21:
        break
    elif total(dealer) >= 21 :
        break
if total(player) == 21 :
    print(f"you have {player} for a total of 21 and the dealer has {dealer} for a total of {total(dealer)}")
    print("BlackJack! You Win")
elif total(dealer) == 21 :
    print(f"you have {player} for a total of {total(player)}and the dealer has {dealer} for a total of {total(dealer)}")
    print("BlackJack! Dealer Wins")
elif total(player) > total(dealer) :
    print(f"you have {player} for a total of {total(player)}and the dealer has {dealer} for a total of {total(dealer)}")
    print("BlackJack! You Win")
elif total(player) < total(dealer) : 
    print(f"you have {player} for a total of {total(player)}and the dealer has {dealer} for a total of {total(dealer)}")
    print("BlackJack! Dealer Wins")
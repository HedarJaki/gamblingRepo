import random
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

def casino():
    gambling = random.choice

def topup():
    while True:
        amount = input("how much do you want to topup? ")
        if amount.isdigit() :
            amount = int(amount)
            if amount > 0 :
                return amount
            else:
                print("amount must greater than 0")
        else:
            print("please enter a number")

def get_number_of_lines():
    while True:
        get_lines = input("how much lines do you want to bet? ")
        if get_lines.isdigit() :
            get_lines = int(get_lines)
            if 0 < get_lines <= MAX_LINES :
                return get_lines 
            else:
                print("line must greater than 0, less or equal to 3")
        else:
                print("please enter a number")

def get_bet():
    while True:
        amount = input("how much do you want to bet? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<=amount<=MAX_BET:
                return amount
            else:
                print(f"your amount must between ${MIN_BET} - ${MAX_BET}")
        else:
            print("please enter a number!")

def choice_topup(balance):
    while True :
        stored_balance = input("1 : topup\n2 :  continue\nChoice : ")
        if stored_balance.isdigit():
            stored_balance = int(stored_balance)
            if stored_balance == 1:
                balance += topup()
                print(f"now you have ${balance}")
                return balance
            elif stored_balance == 2:
                return
            else:
                print("please enter 1 if you want to topup or enter 2 if you want to continue")
        else:
            print("please enter number 1 or 2")

def minusbalance(balance, total_bet):
    while True:
        amount = input("topup : ")
        if amount.isdigit():
            amount = int(amount)
            if amount > (total_bet - balance):
                balance =+ topup()
                print("now you have {balance}")
                return balance 
            else:
                while True :
                    print(f"you need {total_bet-balance} to continue")
                    addmoney = input("1 : topup\n2 : exit\n")
                    if addmoney.isdigit():
                        addmoney = int(addmoney)
                        if addmoney == 1:
                            balance += topup()
                            print(f"now you have {balance}")
                            return balance
                        elif addmoney == 2:
                            break
                        else:
                            print("please enter 1 or 2")
                    else:
                        print("please enter a number")
        else:
            print("please enter a number")

#Main Program
balance = topup()
balance = choice_topup(balance)
lines = get_number_of_lines()
bet = get_bet()
total_bet = bet*lines
if total_bet > balance:
    balance = minusbalance(balance, total_bet)
print(balance, lines, bet)
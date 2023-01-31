from random import *
RPS = [0,1,2]

while True:
    gamechoice = int(input("Tere! See on mäng kivi käärid paber. Missugune mängu režiim sa tahad? \n 1 - Bottiga \n 2 - Mängijaga \n 3 - stop\n"))
    if gamechoice == 1:
        uservalik = int(input("Vali: kivi(0) käärid(1) või paber(2):"))
        botivalik = choice(RPS)
        print(f"Boti valik on:{botivalik} \nUser valik on:{uservalik}")
        if uservalik == botivalik:
            print("Viit")
        elif uservalik ==0 and botivalik == 1 or uservalik ==1 and botivalik == 2 or uservalik ==2 and botivalik == 0:
            print("Win")
        else:
            print("defeat")
    elif gamechoice == 2:
        uservalik = (input("Vali: kivi(0) käärid(1) või paber(2):"))
        user2valik = (input("Vali: kivi(0) käärid(1) või paber(2):"))
        print(f"Boti valik on:{uservalik} \nUser valik on:{user2valik}")
        if uservalik == user2valik:
            print("Viit")
        elif uservalik ==0 and user2valik == 1 or uservalik ==1 and user2valik == 2 or uservalik ==2 and user2valik == 0:
            print("Win")
        else:
            print("defeat")
    elif gamechoice == 3:
        print("Head aega!")
        break
    else:
        ValueError
from random import *
import pickle
import os

RPS = [0,1,2]
players = []
playerwin = 0
plyerwinbot = 0
playerscore = 0
adminpass = 8585

storage_filename = "playerslist"
if not os.path.exists(storage_filename): 
    with open(storage_filename, "wb") as f: 
        pickle.dump(players, f)
else: 
    with open(storage_filename, "rb") as f:
        players = pickle.load(f)
 

playername = str(input("Tere. Mis on sinu nimi?"))


while True:
    playerscore = str(f"{playername} on {playerwin} win")
    
    gamechoice = int(input("See on mäng kivi käärid paber. Missugune mängu režiim sa tahad? \n 1 - Bottiga \n 2 - Mängijaga \n 3 - stop\n 4 - Vaata score\n 5 - vaata kõik players\n 6 - adminmenu\n"))
    if gamechoice == 1:
        uservalik = int(input("Vali: kivi(0) käärid(1) või paber(2):"))
        botivalik = choice(RPS)
        print(f"Boti valik on:{botivalik} \nUser valik on:{uservalik}")
        if uservalik == botivalik:
            print("Viit")
        elif uservalik ==0 and botivalik == 1 or uservalik ==1 and botivalik == 2 or uservalik ==2 and botivalik == 0:
            print("Win")
            playerwin = playerwin + 1
        else:
            print("defeat")
    elif gamechoice == 2:
        user3valik = int(input("Vali: kivi(0) käärid(1) või paber(2):"))
        user2valik = int(input("Vali: kivi(0) käärid(1) või paber(2):"))
        print(f"User valik on:{user3valik} \nUser 2 valik on:{user2valik}")
        if user3valik == user2valik:
            print("Viit")
        elif user3valik == 0 and user2valik == 1 or user3valik == 1 and user2valik == 2 or user3valik == 2 and user2valik == 0: #не работает, работает только виит и . Возможно надо исправить условие иф
            print("Win")
            playerwin = playerwin + 1
        else:
            print("defeat")
    elif gamechoice == 3:
        print("Head aega!")
        break
    elif gamechoice == 4:
        print(playerscore)
    elif gamechoice == 5:
        print(players)
        print("You will see your name only after you close program by pressing 3 in menu")
    elif gamechoice == 6:
        anspass = int(input("Enter password:"))
        if anspass == adminpass:
                while True:
                    adminchoice = int(input("Menu:\n 1 - delete user from plyerslist\n 2 - playerslist\n 3 - exit from admin menu\n"))
                    if adminchoice == 1:
                        removechoice = input("Enter player to remove:")
                        players.remove(removechoice)
                    elif adminchoice == 2:
                        print(players)
                    elif adminchoice == 3:
                        break
                    else:
                        print("Vale number")
                        ValueError
        else:
                print("Vale password")
                break
    else:
        print("Vale number")
        ValueError
players.append(playerscore)
with open(storage_filename, "wb") as f:
                pickle.dump(players, f)

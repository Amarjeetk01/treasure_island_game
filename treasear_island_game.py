treasure=('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
welcome='''
 _    _  ____  __    ___  _____  __  __  ____    ____  _____                                 
( \/\/ )( ___)(  )  / __)(  _  )(  \/  )( ___)  (_  _)(  _  )                                
 )    (  )__)  )(__( (__  )(_)(  )    (  )__)     )(   )(_)(                                 
(__/\__)(____)(____)\___)(_____)(_/\/\_)(____)   (__) (_____)                                
 ____  ____  ____    __    ___  __  __  ____  ____    ____  ___  __      __    _  _  ____    
(_  _)(  _ \( ___)  /__\  / __)(  )(  )(  _ \( ___)  (_  _)/ __)(  )    /__\  ( \( )(  _ \   
  )(   )   / )__)  /(__)\ \__ \ )(__)(  )   / )__)    _)(_ \__ \ )(__  /(__)\  )  (  )(_) )  
 (__) (_)\_)(____)(__)(__)(___/(______)(_)\_)(____)  (____)(___/(____)(__)(__)(_)\_)(____/
'''
over='''                                                       
   __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
  / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
  \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
   __/ |                                           
  |___/   
'''
ways='''
 _______ ______ ______ ___
/______/______/______/____
/______/______/______/____
'''
river='''
______________________________  /         \ 
 -          -         -        / '  '. ` ` \    -    -
      --                  --  /    '  . `   \    --
---            ---           /  '            \ ---
     ----               --- /       ' '` `    \  ----
-----         ----
'''
doors='''
 __________    __________    __________
|  __  __  |  |  __  __  |  |  __  __  |
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |__||__| |  | |__||__| |  | |__||__| |
|   BLUE ()|  |    RED ()|  | YELLOW ()|
|  __  __  |  |  __  __  |  |  __  __  |
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |__||__| |  | |__||__| |  | |__||__| |
|__________|  |__________|  |__________|
'''
print(welcome)
import random

print("Your mission to find Treasure")
select1=["left","right"]
ran_select1=random.choice(select1)
select2=["swim","wait"]
ran_select2=random.choice(select2)
select3=["Red","blue","yellow"]
ran_select3=random.choice(select3)
choice1=input(f"There are two paths ahead.\n{ways}\nType 'left' or 'right' to choose. ").lower()
if ran_select1==choice1:
    choice2=input(f"There is a river on the way ahead.\n{river}\nWhat would like to 'swim' or 'wait'. ").lower()
    if ran_select2==choice2:
        choice3=input(f"There are three doors on the way ahead.\n{doors}\nWhat would like to choice 'red' or 'blue' or 'yellow'. ").lower()
        if ran_select3==choice3:
            print(f"Congratulation you won.\nHere your treasure\n{treasure}")
        else:
            print(f"Burned by fire.\n{over}")
    else:
        print(f"Attack by trout.\n{over}")
else:
    print(f"You fall into a hole.\n {over}")
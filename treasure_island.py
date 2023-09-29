print('''
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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

trial1 = input('You are at the crossroad, where do you want to go? Type "left" or "right". ').lower()
if trial1 == "left":
  print("You passed and move to next location.")
  trial2 = input ('You are at the river, what should you do next? Type "swim" or "wait". ').lower()
  
  if trial2 == "wait":
    print("You succesfully passed the river and move to next location.")
    trial3 = input ('You approach the final door. There are four doors with different color. Type "red", "orange", "green" or "blue". ').lower()
    
    if trial3 == "red":
      print("You open and see the treasure. Congratulations!!!")
    elif trial3 == "orange":
      print("Fire started to spread through the room. Game over, try again.")
    elif (trial3 == "green"):
      print("You were overflowed with toxic liquids. Game over, try again.")
    elif (trial3 == "blue"):
      print("You encountered a ghost and it sucked your soul. Game over, try again.")
      
    else:
      print("You decided not to find the treasure and return.")
      
  else:
    print("You were attacked by a crocodiles. Game over, try again")
    
else:
  print("You fell into a hole. Game over, try again.")
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇


import random
from random import randint
print('Welcome to Avatar Showdown')
print('How to play:')
print('choose between 5 choices: fire, earth, water, air, and heal')
print('depending on what the computer chooses, there is a possibility of a critical')
print('first to 0 health wins')

player_health = 100
computer_health = 100
battle_continue = True
choice = ["fire","earth","water","air","heal"]

def critical_to_player():
    global player_health
    player_health -= 20
    print("Computer Critical -20 Points to you...")

def critical_to_computer():
    global computer_health
    computer_health -= 20
    print("Critical! -20 Points to Computer!")

def normal_attack():
    global player_health
    player_health -= 5
    global computer_health
    computer_health -= 5
    print("-5 Health Each")

def heal_to_player():
	global player_health
	player_health += random.randint(5,15)
	print("Heal successful")

def heal_to_computer():
	global computer_health
	computer_health += random.randint(5,15)
	print("opponent has healed ")

def determine_winner():
    global player_health
    if player_health <= 0:
        player_health = 0
        print ('Oh no! You vanished when we needed you most :(')

    global computer_health
    if computer_health <= 0:
        computer_health = 0
        print('You are the next avatar!')

def battle():
    computer = choice[randint(0,4)]

    player = input("Your Choice: ").lower()
    print("Computer Chose: " + computer)
    
    #both heal
    if player=="heal" and computer =="heal":
        heal_to_computer()
        heal_to_player()

    #draw
    elif player == computer:
        print("Draw")
        
    #earth choice
    elif player == "earth" and computer == "fire":
        normal_attack()
    elif player == "earth" and computer == "water":
        critical_to_computer()
    elif player == "earth" and computer == "air":
        critical_to_player()
        
    #fire choice
    elif player == "fire" and computer == "earth":
        normal_attack()
    elif player == "fire" and computer == "water":
        critical_to_player()
    elif player == "fire" and computer == "air":
        critical_to_computer()
        
    #water choice
    elif player == "water" and computer  == "earth":
        critical_to_player()
    elif player == "water" and computer == "fire":
        critical_to_computer()
    elif player == "water" and computer == "air":
        normal_attack()
        
    #air choice
    elif player == "air" and computer  == "earth":
        critical_to_computer() 
    elif player == "air" and computer == "fire":
        critical_to_player()
    elif player == "air" and computer == "water":
        normal_attack()
        
	#player heal
    elif player == "heal" and computer != "heal" and player_health<100:
	    heal_to_player()
	    normal_attack()

    #computer heal
    elif player != "heal" and computer == "heal" and computer_health<100:
	    heal_to_computer()
	    normal_attack()
    
    #end
    elif player == "end":
        exit()



#main algorithm
while battle_continue == True:
    battle()
    print("Player's current health is", player_health)
    print("Computer's current health is", computer_health)
    determine_winner()


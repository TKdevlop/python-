import random
import simplegui

COMPUTER=0
HUMAN=0
human_choice=""
computer_choice=""

def choice_to_number(choice):
    if choice=="rock":
       return 0
    elif choice=="papar":
        return 1
    elif choice=="scissors":
         return 2
print(choice_to_number(choice))

def number_to_choice(number):
    if number==0
       return="rock":
    elif number==1
       return="paper":
    elif number==2
       return="scissors":
print(number_to_choice(number))

def random_ch():
    return  random.choice(["rock","paper","scissros")]

def choice_result(ch_human,ch_computer):
    global COMPUTER_SCORE
    global HUMAN_SCORE

    def rock():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'rock'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)

def paper():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'paper'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)
 def scissors():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'scissors'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)

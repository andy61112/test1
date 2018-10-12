# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 10:00:43 2018

@author: Andy
"""
"""Docstring:
    A) Instruction:
    This game name is ultimate password. We will have two players:host and 
    contestant. As game start, host need to think one fixed number from 1~100 
    and contestant guess it. If contestant guessed corrected, 
    the game end and contestant win. Otherwise, host will specify the range between
    the number based on the contestant guess. If contestent couldn't answer correct
    after five round, host win.Game could end in round 1 or until round 100.
    
    For example:
        round 1 : Host has a number(22) in mind,contestant guess 50.
                  Then host will answer 1-50
        round 2:  Contestant guess again(26)          
                  The host will answer 1-26
        round 3:  Contestant guess again(20)          
                  The host will answer 20-26
        round 4:  Contestant guess again(23)
                  The host will answer 20-23
        round 5:  Contestant guess again()
                  The host will answer "Bingo!Congratulation"
                  Contestant win the game.
   """ 
from random import randint

def game_start():
    global host_name
    global contestant_name
    host_name = input("Input host name:\n")
    contestant_name = input("Input contestant name:\n")
print(f"Now the {host_name} and {contestant_name} are all set, let us begin our journey!")

lowest = 1
highest = 100
answer = randint(lowest, highest)

# Please keep guessing until you guess correctly
while True:
    print('Password is between'+str(lowest)+'and'+str(highest))
    guess = input()
    #Check if the content contestant enter is number
    try:
        guess = int(guess)#tranform string to integer
    except ValueError: # Require contestant to say the new number
        print(f"{host_name}:The thing you said is incorrect, please specify a number\n")
        continue
    #Check if the number contestant enter is between the largest and lowest number
    if guess <= lowest or guess >=highest:
        print(f"{host_name}:Please said the number between str(lowest) and str(highest)\n")
        continue
    # Check if the contestant guess correctly
    if guess == answer:
        print(f"{host_name}:{contestant_name}you win the game,congratulation!\n")
        break # jump out the loop if contestant guess correctly
    elif guess < answer:
        lowest = guess
    else:
        highest = guess
        


















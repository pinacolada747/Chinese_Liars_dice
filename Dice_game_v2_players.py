import random
import time
from Dice_game_v2_probability_test import *

global sleep_time
sleep_time = 0.1
#incorporating 1 to all count functions cs + c1*isonecalled
#tweak probability formulae
#when one's are called reverts to standard

#measure opponent tendency to bluff, after a number of games the bot should have data
#make tendency to bluff control the bots call aggressiveness
#invert human bluff tendency = how cautious they are
#increase bluff aggressiveness based on how cautious the human is


def call_probability(d1,p1,d2):
    a = random.randint(1,100)
    if a < p1:
        return d1
    else:
        return d2

class Player():
    def set_qty_call(self,qty_call1):
        self.current_qty = qty_call1

    def set_dice_call(self,dice_call1):
        self.dice_value_call = dice_call1
    def set_dice_list(self,list):
        self.dice_list = list

    def bluff(self,round): # computer bluffs at 30 percent chance at any round
        print('-' * 50)
        print(f'{self.name} calls bluff')
        print('-' * 50)
        if round.check_value() == True:  # checks current call against called values
            return True
        else:
            return False

class Human(Player):
    def __init__(self):
        self.name = input('Please enter your name: ')
        # self.total_funds = 1000
        self.call_history= []
        # self.current_bet = 0
        # self.score = 0

    def call(self,round):
        time.sleep(sleep_time)
        print('-'*50)
        print('Your call')
        while True: #called value validation, must comply with game rules,
            qty_call = int(input('Please enter quantity'))
            if qty_call > round.current_qty_call and qty_call  < 11:
                self.set_qty_call(qty_call)
                round.set_current_qty_call(qty_call) # sets the round's current value
                dice_call = int(input('Please enter dice number'))
                if dice_call < 7 and dice_call > 0:
                    self.set_dice_call(dice_call)
                    round.set_current_dice_call(dice_call)
                    round.show_current_call()
                    break
                else:
                    print('Please enter values between 1 and 6')
            elif qty_call == round.current_qty_call:
                self.set_qty_call(qty_call)
                round.set_current_qty_call(qty_call)
                dice_call = int(input('Please enter dice number'))
                if dice_call < 7 and dice_call > round.current_dice_call:
                    self.set_dice_call(dice_call)
                    round.set_current_dice_call(dice_call)
                    round.show_current_call()
                    break
                else:
                    print('Please enter values between', round.current_dice_call,'and 6')
            else:
                print('Please enter a number between', round.current_qty_call, 'and 10')

    def bluff_or_call(self,round):
        while True:
            a = input('Enter b to call bluff or c to make call')
            if a == 'b':
                return True
            elif a == 'c':
                return False
            else:
                print('Please enter b or c')


class Computer_drunk(Player):
    def __init__(self):
        self.name = 'Computer_drunk'
        # self.total_funds = 1000
        self.call_history= []
        # self.score = 0

    def call(self, round):
        time.sleep(sleep_time)
        print('-' * 50)
        if round.current_dice_call < 6:
            if round.current_qty_call < 10: # can b
                qty_call = random.randint(round.current_qty_call, 10)
                if qty_call > round.current_qty_call:
                    self.set_qty_call(qty_call)
                    round.set_current_qty_call(qty_call)
                    dice_call = random.randint(1, 6)
                    self.set_dice_call(dice_call)
                    round.set_current_dice_call(dice_call)
                else: #if the same quantity is called
                    self.set_qty_call(qty_call)
                    round.set_current_qty_call(qty_call)
                    dice_call = random.randint(round.current_dice_call+1, 6)
                    self.set_dice_call(dice_call)
                    round.set_current_dice_call(dice_call)
        else: # if current dice_call = 6
            qty_call = round.current_qty_call + 1
            round.set_current_qty_call(qty_call)
            self.set_qty_call(qty_call)
            dice_call = random.randint(1,6)
            self.set_dice_call(dice_call)
            round.set_current_dice_call(dice_call)
        time.sleep(sleep_time)
        print('-' * 50)
        print('Drunk computer has called', self.current_qty, 'of', self.dice_value_call)
        round.show_current_call()

    def bluff_or_call(self,round):
        if round.current_qty_call > 9:
            return True
        else:
            bluff_chance = random.randint(0,100)
            if bluff_chance < 30:
                return True
            else:
                return False

class Computer_sensible(Player): #computer calls the next biggest value or dice number instead of spastic
    def __init__(self):
        self.name = 'Computer_sensible'
        # self.total_funds = 1000
        self.call_history = []

    def call(self, round):
        time.sleep(sleep_time)
        print('-' * 50)
        if round.current_dice_call < 6:
            if round.current_qty_call < 10:
                qty_call = random.randint(round.current_qty_call, round.current_qty_call+1)
                if qty_call > round.current_qty_call:
                    self.set_qty_call(qty_call)
                    round.set_current_qty_call(qty_call)
                    dice_call = random.randint(1, 6)
                    self.set_dice_call(dice_call)
                    round.set_current_dice_call(dice_call)
                else: #if the same quantity is called
                    self.set_qty_call(qty_call)
                    round.set_current_qty_call(qty_call)
                    dice_call = random.randint(round.current_dice_call+1, 6)
                    self.set_dice_call(dice_call)
                    round.set_current_dice_call(dice_call)
        else: # if current dice_call = 6
            qty_call = round.current_qty_call + 1
            round.set_current_qty_call(qty_call)
            self.set_qty_call(qty_call)
            dice_call = random.randint(1,6)
            self.set_dice_call(dice_call)
            round.set_current_dice_call(dice_call)
        time.sleep(sleep_time)
        print('-' * 50)
        print('Sensible computer has called', self.current_qty, 'of', self.dice_value_call)
        round.show_current_call()

    def bluff_or_call(self,round):
        if round.current_qty_call > 9:
            return True
        else:
            bluff_chance = random.randint(0,100)
            if bluff_chance < 30:
                return True
            else:
                return False

class Computer_omni(Player): #computer calls the next biggest value or dice number instead of spastic
    def __init__(self):
        self.name = 'Computer_omni'
        # self.total_funds = 1000
        self.call_history = []

    def set_qty_call(self, qty_call1):
        self.current_qty = qty_call1

    def set_dice_call(self, dice_call1):
        self.dice_value_call = dice_call1

    def call(self, round):
        time.sleep(sleep_time)
        print('-' * 50)
        if round.current_dice_call < 6:
        # if round.current_qty_call < 10:
            qty_call = random.randint(round.current_qty_call, round.current_qty_call+1)
            if qty_call > round.current_qty_call:
                self.set_qty_call(qty_call)
                round.set_current_qty_call(qty_call)
                dice_call = random.randint(1, 6)
                self.set_dice_call(dice_call)
                round.set_current_dice_call(dice_call)
            else: #if the same quantity is called
                self.set_qty_call(qty_call)
                round.set_current_qty_call(qty_call)
                dice_call = random.randint(round.current_dice_call+1, 6)
                self.set_dice_call(dice_call)
                round.set_current_dice_call(dice_call)
        else: # if current dice_call = 6
            qty_call = round.current_qty_call + 1
            round.set_current_qty_call(qty_call)
            self.set_qty_call(qty_call)
            dice_call = random.randint(1,6)
            self.set_dice_call(dice_call)
            round.set_current_dice_call(dice_call)
        time.sleep(sleep_time)
        print('-' * 50)
        print(self.name, ' has called', self.current_qty, 'of', self.dice_value_call)
        round.show_current_call()

    def bluff_or_call(self,round): # computer bluffs by cheating
        if round.current_qty_call > 9:
            return True
        else:
            s3 = lambda a, b: a.count(int(b))
            s4 = s3(round.full_list, round.current_dice_call)
            if s4 < round.current_qty_call:
                return True
            else:
                return False

class Computer_intelligent(Player): #computer calls the next biggest value or dice number instead of spastic
    def __init__(self):
        self.name = 'Computer_intelligent'
        # self.total_funds = 1000
        self.dice_list = []
        self.bluff_call_aggressiveness = 30
    def call(self, round):
        time.sleep(sleep_time)
        print('-' * 50)
        if round.current_dice_call < 6:
            if round.current_qty_call < 10:
                qty_call = random.randint(round.current_qty_call, round.current_qty_call+1)
                if qty_call > round.current_qty_call:
                    self.set_qty_call(qty_call)
                    round.set_current_qty_call(qty_call)
                    dice_call = random.randint(1, 6)
                    self.set_dice_call(dice_call)
                    round.set_current_dice_call(dice_call)
                else: #if the same quantity is called
                    self.set_qty_call(qty_call)
                    round.set_current_qty_call(qty_call)
                    dice_call = random.randint(round.current_dice_call+1, 6)
                    self.set_dice_call(dice_call)
                    round.set_current_dice_call(dice_call)
        else: # if current dice_call = 6
            qty_call = round.current_qty_call + 1
            round.set_current_qty_call(qty_call)
            self.set_qty_call(qty_call)
            dice_call = random.randint(1,6)
            self.set_dice_call(dice_call)
            round.set_current_dice_call(dice_call)
        time.sleep(sleep_time)
        print('-' * 50)
        print(self.name, ' has called', self.current_qty, 'of', self.dice_value_call)
        round.show_current_call()

    def bluff_or_call(self, round1):
        if round1.current_qty_call > 9:
            return True
        else:
            # if (int(round(calculate_probability(self.dice_list,round1.current_qty_call,round1.current_dice_call),2)*100)) < self.bluff_call_aggressiveness:
            if calculate_probability(self.dice_list, round1.current_qty_call, round1.current_dice_call) < self.bluff_call_aggressiveness:
                return True
            else:
                return False

class Computer_intelligent1(Computer_intelligent):
    def __init__(self):
        self.name = 'Computer_intelligent1'
        # self.total_funds = 1000
        self.dice_list = []
        self.bluff_call_aggressiveness = 50

class Computer_intelligent2(Computer_intelligent):
    def __init__(self):
        self.name = 'Computer_intelligent2'
        # self.total_funds = 1000
        self.dice_list = []
        self.bluff_call_aggressiveness = 10

class Computer_intelligent4(Player): #computer calls the next biggest value or dice number instead of spastic
    def __init__(self):
        self.name = 'Computer_intelligent'
        # self.total_funds = 1000
        self.dice_list = []
        self.bluff_call_aggressiveness = 30

    def call(self, round):
        time.sleep(sleep_time)
        print('-' * 50)
        if round.current_dice_call < 6:
            if round.current_qty_call < 10:
                qty_call = random.randint(round.current_qty_call, round.current_qty_call+1)
                if qty_call > round.current_qty_call:
                    self.set_qty_call(qty_call)
                    round.set_current_qty_call(qty_call)
                    dice_call = random.randint(1, 6)
                    self.set_dice_call(dice_call)
                    round.set_current_dice_call(dice_call)
                else: #if the same quantity is called
                    self.set_qty_call(qty_call)
                    round.set_current_qty_call(qty_call)
                    dice_call = random.randint(round.current_dice_call+1, 6)
                    self.set_dice_call(dice_call)
                    round.set_current_dice_call(dice_call)
        else: # if current dice_call = 6
            qty_call = round.current_qty_call + 1
            round.set_current_qty_call(qty_call)
            self.set_qty_call(qty_call)
            dice_call = random.randint(1,6)
            self.set_dice_call(dice_call)
            round.set_current_dice_call(dice_call)
        time.sleep(sleep_time)
        print('-' * 50)
        print(self.name, ' has called', self.current_qty, 'of', self.dice_value_call)
        round.show_current_call()

    def bluff_or_call(self, round1):
        if round1.current_qty_call > 9:
            return True
        else:
            if calculate_probability(self.dice_list,round1.current_qty_call,round1.current_dice_call) < self.bluff_call_aggressiveness:
                return True
            else:
                return False


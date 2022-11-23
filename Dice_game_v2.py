import random
import time
from Dice_game_v2_players import *
from openpyxl import Workbook, load_workbook
from datetime import datetime

# integration of probability - reference to dices in cup? p1 v p2
# automate workbook creating
# first stage analytics - win rate

#need to force call bluff at dice quantity 10
global sleep_time
sleep_time = 0.1
global excel_path
excel_path = "C:/Users/user/Desktop/Dice_output5.xlsx"


def print_ascii(fn):
    f = open(fn,'r')
    print(''.join([g for g in f]))

print_ascii('liars_dice.txt')

def print_bracket(string):
    time.sleep(sleep_time)
    print('-'*50)
    print(string)
    print('-'*50)

def iterate(list1,list2):
    for a in list1:
        list2.append(a)

class Round():
    def __init__(self,):
        self.current_qty_call = 1 #the most recent dice call
        self.current_dice_call = 1
        self.p1_list = [] # for storage
        self.p2_list = []
        for i in range(5):
            a = random.randint(1, 6)
            self.p1_list.append(a) # shakes the dice cup

        for i in range(5):
            b = random.randint(1, 6)
            self.p2_list.append(b) # computer  shakes the dice cup
        # print('The computers dices are',self.computer_list)
        self.full_list = self.p1_list + self.p2_list


    def reveal_dice(self):
        print('-'*50)
        print('your dices are', self.p1_list)
        print('the computers dices are', self.p2_list)
        print('-'*50)

    def set_current_call(self,current_qty_call1, current_dice_call1):
        self.current_dice_call = current_dice_call1
        self.current_qty_call = current_qty_call1

    def set_current_dice_call(self,current_dice_call1):
        self.current_dice_call = current_dice_call1

    def set_current_qty_call(self,current_qty_call1):
        self.current_qty_call = current_qty_call1

    def show_current_call(self):
        time.sleep(sleep_time)
        print('-'*50)
        print('The current call is ', end = '')
        print(self.current_qty_call,'of',self.current_dice_call)

    def check_value(self):
        print(self.full_list)
        s3 = lambda a,b : a.count(int(b))
        s4 = s3(self.full_list,self.current_dice_call)
        print('there are a total of',s4, 'of', self.current_dice_call)
        if int(s4) > self.current_qty_call or int(s4) == int(self.current_qty_call):
            return True
        else:
            return False


class Game: #mainly the score counter and to include rounds
    global excel_path
    def __init__(self):

        self.p1_score = 0
        self.p2_score = 0
        self.p1 = 0
        self.p2 = 0
        self.game_mode = 0
        print_bracket('Welcome to the game of dice:')
        while self.p1 == 0:
            self.game_mode = input('Please input c for CVC or p for PVC: ')
            if self.game_mode == 'c':
                a = random.randint(1, 100)
                if a < 33:
                    self.p1 = Computer_intelligent1()
                elif a > 66:
                    self.p1 = Computer_intelligent1()
                else:
                    self.p1 = Computer_intelligent1()
            elif self.game_mode == 'p':
                self.p1 = Human()
            else:
                print('Please input c for CVC or p for PVC: ')

        self.round_number = 0
        while self.round_number < 500:
            self.round_number += 1
            print('round',self.round_number,'starts')
            self.start_round()

    def print_score(self):
        time.sleep(sleep_time)
        print_bracket(self.p1.name+' v.s '+self.p2.name)
        print(self.p1_score, ' ' * 11, self.p2_score)

    def save(self):
        iterate(self.p_moves,self.output_list)
        self.ws.append(self.output_list)
        self.wb.save(excel_path)

    def p1_lost(self):
        now = datetime.now()
        print_bracket('P1 have lost')
        self.p2_score += 1
        self.p_moves.append('p1_bl')
        self.output_list.insert(0, str(now))
        self.output_list.insert(1, self.p2.name)
        self.output_list.insert(2, self.turns_played)
        self.print_score()
        self.turn = 4
        self.save()

    def p2_lost(self):
        now = datetime.now()
        print_bracket('P2 have lost')
        self.p1_score += 1
        self.p_moves.append('p2_bl')
        self.output_list.insert(0,str(now))
        self.output_list.insert(1,self.p1.name)
        self.output_list.insert(2, self.turns_played)
        self.print_score()
        self.turn = 4
        self.save()
    def p1_win(self):
        now = datetime.now()
        print_bracket('P1 have won')
        self.p1_score += 1
        self.p_moves.append('p1_bw')
        self.output_list.insert(0,str(now))
        self.output_list.insert(1,self.p1.name)
        self.output_list.insert(2, self.turns_played)
        self.print_score()
        self.turn = 4
        self.save()
    def p2_win(self):
        now = datetime.now()
        print_bracket('P2 have won')
        self.p2_score += 1
        self.p_moves.append('p2_bw')
        self.output_list.insert(0,str(now))
        self.output_list.insert(1,self.p2.name)
        self.output_list.insert(2,self.turns_played)
        self.print_score()
        self.turn = 4
        self.save()

    def append_call(self):
        self.p_moves.append(self.round1.current_qty_call)
        self.p_moves.append(self.round1.current_dice_call)

    def start_round(self):
        self.wb = load_workbook(excel_path)
        self.ws = self.wb['Dice_game_output']
        self.output_list = []
        self.p_moves = []
        a = random.randint(1, 100)
        self.turn = 3
        self.turns_played = 0
        if a < 33:
            # print_bracket('You are playing against computer sensible')
            self.p2 = Computer_intelligent1()
        elif a > 66:
            # print_bracket('You are playing against computer omni')
            self.p2 = Computer_intelligent1()
        else:
            # print_bracket('You are playing drunk computer')
            self.p2 = Computer_intelligent1()

        time.sleep(sleep_time)

        self.round1 = Round()
        # round starts
        self.output_list.append(self.p1.name) # player name to output list
        self.output_list.append(self.p2.name) # computer name to output list

        iterate(self.round1.p1_list, self.output_list)
        iterate(self.round1.p2_list, self.output_list)
        self.p1.set_dice_list(self.round1.p1_list)
        self.p2.set_dice_list(self.round1.p2_list)
        while self.turn == 3:
            print('your dice is :',self.p1.dice_list)
            self.p1.call(self.round1)
            self.turns_played += 1
            self.append_call()
            self.turn = 2
        while self.turn < 3:
            if self.turn == 2:
                print('your dice is :',self.p1.dice_list)
                if self.p2.bluff_or_call(self.round1) == True:
                    if self.p2.bluff(self.round1) == True:
                        self.turns_played += 1
                        self.p2_lost()
                    else:
                        self.turns_played += 1
                        self.p2_win()
                else:
                    self.p2.call(self.round1)
                    self.turns_played += 1
                    self.append_call()
                    self.turn = 1
            if self.turn == 1:
                print('your dice is :',self.p1.dice_list)
                if self.p1.bluff_or_call(self.round1) == True:
                    if self.p1.bluff(self.round1) == True:
                        self.turns_played += 1
                        self.p1_lost()
                    else:
                        self.turns_played += 1
                        self.p1_win()
                else:
                    self.p1.call(self.round1)
                    self.turns_played += 1
                    self.append_call()
                    self.turn = 2

def main():
    game1 = Game()
if __name__ == '__main__':
    main()

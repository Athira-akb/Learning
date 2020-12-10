#attack(low,high); damage; magic(thunder+fire+water)(cost,damage);hp ; mp; action

import random

class bcolors:
    HEADER ='\033[95m'
    OKBLUE ='\033[94m'
    OKGREEN ='\033[92m'
    WARNING ='\033[93m'
    FAIL ='\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:

    def __init__(self,hp,mp,atk,defn,magic):
        self.hp_max = hp    #to save the max value
        self.hp = hp
        self.mp_max = mp
        self.mp = mp
        self.atkl = atk - 5
        self.atkh = atk + 5
        self.defn = defn
        self.magic = magic
        self.action = ["action","magic"]

    #Generate Attack Damage
    def generate_damege(self):
        return random.randrange(self.atkl,self.atkh)

    #Generate Spell Damage
    def generate_spell_damege(self,i):
        mgl = self.magic[i]["Damage"] - 5   #low
        mgh = self.magic[i]["Damage"] + 5   #high
        return random.randrange(mgl,mgh)

    #Take damage
    def take_damage(self,Damage):
        self.hp -= Damage
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return  self.hp

    def get_max_hp(self):
        return self.hp_max

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.mp_max

    def reduce_mp(self,cost):
        self.mp -= cost

    def get_spell_name(self,i):
        return  self.magic[i]["Name"]

    def get_spell_mp_cost(self,i):
        return  self.magic[i]["Cost"]

    #choice
    def choose_action(self):
        i = 1
        print ("Action ")
        for item in self.actions:
            print (str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i=1
        for spell in self.magic:
            print(str(i) + ":", spell["Name"],"(Cost :", str(spell["mp"] + ")"))




















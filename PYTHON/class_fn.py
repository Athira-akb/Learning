'''class Enemy :
    atkl = 60
    atkh = 80

    def get_atk(self):
        print ("Low attack is ",self.atkl)
        print ("High attack is",self.atkh)

enemy1 = Enemy()        #calling class
enemy1.get_atk()        #calling function'''

class Enemy():
    hp = 200

    def __init__(self,atkl,atkh):
        self.atkl = atkl
        self.atkh = atkh


    def atk(self):
        print ("Low attack is ", self.atkl)
        print ("High attack is ", self.atkh)

enemy1 = Enemy(40,49)
enemy1.atk()

enemy2 = Enemy(50,59)
enemy2.atk()


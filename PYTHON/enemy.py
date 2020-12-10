class Enemy():
    def __init__(self,atkl,atkh):
        self.max_hp = atkh
        self.min_hp = atkl

    def get_atk(self):
        return self.max_hp
        return self.min_hp
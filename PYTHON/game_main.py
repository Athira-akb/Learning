from CLASS.game import Person

magic =[
    {"Name": "Fire", "Cost": 20, "Damage": 55},
    {"Name": "Water", "Cost":15, "Damage":70},
    {"Name": "Thunder", "Cost":25, "Damage":45}
]

#Player1
print ("****Player 1 : Nairobi**** ")
player = Person(460,50,45,34,magic)    #hp,mp,atk,def,magic
enemy = Person(1250,70,60,25,magic)

running = True
i=0

while running:
        


'''damage = player1.generate_damege()
print("Attack damage ",damage)
print ("Spell attack damage ",player1.generate_spell_damege(0))
print("HP after damage is ",player1.take_damage(0))'''

'''print("\n")

#Player2
print("****Player 2 : Hiroshi****")
player2 = Person(450,70,95,30,magic)    #hp,mp,atk,def,magic
damage = player2.generate_damege()
print("Attack damage :",damage)
print("Spell attack damage :",player2.generate_spell_damege(1))'''
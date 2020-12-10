import random

#define variables
playerhp = 260
enemyhp = 60
enemyattack = 80


while playerhp > 0 :
    damage = random.randrange(enemyhp,enemyattack)
    playerhp = playerhp - damage

    if playerhp <= 30:
        playerhp = 30

    print ("Enemy strikes for ",damage," damage points. Current HP is ",playerhp)

    if playerhp ==30 :
        print ("You have low health. You have been teleported to the nearest inn")
        break
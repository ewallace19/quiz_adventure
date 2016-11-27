
# An adventure game

# An adventure
name = ""
hp = 1
boss_hp = 10000
enemy_hp = 30
    
from random import randint
def healthbar():
    print("_________")
    print("hp ", hp)
    print("_________")

def deathcheck():
    if hp < 1:
        quit()

def bosshpbar():
    print("__________________")
    print("boss hp", boss_hp)
    print("__________________")


    
def class_setup():
    global name
    global hp
    print("What fate do you choose?")
    print("a. Mercenary( the most ordinary class, medium hp and medium damage)")
    print("b. Cleric( has a critical strike chance of 50%)")
    print("c. Deprived (has the most hp, but has the least attack damage)")
    action = input("Pick your class: ")
    if action == "a":
        hp = 160
        name = "Mercenary"
    elif action == "b":
        hp = 100
        name = "Cleric"
    elif action == "c":
        hp = 250
        name = "Deprived"
    room1()
def room1():
    global name
    global hp

    healthbar()
    
    print("You're on a tower at the edge of a castle's perimeters, what do you do?")
    print("a. climb down the stairs")
    print("b. stay where you are")
    print("c. look for another way")
    action = input("Pick your action: ")
    if action.lower() == "a":
        room2()
    elif action.lower() == "c":
        print("There is no other way. You wasted your time. Well done")
        room1()
    elif action.lower() == "b":
        room1()
def room2():
    global name
    global hp

    healthbar()

    print("You encounter a sleeping, onion man.What do you do?")
    print("a. wake him up")
    print("b. kill him")
    print("c. leave him")
    action = input("Pick your action: ")
    if action.lower() == "a":
        print("""Why hello there ashen one, i wasnt expecting you so soom, i cant help you currently due to my armour being stuck in the floor. oh well, may thou'st peace discover.""")
        room3()
    elif action.lower() == "b":
        print("I'm not letting you do that, you monster!")
        room2()
    elif action.lower() == "c":
        room3()
def room3():
    global name
    global hp
    global enemy_hp
    global random

    healthbar()
    
    print("You find a living suit of armour wielding a sword. what do you do?")
    print("a. attack")
    print("b. try to parry it")
    print("c. defend")
    action = input("pick your action: ")
    if action.lower() == "b":
        random = randint(0, 3)
        if random < 2:
            print("you successfully parried the enemy, well done")
            room4()
        elif random >= 2:
            print("you failed to parry the enemy, you took damage")
            hp -= 20
            room3()
    if action.lower() == "a":
        print("the enemy took damage")
        room3()
        if name == "Mercenary":
            enemy_hp -= 20

        elif name == "Cleric":
            random = randint(0, 1)
            if random == 1:
                enemy_hp -= 15

            elif random == 0:
                enemy_hp -= 30

    elif action.lower() == "c":
            print("you rolled")

    if enemy_hp > 0:
            room3()

    elif enemy_hp < 0:
            room4()

    deathcheck()
    
def room4():
    global name
    global hp
    global enemy_hp
    global random

    healthbar()
    
    print("you find a fork in your path, there is a tower upstairs. on the other path, there is a path which is guarded by a skeleton but has a clear path behind it. what do you do?")
    print("a. go up the stairs")
    print("b. go down the pathway")
    action = input("pick your answer: ")
    if action.lower() == "a":
        room5a()

    elif action.lower() == "b":
        room5b()
def room5a():
    global name
    global hp
    global enemy_hp
    global random

    healthbar()

    
    print("a dragon lands on top of the tower, it swoops down at you, you took damage but you can still escape. what do you do?")
    print("a. run into the gate infront of you")
    print("b.  look for another gate")
    print("c. turn back")
    action = input("Pick your action: ")
    if action.lower() == "a":
        print("you escaped the dragon just in time")
        hp -= 30
        room6()

    elif action.lower() == "b":
        print("There is no other gate, the dragon crushes you with its foot")
        quit()

    elif action.lower() == "c":
        print("The dragon saw you run away and chased you")
        quit()
    
def room5b():
    global name
    global hp
    global enemy_hp
    global random

    healthbar()
    
    enemy_hp = 40
    print("As you progress down the path,you come across an archer skeleton. What do you do?")
    print("a. attack")
    print("b. try to parry it")
    print("c. defend")
    action = input("pick your action: ")
    if action == "b":
        random = randint(0, 3)
        if random < 2:
            print("you successfully parried the enemy, well done")
            room6()
        elif random >= 2:
            print("you failed to parry the enemy, you took damage")
            hp -= 40
            room5b()
    if action == "a":
        print("the enemy took damage")
        room5b()
        if action == "a":
            if name == "Mercenary":
                enemy_hp -= 20

            elif name == "Cleric":
                random = randint(0, 1)
                if random == 1:
                    enemy_hp -= 15

                elif random == 0:
                    enemy_hp -= 30

            else:
                emeny_hp -= 5
    deathcheck()
    

    if enemy_hp < 1:
        room8()
    elif enemy_hp > 0:
        room5b
    

def room6():
    global name
    global hp
    global enemy_hp
    global random

    healthbar()
    
    print("You escape the dragon and entered the tower, there are 2 sets of stairs,which do you pick?")
    print("a. up the stairs")
    print("b. down the stairs")
    print("c. start attacking walls incase they are fake")
    action = input("Pick your action: ")
    if action == "a":
        print("You found a bonfire, your hp is fully restored")
        if name == "Mercenary":
            hp = 160
        elif name == "Cleric":
            hp = 100
        else:
            hp = 200

        room7()
            
    elif action == "b":
        room7()
    elif action == "c":
        print("Well that was a waste of your time, why do you keep doing this to yourself?!")
        room6()


def room7():
    global name
    global hp
    global enemy_hp
    global random

    healthbar()
    
    
    print("You walk down the stairs to see a door loading to a roof, there are enemy's outside the door but it dosent seem that they care. What do you do?")
    print("a. run past the enemys and down the ladder to escape")
    print("b. run past the enemys and jump off the roof")
    print("c. be scared and don't leave EVER")
    action = input("Pick your action: ")
    if action == "a":
        room8()
    elif action == "b":
        print("You hurt yourself, but it was worth it. or was it?")
        hp -= 15
        room9()
    elif action == "c":
        room7()

def room8():
    global name
    global hp
    global enemy_hp
    global random

    healthbar()
    
    print("You end up at the bottom of a ladder, you can either take more damage and end up in what looks like an arena, or you can go the long way through a church. What do you do?")
    print("a. skip to the arena")
    print("b. go the long way")
    print("c. PRAISE THE SUN")
    action = input("Pick your action: ")
    if action == "a":
        hp -= 40
        bossroom()

    elif action == "b":
        room9()

    elif action == "c":
        print("Just for doing that you automatically win life. But this is not a super mario game where you can win in 10 mins, no you need to continue. but now you have more health than usual.")
        hp = 300
        room8()
    

def room9():
    global name
    global hp
    global enemy_hp
    global random

    healthbar()
    
    print("You encounter a shrine handmaiden called Emma, She gives you the small lothric banner and makes you part of her covenant. Do you accept this?")
    print("a.yes")
    print("b. no")
    print("c. kill her")
    action = input("Pick your action: ")
    if action == "a":
        print("you are now part of the way of blue covenant.")
        bossroom()
    elif action == "b":
        print("you leave Emma in her church to rot away")
        bossroom()
    elif action == "c":
        print("This triggers a very large enemy to show up and kills you in 1 hit")
        quit()

def bossroom():
    global name
    global hp
    global boss_hp
    global random
    boss_hp = 10000

    healthbar(), bosshpbar()
    print("As you enter the boss room, you come across a weapon on the floor called the storm ruler, however as you go to pick it up, a giant follows you in.; are you ready?")
    print("a. charge your weapon")
    print("b. defend")
    action = input("pick your action: ")

    

    if action == "a":
        print("you charged your weapon, then you went for an attack, you did 0.2 of the boss' hp")
        boss_hp -= 2000
    elif action == "b":
        random = randint(0, 1)
        if random == 1:
            print("you dodged his attack and did some damage")
            boss_hp -= 1000
        else:
            print("You dodged an attack, but he hit again and you failed to dodge")
    if boss_hp < 1:
        print("well done, you have beat yhorm the giant, contgrats, you win! ")

    if boss_hp > 0:
        bossroom()
                
        
        
        
# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    class_setup()

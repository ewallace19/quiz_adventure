
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


    
def class_setup():
    global name
    global hp
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
        print("""Why hello there ashen one, i wasn't expecting you this soon" said Siegward, knight of Catarina""")
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
def room4():
    global hp

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
    print("a dragon lands on top of the tower, it swoops down at you, you took damage but you can still escape. what do you do?")
    print("a. run  into the gate infront of you")
    print("b.  look for another gate")
    print("c. turn back")
    action = input("Pick your action: ")
    if action.lower() == "a":
        print("you escaped the dragon just in time")
        room6()

    elif action.lower() == "b":
        print("There is no other gate, the dragon crushes you with its foot")
        quit()
    
def room5b():
    global name
    global hp
    global enemy_hp
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

    if enemy_hp < 1:
        room8()
    elif enemy_hp > 0:
        room5b
    

def room6():
    global name
    global hp
    print("You escape the dragon and entered the tower, there are 2 sets of stairs,which do you pick?")
    print("a. up the stairs")
    print("b. down the stairs")
    print("c. start attacking walls incase they are fake")
    action = input("Pick your action: ")
    if action == "a":
        print("You found a bonfire, your hp if fully restored")
        room7()
    elif action == "b":
        room7()
    elif action == "c":
        print("Well that was a waste of your time, why do you keep doing this to yourself?!")


def room7():
    global name
    global hp
    print("You walk dwon the stairs to see a door loading to a roof, there are enemy's outside the door but it dosent seem that they care. What do you do?")
    print("a. run past the enemys and down the ladder to escape")
    print("b. run past the enemys and jumo off the roof")
    print("c. ")
    action = input("Pick your action: ")

def room8():
    global name
    global hp
    print("")
    print("a. ")
    print("b. ")
    print("c. ")
    action = input("Pick your action: ")

def room9():
    global name
    global hp
    print("")
    print("a. ")
    print("b. ")
    print("c. ")
    action = input("Pick your action: ")

def bossroom():
    print("njaenievbbr")
    









# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    class_setup()

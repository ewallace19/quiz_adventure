# Our quiz!
score = 100
name = ""
def quiz():

    name = input("Enter Name: ")

    question1()
    question2()
    question3()
    question4()
    question5()
    question6()
    question7()
    question8()
    question9()
    question10()
    #question11()
    
    

def question1():
    global name
    global score
    print("You start at 100 points,you need 0 to win. This quiz is about Dark souls 3")

    print("Question 1")
    print("What is the name of the 1st boss? (The boss in Cemetery of Ash)")
    print("a. Ludex Gundyr")
    print("b. Crystal Sage")
    print("c. High Lord Wolnir")
    answer1 = input("Pick your answer: ")
    if answer1.lower() == ("a"):
        score -= 10
    else:
        pass

def question2():
    global name
    global score
    
    print("Question 2")
    print("Who do you give the transposing kiln to in firelink shrine?")
    print("a. Aldrich devourer of gods")
    print("b. Lothric, younger prince")
    print("c. Ludleth the exiled")
    answer2 = input("pick your answer: ")
    if answer2.lower() == "c":
        score -= 10
    else:
        pass

def question3():
    global name
    global score
    
    print("Question 3")
    print("How many optional bosses are they in the game?")
    print("a. 2")
    print("b. 6")
    print("c. 1")
    answer3 = input("pick your answer: ")
    if answer3.lower() == "b":
        score -= 10
    else:
        pass
    
def question4():
    global name
    global score
    
    print("Question 4")
    print("Who do you fight in kiln of the first flame?")
    print("a. Yhorm the giant")
    print("b. Soul of cinder")
    print("c. Nameless king")
    answer4 = input("pick your answer: ")
    if answer4.lower() == "b":
        score -= 10
    else:
        pass
    
def question5():
    global name
    global score
    
    print("Question 5")
    print("What effect does the Farron keep swamp give?")
    print("a. curse")
    print("b. bleed")
    print("c. poison")
    answer5 = input("Pick your answer: ")
    if answer5.lower() == "c":
        score -= 10
    else:
        pass

def question6():
    global name
    global score

    print("Question 6")
    print("Which emote do you get after killing ocieros, the consumed king?")
    print("a. By my sword")
    print("b. Path of the dragon")
    print("c. curl up")
    answer6 = input("Pick your answer: ")
    if answer6.lower() == "b":
        score -= 10
    else:
        pass

def question7():
    global name
    global score

    print("Question 7")
    print("Which boss has its only weakness in its boss room?")
    print("a. Dancer of the Boreal valley ")
    print("b. Lothric, younger prince and Lorien, older prince")
    print("c. Yhorm the giant")
    answer7 = input("Pick your answer: ")
    if answer7.lower() == "c":
        score -= 10
    else:
        pass

def question8():
    global name
    global score

    print("Question 8")
    print("Who is the last Lord of Cinder you fight?")
    print("a. Abyss watchers")
    print("b. Lothric, younger prince and Lorien, older prince")
    print("c. Aldrich, devourer of gods")
    answer8 = input("Pick your answer: ")
    if answer8.lower() == "b":
        score -= 10
    else:
        pass

def question9():
    global name
    global score

    print("Question 9")
    print("Which NPC do you summon in order to get both twinkling dragon stones?")
    print("a. Hawkwood the deserter")
    print("b. Black Hand gotthard")
    print("c. Ringfinger Leonhard")
    answer9 = input("Pick your answer: ")
    if answer9.lower() == "c":
        score -= 10
    else:
        pass

def question10():
    global name
    global score

    print("Question 10")
    print("How many katanas are they in the game?")
    print("a. 6")
    print("b. 7")
    print("c. 8")
    answer10 = input("Pick your answer: ")
    if answer10.lower() == "b":
        score -= 10
    else:
        pass

    if score == 0:
        bonus_question()
        print("Well done,", name" you have got all of the questions correct, you now get to answer a bonus question.")

def bonus_question():
    print("Which boss is closest to the 'Great belfry' bonfire?")
    print("a. NAmeless king")
    print("b. Soul of Cinder")
    print("c. Gwyndolin dark sun")
    if bonus_answer == 
    

        





# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()

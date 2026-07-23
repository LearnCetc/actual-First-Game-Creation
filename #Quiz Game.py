#Quiz Game
import random

t = 1
Sign = "o"
Sign_Loop_Value = 0
global Points
Points = 0
Difficulty = -1

print("Game by LearnCetc\n")

while Sign_Loop_Value == 0: #Used to make the code loop until a valid letter has been writen
    Sign = input("\nDo you want to do\nAddition (A)\nSubstraction (S)\nMultiplication (M)\nDivision (D)\n: ")
    Sign = Sign.upper()

    if Sign == "A":
        Sign = "+"
        Sign_Loop_Value += 1

    if Sign == "S":
        Sign = "-"
        Sign_Loop_Value += 1

    if Sign == "M":
        Sign = "*"
        Sign_Loop_Value += 1

    if Sign == "D":
        Sign = "/"
        print(f"if the answer contains infinte decimals round it and then write it with {Difficulty} decimals")
        Sign_Loop_Value += 1

while t == 1:
    Difficulty_Mode  = input("What difficulty do you want to play on?\nEasy (E)\nMedium (M)\nHard(H)\nDifficulty: ")

    if Difficulty_Mode.upper() == "E":
        Difficulty = 0
        t -= 1
    if Difficulty_Mode.upper() == "M":
        Difficulty = 1
        t -= 1
    if Difficulty_Mode.upper() == "H":
        Difficulty = 2
        t -= 1

#print("You can change this later by typing the right letter.") #to be added later

while t == 0: #Loop the whole program

    Wrong_Right = False
    Guesses = 3

    def x():
        x = random.random() * 10
        x = round(x, Difficulty)
        if int(x) == float(x):
            x = int(x)
        return x
    
    def y():
        y = random.random() * 10
        y = round(y, Difficulty)
        if int(y) == float(y):
            y = int(y)
        return y

    x = x()
    y = y()

    if Points == 5:
        print("\nCongrats! you now have 5 points.")
    if (Points % 10) == 0:
        print(f"\nCongrats! you now have {Points} points.")
    
    if Sign == "+":
        Correct_Answer = x + y
    if Sign == "-":
        Correct_Answer = x - y
    if Sign == "*":
        Correct_Answer = x * y
    if Sign == "/":
        Correct_Answer = round((x / y), Difficulty)

    while Wrong_Right == False and Guesses > -1:
        print(f"\nwhat is {x} {Sign} {y}?")
        Answer = input("Answer: ")
        print(Correct_Answer)
        if (Correct_Answer * 0.999) < float(Answer) < (Correct_Answer * 1.001):
            print("\nThat's correct!")
            Wrong_Right == True
            Points += 1
            Guesses = -2
            
        elif Guesses > 0:
            ("\nNot quite, please try again.\n")
            Guesses -= 1

        if Guesses == 0:
            print("\nThat's incorrect.")
            print(f"The answer is {Correct_Answer}")
            Wrong_Right = True
            Guesses -= 1

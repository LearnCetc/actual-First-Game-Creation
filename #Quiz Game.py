#Quiz Game
import random

t = 0
Sign = "o"
Sign_Loop_Value = 0
global Points
Points = 0
Points_bool = True

print("Game by LearnCetc\n")
Amount_of_Decimals = input("How many decimals?\nAmount of decimals: ")
Amount_of_Decimals = int(Amount_of_Decimals)

while Sign_Loop_Value == 0: #Used to make the code loop until a valid letter has been writen
    Sign = input("\nDo you want to do\nAddition (A)\nSubstraction (S)\nMultiplication (M)\nDivision (D)\n")
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
        print(f"if the answer contains infinte decimals round it and then write it with {Amount_of_Decimals} decimals")
        Sign_Loop_Value += 1

With_or_Without_Points = input("Do you want to use points? (Y) (N): ")
if With_or_Without_Points.upper() == "N":
    Points_bool = False

#print("You can change this later by typing the right letter.") #to be added later

while t == 0: #Loop the whole program

    Wrong_Right = False
    Guesses = 3

    def x():
        x = random.random() * 10
        x = round(x, Amount_of_Decimals)
        x += Points
        if int(x) == float(x):
            x = int(x)
        return x
    
    def y():
        y = random.random() * 10
        y = round(y, Amount_of_Decimals)
        y += Points
        if int(y) == float(y):
            y = int(y)
        return y

    x = x()
    y = y()
    print(Points)
    
    if Sign == "+":
        Correct_Answer = x + y
    if Sign == "-":
        Correct_Answer = x - y
    if Sign == "*":
        Correct_Answer = x * y
    if Sign == "/":
        Correct_Answer = round((x / y), Amount_of_Decimals)
    print(Points_bool)
    while Wrong_Right == False and Guesses > -1:
        print(f"\nwhat is {x} {Sign} {y}?")
        Answer = input("Answer: ")
        print(Correct_Answer)
        if (Correct_Answer * 0.999) < float(Answer) < (Correct_Answer * 1.001):
            print("\nThat's correct!\n")
            Wrong_Right == True
            if Points_bool == True:
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
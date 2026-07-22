#Quiz Game
import random
t = 0
print("Game by LearnCetc\n")
Amount_of_Decimals = input("How many decimals?\nAmount of decimals: ")
Amount_of_Decimals = int(Amount_of_Decimals)

Sign = input("Do you want to do\nAddition (A)\nSubstraction (S)\nMultiplication (M)\nDivision (D)\n")
Sign = Sign.upper()
if Sign == "D":
    print(f"if the answer contains infinte decimals write it with {Amount_of_Decimals} decimals")
print("You can change this later by typing the right letter.")

while t == 0: #Loop the whole program

    if Sign == "A":
        Sign = "+"
    elif Sign == "S":
        Sign = "-"
    elif Sign == "M":
        Sign = "*"
    elif Sign == "D":
        Sign = "/"
    else:
        break

    Wrong_Right = False
    Guesses = 3

    def x():
        x = random.random() * 10
        x = round(x, Amount_of_Decimals)
        return x
    
    def y():
        y = random.random() * 10
        y = round(y, Amount_of_Decimals)
        return y
    
    if Sign == "+":
        Correct_Answer = x(x) + y(y)
    if Sign == "-":
        Correct_Answer = x(x) - y(y)
    if Sign == "*":
        Correct_Answer = x(x) * y(y)
    if Sign == "/":
        Correct_Answer = x() / y()
        Correct_Answer = round(Correct_Answer, Amount_of_Decimals)

    while Wrong_Right == False and Guesses > -1:
        print(f"what is {x()} {Sign} {y()}?")
        Answer = input("Answer: ")

        if Answer == Correct_Answer:
            print("\nThat's correct!\n")
            Wrong_Right == True

        elif Guesses > 0:
            ("\nNot quite, please try again.\n")
            Guesses -= 1

        if Guesses == 0:
            print("That's incorrect.")
            print(f"The answer is {Correct_Answer}")
            Guesses -= 1
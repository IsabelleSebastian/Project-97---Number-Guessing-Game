import random
number = random.randint(0,10)

chances = 0

print("Guess My Lucky Number : 0-10")

while (chances < 5):
    chooseNumber = int(input("Your Guess: "))

    if(chooseNumber > number):
        print("Your guess is too high; the number is less than ", chooseNumber)
           
    elif(chooseNumber < number):
        print("Your guess is too low; guess a number greater than ", chooseNumber)
    
    elif(chooseNumber == number):
        print("Yay!! That's correct!!!") 
        break


    chances += 1

if not chances < 5:
    print("You Lose!! :( The number is ", number)

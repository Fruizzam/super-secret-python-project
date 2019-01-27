import random
n = random.randint(1,99)
guess = int(input("Enter an integer from 1 to 99: "))
while n != guess:
    if guess < n:
            print("that's too low")
            guess = int(input("Enter an number from 1 to 99: "))
    elif guess > n:
            print("that's too high")
            guess = int(input("Enter an number from 1 to 99: "))
            #dont put the answer in the loop lmao
if guess == n:
        print("you guessed it!")
name = input("What is your name? ")
print("Welcome " + name + ", you are worthy. [Enter]")
input ()
print("We will now begin the assessment.")
input ()
d1 = input ("Which do you prefer? (A) Left. (B) Right. [A/B] :")
if d1 == "a" or "A":
    print ("You begin to walk down the path
input ()
    print ("There are cows grazing in the grass. Their eyes follow you.")
input ()          
    print ("You see one of them begin to melt.")
if d1 == "b" or "B":
    print ("You are cancelled. Sorry.")

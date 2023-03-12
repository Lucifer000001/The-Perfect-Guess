import random
randNumber = random.randint(1,100)
guesses = 0
print("**********Guess the Number Selected Between 1 and 100***************\n")
user = None
while (user != randNumber):
    user = int(input("\nNow Guess The Number : "))
    guesses += 1
    if (randNumber == user):
        print("\n*****\U0001F603Congratulations You Got it Right\U0001F603***********")
    else:
        if (randNumber > user):
            print("A little higher please!!!!!!")
        else:
            print("A little lower  please!!!!!!")
print(f"\nYour Total Number Of Guesses Were : {guesses}")
with open("highscore.txt","r") as f:
    highScore = int(f.read())
if (guesses < highScore):
    print("\n*********\U0001F60ECongratulations You Broke The Record\U0001F60E***********")
    with open("highscore.txt","w") as f:
        f.write(str(guesses)) 
print("\n********\U0001F607Hope You Liked The Game\U0001F607**********")
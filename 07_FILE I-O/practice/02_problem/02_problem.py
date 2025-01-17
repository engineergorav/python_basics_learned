# the game fun( ) lets a user play a game and returns the score as an integer, You need to read a file "Hi-score.txt"
# which is either blank or contains previous hi score. You need to write a program to update the Hi score whenever 
# the game() fun break the previous hi score.


import random
import os 


def game():
    print(" ")
    print("you are playing the game: ")
    score=random.randint(1,99)
    if os.path.exists("Hi-score.txt") and os.path.getsize("Hi-score.txt")>=0:
        with open("Hi-score.txt") as f:
            hiscore=f.read() 
            hiscore=int(hiscore)
            print(f"your todays score is {score}")
            print(f"Your high score is {int(hiscore)}")
            if(score>hiscore):
                update(score)
            else:
                print("your score is low:")
                print(" ")
    else:
        hiscore=0
        print(f"your todays score is {score}")
        print(f"Your  todays high score is {hiscore}")
        update(hiscore)
def update(a):
    with open("Hi-score.txt","w") as f:
        f.write(str(a))
        print("Hi score is updated successfully: ")
        print(" ")

game()
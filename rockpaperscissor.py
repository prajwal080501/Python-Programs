
import random
print("Rules for the game : \n\n\n Rock vs Paper : Paper wins. \n\n Rock vs Scissors : Rock wins. \n\n Paper vs scissors : Scissors win .")
while True:
    
    r = 'rock'
    p = 'paper'
    s = 'scissors'

    user_choice = input(
        "Enter your choice(\n Press r.for rock \n Press p.for paper\n Press s.scissors \n 0.To Exit:)\n->")
    if(user_choice == 0):
        exit()
    print("You chose \n", user_choice)
    print("Now its computers turn.... \n")
    computer_choice = random.randint(1,3)
    if(computer_choice == 1):
        print("computer chose :\n" + r)
    if(computer_choice == 2):
        print("computer chose :\n" + p )
    if(computer_choice == 3):
        print("computer chose :\n" + s )
    if(computer_choice == 1 and  user_choice == r):
        print("its a draw")
    if(computer_choice == 2 and  user_choice == p):
        print("its a draw")
    if(computer_choice == 3 and  user_choice == s):
        print("its a draw")
    if(computer_choice == 1 and user_choice == p):
        print("You  chose Paper  you  wins computer  loses ")
    if(computer_choice == 1 and user_choice == s):
        print("Computer  Wins computer chose :Rock . ")
    if(computer_choice  == 2 and user_choice == r):
        print("Computer chose: Paper Computer wins" )
    if(computer_choice == 3 and user_choice == r):
        print("You chose :Rock You  win !")
    if(computer_choice == 3 and user_choice == p):
        print("computer  wins !")
    if(computer_choice == 2 and  user_choice == s):
        print("You win !")
    
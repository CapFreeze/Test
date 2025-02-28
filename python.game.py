from random import randrange
answer = randrange (100)
while True:
    player_guess = int (input("Guess a number:  "))
    if (answer == player_guess):
        print("You Win!")
        break
    if ( answer < player_guess ) : 
        print("It's Smaller")    
    else:
        print("Its Bigger")      
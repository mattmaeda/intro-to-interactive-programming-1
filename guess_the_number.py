# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

game_type = None

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global guesses
    global game_type
   
    # Initialize using number 0 - 99
    if game_type is None or game_type == 100:
        range100()
    else:
        range1000()
   
    print ""

       
# helper function to print remaining guesses
def remaining_guesses():
    # print remaining guesses
    global guesses    
    print "Number of remaining guesses: %d" % guesses


# helper function to set range
def set_secret_number(x):
    # set secret number on max range
    global secret_number
    print "New game.  Range is from 0 to %d" % x
    secret_number = random.randrange(x)    
   
   
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global guesses
    global game_type    
   
    guesses = 7
    game_type = 100
    set_secret_number(game_type)
    remaining_guesses()


def range1000():
    # button that changes the range to [0,1000) and starts a new game    
    global guesses
    global game_type    
   
    guesses = 10
    game_type = 1000
    set_secret_number(game_type)
    remaining_guesses()
 

def input_guess(guess):
    # main game logic goes here
    global secret_number
    global guesses
    global game_type
   
    restart = False
   
    print "Guess was %s" % guess
   
    int_guess = int(guess)
   
    if int_guess == secret_number:
        print "Correct!"
        print ""
        restart = True
       
    # Last guess
    elif guesses == 1:
        print "You ran out of guesses.  The number was %d" % secret_number
        print ""
        restart = True      
       
    else:
        guesses -= 1
        remaining_guesses()
       
        if int_guess < secret_number:
            print "Higher"
        else:
            print "Lower"
       
        print ""
   
    # Restart game?
    if restart:
        new_game()

   
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game
new_game()
f.start()

# always remember to check your completed program against the grading rubric

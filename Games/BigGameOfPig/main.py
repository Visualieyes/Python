import random


#Scores two dice die1 and die2 according to Big Pig rules.
#If both dice show one, returned points are 25
#If only one die shows one, returned points are 0
#if both dice show the same number, returned points are 4 * what one die shows
#otherwise returned points are the sum of faces of the dice
def score_dice(die1, die2):
    if die1 == 1 and die2 ==1:
        pts = 25
    elif die1 == 1 or die2 == 1:
        pts = 0
    elif die1 == die2:
        pts = (die1 +die2)*2
    else:
        pts = die1+ die2
    return pts


#Rolls and returns random faces of two dice as a tuple.
def roll_dice():
    r1 = random.randrange(1, 7)
    r2 = random.randrange(1, 7)

    return (r1,r2)

#Displays the dice on the screen.
def display_dice(d1, d2):
    print("Roll: ", d1 ,"and", d2)


#Asks the user to enter r for roll or h for hold until they do so.
#Return True if the user entered r and False if the entered h.
def go_again():
    decision = True
 
    while decision:
        decision = input("""Enter 'r' to roll or 'h' to hold:""")
        if decision != 'r' and decision != 'h':
            print("invalid input")
            decision = True
        elif decision == 'r': 
            return True
        else:
            return False

        

#Displays the turn score_board.
def print_points(points, turn_points):
    print("****************************************")
    print("This throw:", points, "points. This turn:", turn_points)
    print("****************************************")
    
#Roll, display and score two dice.
def throw_and_score_dice():
    (die1, die2) = roll_dice()
    display_dice(die1,die2)
    points = score_dice(die1, die2)

    return points 
    
#Play the whole turn of a user.
#Return the number of points for the turn.
def user_turn():
     points = throw_and_score_dice()
     total = 0
     while go_again():
         
         points = throw_and_score_dice()
         total = total + points
         

     return total


#Returns True if the computer should roll again and False otherwise.
#Implement as a random decision. If you have time, this where you can
#implement AI for the computer player.
def computer_go_again():
    computer_move = random.randint(0,1)
    if computer_move == 1:
        return False
    else:
        return True
    

#Play the whole turn of a user.
#Return the number of points for the turn.
def computer_turn():
     points = throw_and_score_dice()
     total = 0
     while go_again():
         
         points = throw_and_score_dice()
         total = total + points
         

     return total

#Display the scoreboard.
def display_scoreboard(user_points, computer_points):
    print("\n\n#################################")
    print("#\tYou: ", user_points, "Me:", computer_points,"\t\t")
    print("#################################\n\n")

#Display the instructions
def display_intro():
    print("Welcome to the game of Pig!")
    print("Here are the rules:")
    print("You can roll the dice as many times as you want and accumulate points.")
    print("as long as you don’t get 1 on exactly one die. If you do get 1 on exactly")
    print("one die, you lose your accumulated points for your turn and your turn")
    print("is over. You can choose to stop your turn at any time and keep your points.")
    print()

#Return true if either user points or computer_points are greater or equal
#to maxpoints
def game_over(user_points,computer_points,max_points):
        return user_points >= max_points or computer_points >= max_points


#Display the winner of the game.
def display_winner(user_points, computer_points,max_points):
    if user_points >= max_points:
        print("\n\nCongratulations! You win!");
    else:
        print("I win! Yeah!!!");

#Play a game of Pig
def play_pig():

    #points to win the game - make the value smaller while you are developing the game
    max_points = 50;

    user_points = 0;
    computer_points = 0

    #user starts
    whose_turn = "USER"

    display_intro()
    
    while not game_over(user_points,computer_points,max_points):
        if whose_turn == "USER":
            print("Your turn!")
            user_points = user_points + user_turn()
            whose_turn = "COMPUTER"
        else:
            print("My turn!")
            computer_points = computer_points + computer_turn()
            whose_turn = "USER" 

        display_scoreboard(user_points, computer_points)
        dummy = input("Press enter to continue")

    display_winner(user_points, computer_points,max_points)

    
play_pig()
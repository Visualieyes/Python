#Code Author: Keyann Al-Kheder
#Project #2: Rock Paper Scissors Game
#Class: Comp 101

# import random module 
import random 
  


#Check which player won the round
def rps_Outcome(player_choice, comp_choice):

    if((player_choice == 'rock' and comp_choice == 'paper')):
        return 'lose'
    elif((player_choice == 'rock' and comp_choice == 'scissors')): 
        return 'win'
    elif((player_choice == 'paper' and comp_choice == 'rock')):
        return 'win'
    elif((player_choice == 'paper' and comp_choice == 'scissors')):
        return 'lose'
    elif((player_choice == 'scissors' and comp_choice == 'paper')):
        return 'win'
    elif((player_choice == 'scissors' and comp_choice == 'rock')):
        return 'lose'
    else:
        return 'draw'


#Helper function
#Gathers user input and converts it to an easily comprable
#player choice
def player_Choice():

    print("Enter choice \n (R/r) Rock \n (P/p) paper \n (S/s) scissors \n") 

    #take the input from user 
    choice = input("User turn: ")

    if choice == 'r' or choice =='R': 
        return 'rock'
    elif choice == 'P' or choice == 'p': 
        return 'paper'
    elif choice == 'S' or choice == 's': 
        return 'scissors'
    else:
        print("Error: Wrong Input")
        return -1

    
#Randomly generates a choice for the computer
def comp_Choice():
    comp_choice = random.randint(1, 3) 
  
    if comp_choice == 1: 
        return 'rock'
    elif comp_choice == 2: 
        return 'paper'
    else: 
        return 'scissors'


def main():
    # Print multiline instruction 
    print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n"
                                +"First to 3 wins ")          
    

    #if ((input("Would you like to play rock paper scissors? (y) yes (n) no")) == 'y'):
    gameOver = False
    #Player Scores
    playerScore = 0
    compScore = 0
    
    while not gameOver:

        #Player Moves  
        playerChoice = player_Choice()
        while(playerChoice == -1):
            playerChoice = player_Choice()
        
        compChoice = comp_Choice()
     
        #Display moves on screen
        print("Your choice is: " + playerChoice) 

        print("Computer choice is: " + compChoice)
            
          
        #Check and display outcome on screen
        if (rps_Outcome(playerChoice, compChoice) == 'win'):
            print("You Win!")
            playerScore = playerScore + 1
        elif (rps_Outcome(playerChoice, compChoice) == 'lose'):
            print("Comp Wins")
            compScore = compScore + 1
        else:
            print("Draw!")

        #Display new score    
        print("Player Score: ", playerScore, "\tComp Score:", compScore)

        
        #Check if score reached 3
        if (playerScore == 3):
            print("You Win!")
            gameOver = True
        elif(compScore == 3):
            print("You Lose!")
            gameOver = True
        else:
            gameOver = False
    
              
    #ask if user wants to play again    
    playAgain = input("Do you want to play again? (Y/N)") 
  
    #if not, game ends
    if (playerAgain == 'n' or playerAgain == 'N'):
        return 0
    elif (playerAgain == 'y' or playerAgain == 'Y'):
        main()
    else:
        exit()
            




        
if __name__ == "__main__":
    main()
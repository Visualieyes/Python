#Frogger game
#The goal of the game is to move your frog accross the stream while avoiding birds and other predators to
#find the bug and eat it at the otherside

import turtle
import math
import random

#Set up screen
window_height = 400
window_width = 400

wn = turtle.Screen()
wn.screensize(window_height,window_width)
wn.bgcolor("pink")

#set up some constants of the game
#use these when you are developing the game so late you can change them
#to make your game more interesting
forward_step = 10         #how much does the turtle move forward
backward_step= +10
turn_step = 30          #how much does the turtle turn (in degrees)
shrink_factor = 1     #how much does the turtle shrink when it moves - you may want
                        #to make this number smaller when you finish your game
death_width = 0.1       #the size at which you stop the game because the user lost

collision_threshold = 20;#we say that two turtles collided if they are this much away
                        #you may want to have this number large while you are developing
                        #your game

#Create player turtle
player = turtle.Turtle()
player.penup()
player.color("blue")
player.shape("turtle")
player.setposition(0,-350)

#create a bug
bug1 = turtle.Turtle()
bug1.penup()
bug1.color("black")
bug1.shape("circle")
#set the bug size to 20% of the original size
bug1.shapesize(0.2,0.2)
bug1.setposition(0, 300)


#create enemy
enemy = turtle.Turtle()
enemy.penup()
enemy.color("red")
enemy.shape("triangle")
enemy.penup()
enemy.setposition(-200, 200)
#second enemy
bob = turtle.Turtle()
bob.penup()
bob.color("blue")
bob.shape("square")
bob.penup()
bob.setposition(100, 100)
#third enemy
doug= turtle.Turtle()
doug.penup()
doug.color("green")
doug.shape("circle")
doug.penup()
doug.setposition(50, 0)
#fourth enemy
austin= turtle.Turtle()
austin.penup()
austin.color("purple")
austin.shape("circle")
austin.penup
austin.setposition(150,-100)
#fifth enemy
alex=turtle.Turtle()
alex.penup()
alex.color("orange")
alex.shape("square")
alex.penup
alex.setposition(-150,-250)
#sixth enemy
greg=turtle.Turtle()
greg.penup()
greg.color("brown")
greg.shape("triangle")
greg.penup
greg.setposition(0,-200)




#create the score keeper turtle
score_keeper = turtle.Turtle()
score_keeper.color("red")
score_keeper.pensize(3)
score_keeper.penup()
score_keeper.hideturtle()
score_keeper.setposition(-295, 260)
score_keeper.pendown()
score = 0
scorestring = "Score: %s" %score
score_keeper.write(scorestring, False, align="left", font=("Arial",14, "normal"))

#Create Title
title= turtle.Turtle()
title.color("red")
title.pensize(5)
title.penup()
title.hideturtle()
title.setposition(0,310)
title.pendown()
titlestring= "FROGGER THE GAME"
title.write(titlestring, False, align= "center", font=("Arial",25, "normal"))

#Create Name of Authors 
name=turtle.Turtle()
name.color("red")
name.pensize(5)
name.penup()
name.hideturtle()
name.setposition(450,260)
name.pendown()
namestring= "By: Austin Dao  and Keyann Al-Kheder"
name.write(namestring,False, align= "right", font=("Arial",12, "normal"))
#Define functions

#This function returns the width of a turtle which_turtle
def get_width(which_turtle):
    which_turtle_dims = which_turtle.shapesize()
    which_turtle_width = which_turtle_dims[0]
    return which_turtle_width

#This function shrinks the turtle by the above defined shrink_factor.
def turtle_shrink(which_turtle):
    player_dims = which_turtle.shapesize()
    player_width = player_dims[0] * shrink_factor
    player_length = player_dims[1] * shrink_factor
    which_turtle.shapesize(player_width,player_length)

#this function turns the player's turtle left by the above defined turn_step
def turn_left():
    player.left(turn_step)

#this function turns the player's turtle right by the above defined turn_step
def turn_right():
    player.right(turn_step)

	
#This function moves the player turtle forward by the above defined
#forward_step and shrinks it.
#Note that this function doesn't have any parameters, but uses the
#global player turtle.
def go_forward():
    #move
    player.forward(forward_step)
    #shrink the turtle
    turtle_shrink(player)

def go_back():
        player.back(backward_step)


#This function eturns true if the turtles t1 and t2 are within the
#above defined collicion_thershold
def is_collision(t1, t2):
    d = math.sqrt((t1.xcor()-t2.xcor())**2 + (t1.ycor()-t2.ycor())**2)
    if d < collision_threshold:
            return True
    else:
            return False

#if the turtle t hit a vertical edge of the screen, turn it around by 180 and move forward a bit
def bounce_of_boundary(t):

    if t.xcor() > window_width - get_width(t) or t.xcor() < -window_width + get_width(t):
            t.right(180)
                                
    t.forward(1)

#update the display of the score_keeper turtle
def update_score(new_score):
    score_keeper.undo()
    score_keeper.penup()
    scorestring = "Score: %s" %new_score
    score_keeper.write(scorestring, False, align="left", font=("Arial",14, "normal"))
		
#Set keyboard bindings
turtle.listen()

turtle.onkey(go_forward, "Up")
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")
turtle.onkey(go_back, "Down")

#This variable is set to True inside the loop below if you want the game to end.
game_over = False
player_width = get_width(player)

#while the game is not over and the turtle is large enough print the width of the turtle
#on the screen.
#This is the main game loop.
while not game_over and player_width > death_width:


    if is_collision(player,bug1):
        print("collision")
        #restore the player turtle to the original size
        player.shapesize(1,1)
        player.setposition(0,-350)
        
        #move the bug and the enemy to a random location on the screen
        new_height = random.randint(-window_height, window_height)
        snew_width = random.randint(-window_width, window_width)
       
        
        #update the score
        score = score + 1
        update_score(score)


    if is_collision(player,enemy)or is_collision(player,bob)or is_collision(player,doug)or is_collision(player,austin) or is_collision(player,alex) or is_collision(player,greg):
            game_over = True
            
    #move the enmy forward and bounce of the wall if it hit it
    enemy.forward(5)
    bounce_of_boundary(enemy)

    player_width = get_width(player)

    # moving bob
    bob.backward(10)
    bounce_of_boundary(bob)

    player_width = get_width(player)
    
    #moving doug
    doug.forward(7)
    bounce_of_boundary(doug)

    player_width = get_width(player)

    #moving austin
    austin.backward(12)
    bounce_of_boundary(austin)

    player_width = get_width(player)
    
    #moving alex
    alex.forward(9)
    bounce_of_boundary(alex)

    player_width= get_width(player)
    
    #moving greg
    greg.backward(15)
    bounce_of_boundary(greg)

    player_width= get_width(player)

#write the outcome of the game for the user
score_keeper.undo()
score_keeper.penup()

if game_over or player_width <= 0.1:

        score_keeper.write("You lost!",False, align="left", font=("Arial",14, "normal"))
else:
        score_keeper.write("You won!",False, align="left", font=("Arial",14, "normal"))

wn.exitonclick()
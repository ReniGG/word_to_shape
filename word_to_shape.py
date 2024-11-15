import turtle
import random

#set up the screen
ws = turtle.Screen()
ws.bgcolor('#99e6ff')
ws.title('Random Shapes from Words')

#set up the turtle
jim = turtle.Turtle()
jim.color('#ff9999')
jim.pensize(5)
jim.speed(0)
jim.shape('turtle')

#set the length for the forward movement
length = 100

#empty list to store the random angles
angles = []

#ask for a word input
word = input('Please, enter a word.')

# list() splits the word into a list of characters
letter_list = list(word) 

#generate random angles for each letter
for _ in letter_list:
    random_angle = random.randint(35, 120)
    angles.append(random_angle) #add the random angle to the angles list

#draw a shape based on the angles list
def draw_shape(length, angles):
    for angle in angles * 12: #iterate through the angles list 12 times
        jim.forward(length)
        jim.left(angle) # Each angle comes from the angles list, which contains random values generated earlier

draw_shape(length, angles)

turtle.done()
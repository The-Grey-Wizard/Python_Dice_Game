import random
import time
import turtle
### INIT OUR DICE ###
screen = turtle.Screen()
screen.addshape("dice01.gif")
screen.addshape("dice02.gif")
screen.addshape("dice03.gif")
screen.addshape("dice04.gif")
screen.addshape("dice05.gif")
screen.addshape("dice06.gif")
die01 = turtle.Turtle()
die02 = turtle.Turtle()
die03 = turtle.Turtle()
die04 = turtle.Turtle()
die05 = turtle.Turtle()
die06 = turtle.Turtle()
die01.hideturtle()
die02.hideturtle()
die03.hideturtle()
die04.hideturtle()
die05.hideturtle()
die06.hideturtle()
die01.shape("dice01.gif")
die02.shape("dice02.gif")
die03.shape("dice03.gif")
die04.shape("dice04.gif")
die05.shape("dice05.gif")
die06.shape("dice06.gif")

### INSTRUCTION ###
print("Let's throw some dice!")

while True: #game runs until player choses presses the "n" key
  print("Throwing...")
  #a short delay before the toss
  time.sleep(2)
  
  #random number between 1 and 6
  #does not count 7
  die_face = random.randrange(1,7)
  print("You rolled a " + str(die_face))
  
  #### SHOW DIE FACES ####
  if die_face == 1:
    die01.showturtle()
  elif die_face == 2:
    die02.showturtle()
  elif die_face == 3:
    die03.showturtle()
  elif die_face == 4:
    die04.showturtle()
  elif die_face == 5:
    die05.showturtle()
  else:
    die06.showturtle()
    
  #CONTINUE?
  cont = input("Do you want to play again? y/n: ")
  if cont == "n":
    print("Quiting Game Now...")
    quit()
  elif cont == "y":
    die01.hideturtle()
    die02.hideturtle()
    die03.hideturtle()
    die04.hideturtle()
    die05.hideturtle()
    die06.hideturtle()
  else:
    while cont != "y" or "n":
      print("Error: Press y/n: ")
      cont = input("Do you want to play again? y/n: ")
      if cont == "n":
        print("Quiting Game Now...")
        quit()
      elif cont == "y":
        die01.hideturtle()
        die02.hideturtle()
        die03.hideturtle()
        die04.hideturtle()
        die05.hideturtle()
        die06.hideturtle()
        break
      else:
        continue


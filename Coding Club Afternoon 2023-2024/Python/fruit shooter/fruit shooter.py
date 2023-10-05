import pgzrun
import random
#Set pictures
apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")
def draw(): #Draw pictures
   screen.clear()
   screen.fill("dark blue")
   apple.draw()
   orange.draw()
   pineapple.draw()
def placeApple(): #Set position for APPLE
   apple.x = random.randint(50, 800) #Random x
   apple.y = random.randint(50, 300) #Random y
def placeOrange(): #Set position for ORANGE
   orange.x = random.randint(50, 800) #Random x
   orange.y = random.randint(50, 300) #Random y
def placePineapple(): #Set position for PINEAPPLE
   pineapple.x = random.randint(50, 800) #Random x
   pineapple.y = random.randint(50, 300) #Random y
#Run scripts
placeApple()
placeOrange()
placePineapple()
def on_mouse_down(pos): #When click
   if apple.collidepoint(pos): #If click apple
      print("You shooted apple!")
      placeApple()
   else:
      if orange.collidepoint(pos): #If click orange
         print("You shooted orange!")
         placeOrange()
      else:
         if pineapple.collidepoint(pos): #If click pineapple
            print("You shooted pineapple!")
            placePineapple()
         else:
            print("You missed!")
   
pgzrun.go()

## FORCE FUNCTIONS FOR PYGAME
## on_mouse_down(pos) ==> click
## Actor(something) ==> Gives a variable an img
## VAR.draw ==> Draw a img variable to the game
## MUST import pgzrun
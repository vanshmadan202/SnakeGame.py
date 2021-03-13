# SnakeGame.py
import pygame,sys,pygame.locals
from tkinter import*
import random
#pygame.locals cotains name of all constants to be used i.e.pygame.locals.set()

#to initialize all modules in pygame
pygame.init()

#window is name of the surface
window=pygame.display.set_mode((460,460))

pygame.display.set_caption("Snake Game")

#to pause the screen for a while
# while True:
#
#     for event in pygame.event.get():
#         if event.type==2:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()
def drawlines():
    for i in range(0,460,20):
        pygame.draw.line(window,(0,255,0),(i,0),(i,460))
    #line(surface,(RGB #green used with),start point,end point)
    for i in range(0,460,20):
        pygame.draw.line(window,(0,255,0),(0,i),(460,i))

snakedots=[]

snakedots.append({"x":10,"y":10})
snakedots.append({"x":11,"y":10})
snakedots.append({"x":12,"y":10})

#print(len(snakedots)) len is no. of dictionnary in list
#x=10

fruitx= random.randint(5,20)
fruity= random.randint(5,20)

def drawsnake():
    fruit=pygame.Rect(fruitx*20 , fruity*20,20,20)
    pygame.draw.rect(window,(0,0,255),fruit)

    for i in range(0,len(snakedots)):
        snake = pygame.Rect(snakedots[i]["x"]*20 , snakedots[i]["y"]*20 ,20 ,20)
        # Alternative of using dictionary #snake=pygame.Rect((x+i)*20 , x*20 , 20, 20)
        pygame.draw.rect(window,(255,0,0) , snake)

drawlines()
drawsnake()
FPSCLOCK = pygame.time.Clock()

# def movesnake():
#     window.fill(0,0,0)

direction=1
score=0
while True:
    for event in pygame.event.get():
        if event.type == 12:
            pygame.quit()
            sys.exit()

        elif event.type == 2 and event.key == 275:
            print("right key pressed")
            direction=2
        elif event.type == 2 and event.key == 276:
            print("Left Key pressed")
            direction=1
        elif event.type == 2 and event.key == 273:
            print("Up Key pressed")
            direction=3
        elif event.type == 2 and event.key == 274:
            print("down key pressed")
            direction=4

    if direction==1:

        snakedots.insert(0,{"x":snakedots[0]["x"]-1,"y":snakedots[0]["y"]})

    if direction==2:

        snakedots.insert(0,{"x":snakedots[0]["x"]+1 , "y":snakedots[0]["y"]})

    if direction==3:

        snakedots.insert(0,{"x":snakedots[0]["x"],"y":snakedots[0]["y"]-1})

    if direction==4:

        snakedots.insert(0,{"x":snakedots[0]["x"],"y":snakedots[0]["y"]+1})

    if fruitx==snakedots[0]["x"] and fruity==snakedots[0]["y"]:
        score=score+10
        fruitx=random.randit(5,20)
        fruity=random.randint(5,20)
    else:
        del snakedots[-1]

    if snakedots[0]["x"] < 1 or snakedots[0]["x"]>22 or snakedots[0]["y"]<1 or snakedots[0]["y"]>22:
        obj=Tk()
        obj.geometry("200x200")
        showinfo("Score is " + score)
        bt1=Button(obj , text="Exit" , command="break")
        bt1.pack()
        obj.mainloop()


    window.fill((0,0,0))
    drawsnake()
    drawlines()
    pygame.display.update()
    FPSCLOCK.tick(5)

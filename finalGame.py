import pygame,sys,pygame.locals
import random
pygame.init()

window=pygame.display.set_mode((460,460))
pygame.display.set_caption("Snake Game")
def drawlines():
    for i in range(0,460,20):
        pygame.draw.line(window, (0, 255, 0), (i, 0), (i, 460))
    for j in range(0,460,20):
        pygame.draw.line(window, (0, 255, 0), (0, j), (460, j))

snakedots=[]

snakedots.append({"x":10,"y":10})
snakedots.append({"x":11,"y":10})
snakedots.append({"x":12,"y":10})

fruitx= random.randint(5,20)
fruity= random.randint(5,20)

def drawsnake():
    fruit = pygame.Rect(fruitx * 20, fruity * 20, 20, 20)
    pygame.draw.rect(window, (0, 0, 255), fruit)

    for i in range(0,len(snakedots)):
        snake = pygame.Rect(snakedots[i]["x"] * 20, snakedots[i]["y"] * 20, 20, 20)
        pygame.draw.rect(window, (255, 0, 0), snake)


drawsnake()
drawlines()
FPSCLOCK = pygame.time.Clock()
direction=1
while True:
        for event in pygame.event.get():
            if event.type == 12:
                pygame.quit()
                sys.exit()
            elif event.type == 2 and event.key == 275:
                direction=2
            elif event.type == 2 and event.key == 276:
                direction=1

            elif event.type == 2 and event.key == 273:
                direction=3

            elif event.type == 2 and event.key == 274:
                direction=4

        if direction == 1:
            snakedots.insert(0, {"x": snakedots[0]["x"] - 1, "y": snakedots[0]["y"]})
        if direction == 2:
            snakedots.insert(0, {"x": snakedots[0]["x"] + 1, "y": snakedots[0]["y"]})
        if direction == 3:
            snakedots.insert(0, {"x": snakedots[0]["x"] , "y": snakedots[0]["y"]-1})
        if direction == 4:
            snakedots.insert(0, {"x": snakedots[0]["x"] , "y": snakedots[0]["y"]+1})

        if fruitx == snakedots[0]["x"] and fruity == snakedots[0]["y"]:
            fruitx = random.randint(5, 20)
            fruity = random.randint(5, 20)
        else:
            del snakedots[-1]

        if snakedots[0]["x"] < 1 or snakedots[0]["x"] > 22 or snakedots[0]["y"] < 1 or snakedots[0]["y"] > 22:
            break

        window.fill((0, 0, 0))
        drawsnake()
        drawlines()
        pygame.display.update()
        FPSCLOCK.tick(5)

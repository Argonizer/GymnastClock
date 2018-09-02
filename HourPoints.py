import pygame
import math

centreX = 200
centreY = 200
radius = 180

color0 = (255, 255, 0)
color1 = (255, 0, 0)
color2 = (0, 255, 0)
color3 = (0, 0, 255)
color4 = (0, 255, 255)
color5 = (255, 0, 255)
color6 = (100, 100, 100)
color7 = (100, 0, 100)
color8 = (100, 100, 0)
color9 = (0, 100, 100)
color10 = (50, 50, 100)
color11 = (50, 70, 0)

List = [color0, color1, color2, color3, color4, color5, color6, color7, color8, color9, color10, color11]

def toRadians(degree):
    return degree / 180 * math.pi

def setCentre(x,y, rad):
    centreX = x
    centreY = y
    radius = rad


def makePoints(Display, hour):


    for i in range(12):
        circleX = int(centreX + radius * math.sin(toRadians(30 * i)))
        circleY = int(centreY - radius * math.cos(toRadians(30 * i)))
        thickness = 5
        if(i == hour):
            thickness = 10
        pygame.draw.circle(Display, List[i], (circleX, circleY), 10, thickness)


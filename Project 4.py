#Veronica Stureborg
#CMPT 120L 200
#Project 4 - Trafficlight
#Programming code for creating a traffic light

from graphics import *
def main ():
    win= GraphWin('Stoplight')
#code for the rectangle
    rectangle= Rectangle(Point(30,30), Point(90, 150))
    rectangle.setOutline("black")
    rectangle.setFill("white")
    rectangle.draw(win)
#code for the red light
    redlight= Circle(Point(60,55), 15)
    redlight.setOutline("black")
    redlight.setFill("red")
    redlight.draw(win)
#code for the yellow light
    yellowlight= Circle(Point(60,90), 15)
    yellowlight.setOutline("black")
    yellowlight.setFill("yellow")
    yellowlight.draw(win)
#code for the green light
    greenlight= Circle(Point(60,125), 15)
    greenlight.setOutline("black")
    greenlight.setFill("green")
    greenlight.draw(win)
                
main()

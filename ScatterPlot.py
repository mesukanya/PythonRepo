import matplotlib.pyplot as plt
from pylab import randn
import numpy as np
import pandas as pd
import math
import random

class TestSCatterplot:

    def DrawScatterPlot(self):
        x=randn(200)
        y=randn(200)
        plt.scatter(x,y, color='r')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def EmptyCircle(self):
        x=np.random.randn(50)
        y=np.random.randn(50)
        plt.scatter(x,y, s=70,facecolors='none',edgecolors='g')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def BallsWithDifferentColors(self):
        no_of_Balls=25
        x=[random.triangular() for i in range(no_of_Balls)]
        y=[random.gauss(0.5,0.25) for i in range(no_of_Balls)]
        colors = [random.randint(1, 4) for i in range(no_of_Balls)]
        areas = [math.pi * random.randint(5, 15)**2 for i in range(no_of_Balls)]
        # draw the plot
        plt.figure()
        plt.scatter(x, y, s=areas, c=colors, alpha=0.85)
        plt.axis([0.0, 1.0, 0.0, 1.0])
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()

    def CompareTwoPlots(self):
        math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
        science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
        marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

        plt.scatter(marks_range,math_marks,label='math marks',color='r')
        plt.scatter(marks_range,science_marks,label='science marks',color='g')
        plt.title("scatter plot")
        plt.xlabel('marks range')
        plt.ylabel('marks scored')
        plt.legend()
        plt.show()

def main():
     val= input("your opration: ")

     if val=="drawScatter":
        p1=TestSCatterplot()
        p1.DrawScatterPlot()
     elif val=="EmptyCircle":
        p1=TestSCatterplot()
        p1.EmptyCircle()
     elif val=="BallsWithDiffColor":
        p1=TestSCatterplot()
        p1.BallsWithDifferentColors()
     elif val=="SCatterPlot":
        p1=TestSCatterplot()
        p1.CompareTwoPlots()     
main()        


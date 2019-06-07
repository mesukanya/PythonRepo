import matplotlib.pyplot as plt
# with open("test.txt") as f:

class MyMatplot:

    def DrawLine(self):
        X = range(1, 50)
        Y = [value * 3 for value in X]
        print("Values of X:")
        print(*range(1,50)) 
        print("Values of Y (thrice of X):")
        print(Y)
        # Plot lines and/or markers to the Axes.
        plt.plot(X, Y)
        # Set the x axis label of the current axis.
        plt.xlabel('x - axis')
        # Set the y axis label of the current axis.
        plt.ylabel('y - axis')
        # Set a title 
        plt.title('Draw a line.')
        # Display the figure.
        plt.show()

    def PlotTwoOrMoreLines(self):
        # line 1 points
        x1 = [10,20,30]
        y1 = [20,40,10]
        
        # line 2 points
        x2 = [10,20,30]
        y2 = [40,10,30]
        
        plt.xlabel('x - axis')
        # Set the y axis label of the current axis.
        plt.ylabel('y - axis')
        # Set a title of the current axes.
        plt.title('Two or more lines on same plot with suitable legends ')
        # plotting the line 1 points 
        #plt.plot(x1, y1, label = "line 1")
        # plotting the line 2 points 
        #plt.plot(x2, y2, label = "line 2")
        # plt.plot(x1,y1, color='blue', linewidth = 3,  label = 'line1-width-3')
        # plt.plot(x2,y2, color='red', linewidth = 5,  label = 'line2-width-5')
        plt.plot(x1,y1, color='blue', linewidth = 3,  label = 'line1-dotted',linestyle='dotted')
        plt.plot(x2,y2, color='red', linewidth = 5,  label = 'line2-dashed', linestyle='dashed')
        # show a legend on the plot
        plt.legend()
        # Display a figure.
        plt.show()


def main():
    val= input("Your Opration: ")

    if val== "DrawLine":
       p1= MyMatplot()
       p1.DrawLine()    
    elif val=="PLotTwoOrMoreLines":
        p1= MyMatplot()
        p1.PlotTwoOrMoreLines() 
        

main()           
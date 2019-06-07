import matplotlib.pyplot as plt

class MyBarChart:

    def DisplayBarChart(self):

        x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
        popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        x_pos = [i for i, _ in enumerate(x)]

        plt.bar(x_pos,popularity,color=(0.4, 0.6, 0.8, 1.0),edgecolor='blue')

        plt.xlabel("Language")
        plt.ylabel("Popularity")

        plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
        plt.xticks(x_pos, x)
        # Turn on the grid
        plt.minorticks_on()  
        plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
        plt.grid(which='minor',linestyle='-',linewidth='0.5',color='black')

        plt.show()

    def HorizontalBarChart(self):
        x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
        popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        x_pose=[i for i,_ in enumerate(x)]
        plt.barh(x_pose,popularity,color='green')
        plt.xlabel("Popularity")
        plt.ylabel("Language")
        plt.title("Draw Horizonal bar chart")
        plt.yticks(x_pose, x)
        plt.minorticks_on()
        plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
        plt.grid(which='minor',linestyle=':',linewidth='0.5',color='green')
        plt.show()

    def DifferentColorForEachBar(self):
        x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
        popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        x_pos=[i for i,_ in enumerate(x)]
        plt.bar(x_pos,popularity,color=['red','purple','green','pink','yellow','blue','cyan'])
        plt.xlabel("Language")
        plt.ylabel("Popularity")
        plt.title("Draw Horizonal bar chart with different color")
        plt.xticks(x_pos,x)
        plt.minorticks_on()
        plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
        plt.grid(which='minor',linestyle=':',linewidth='0.5',color='black')
        plt.show()

    def TextLabelAboveBar(self):
        x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
        popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        x_pos=[i for i,_ in enumerate(x)]
        fig, ax = plt.subplots()
        rects1 = ax.bar(x_pos, popularity, color='b')
        plt.xlabel("Language")
        plt.ylabel("Popularity")
        plt.title("Text Label above bar")
        plt.xticks(x_pos,x)
        plt.minorticks_on()
        plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
        plt.grid(which='minor',linestyle=':',linewidth='0.5',color='black')
       
    def BorderColor(self)
        

    def autolabel(self,rects):
    # """
    # Attach a text label above each bar displaying its height
    # """
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
            '%f' % float(height),
            ha='center', va='bottom')    

def main():
    val= input("enter your opration: ")
    if val== "DisplayBarChart":
        p1=MyBarChart()
        p1.DisplayBarChart()
    elif val== "HorizontalBar":
        p1=MyBarChart()
        p1.HorizontalBarChart()
    elif val== "DifferentColorForEachBar":
        p1=MyBarChart()
        p1.DifferentColorForEachBar()
    elif val== "TextLabelAboveBar":
        p1=MyBarChart()
        p1.TextLabelAboveBar()
        p1.autolabel(rects1)    
main()                




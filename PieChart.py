import matplotlib.pyplot as plt
import pandas as pd

class TestPieChart:

  def DisplayPieChart(self):

        languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
        popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
        explode = (0.1,0,0,0,0,0)
        plt.pie(popuratity,explode=explode,labels=languages,colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
        plt.title("Piechart with title",bbox={'facecolor':'0.8','pad':5})
        # plt.axis("equal")
        plt.show()

  def WorkWIthCSV(self):
        df =  pd.read_csv('home/Documents/PythonTut/medal.csv')
        country_data = df["country"]
        medal_data = df["gold_medal"]
        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
        explode = (0.1, 0, 0, 0, 0)  
        plt.pie(medal_data, labels=country_data, explode=explode, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
        plt.title("Gold medal achievements of five most successful\n"+"countries in 2016 Summer Olympics")
        plt.show()          

def main():
    val= input("your opration: ")

    if val=="DisplayPieChart":
        p1=TestPieChart()
        p1.DisplayPieChart()
    elif val=="WorkWIthCSV":
        p1=TestPieChart()
        p1.WorkWIthCSV()
main()        


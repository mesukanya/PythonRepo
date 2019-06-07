import pandas as pd
import numpy as np

class MyPandas:

   def FindArraySeries(self):
       ds = pd.Series([2,4,6,8,10])
       print(ds)

   def SeriesToList(self):
       ds = pd.Series([2,4,6,8,10])
       print(ds)
       print("Type of series:")
       print(type(ds))
       print("series to list:")
       print(ds.tolist())
      # print(np.asarray(ds))
       print(type(ds.tolist()))
       
   def AddMultiplySubstract(self):
       ds1 = pd.Series([2, 4, 6, 8, 10])
       ds2 = pd.Series([1, 3, 5, 7, 9]) 

       ds = ds1+ds2
       print("Addition:",ds)

       ds = ds1-ds2
       print("Substraction:",ds)

       ds= ds1*ds2
       print("Multiplication:",ds)

       ds= ds1/ds2
       print("division:",ds)   

   def GetPowerOfAnArray(self): 
        x= np.arange(7)
        print("original array")
        print(x)
        print("First array elements raised to powers from second array, element-wise:")
        print(np.power(x, 3))

   def DataFrame(self):
       exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
       labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

       df= pd.DataFrame(exam_data,index=labels)
       print(df)


def main():
    val= input("Enter your OPration:")

    if val == "FindSeries":
       p1= MyPandas()
       p1.FindArraySeries()
    elif val== "SeriesToList":
        p1=MyPandas()
        p1.SeriesToList()   
    elif val== "AddMultiplySubstract":
        p1=MyPandas()
        p1.AddMultiplySubstract()
    elif val== "GetPowerOfAnArray":
        p1=MyPandas()
        p1.GetPowerOfAnArray()
    elif val== "DataFrame":
        p1=MyPandas()
        p1.DataFrame()    
main()         

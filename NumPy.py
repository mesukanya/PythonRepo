import numpy as np
from array import *
class NumPy:

    def ListIntoOneDimentionalArray(self):
        l = [12.23, 13.32, 100, 36.32]
        print("Original List:",l)
        a = np.array(l)
        print("One-dimensional numpy array: ",a)

    def CreateMatrix(self):
        xy =[[0,0,0],
            [0,0,0],
            [0,0,0]]
        val=2
        for x in range(len(xy)):
            for j in range(len(xy[0])):
                
                xy[x][j] = val
                val += 1
        print(xy)        
    
    def ReverseArray(self):
        arr= array('i',[12,13,14,15,16,17,18,19])
        lis= list(arr)
        lis.reverse()
        arr= np.array(lis)
        print(arr)

    def OneOnBorderAndZeroInside(self):
        #x = np.ones((5,5))
        x = np.ones((5,5))
        print("Original Array:")
        print(x)
        print("1 on border and zero inside")
        x[1:-1,1:-1] = 0 
        print(x)    

    def ZeroOnBorderAndONeInside(self):
        x = np.zeros((5,5))
        y = np.ones((3,3))
        print("Original Array:")
        print(y)
        print("Zeros on border")
        x[1:-1,1:-1] = 1 
        print(x) 

    def ConvertListAndTupleInArray(self):
        xList  = [1,2,3,4]
        yTuple = (6,6,6,6)

        print("Display List:",xList)
        print("Display Tuple:",yTuple)

        print("List to array:")
        print(np.asarray(xList))
        print("Tuple to array:")
        print(np.asarray(yTuple))



def main():
    v1 = ("OneDimentionalArray")
    v2 = ("CreateMatrix")
    v3 = ("ReverseArray")
    val = input("Enter your opration: ")
    if v1== val:
        p1= NumPy()
        p1.ListIntoOneDimentionalArray()
    elif v2== val:
        p1=NumPy()
        p1.CreateMatrix()
    elif v3== val:
        p1=NumPy()
        p1.ReverseArray()
    elif val == "OneOnBorder": 
        p1=NumPy()
        p1.OneOnBorderAndZeroInside()
    elif val == "ZeroOnBorder":
        p1=NumPy()
        p1.ZeroOnBorderAndONeInside()
    elif val == "ListAndTupleTOArray":
        p1=NumPy()
        p1.ConvertListAndTupleInArray()  

main()        

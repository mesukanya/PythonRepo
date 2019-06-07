
class LinerAlgebra:

    def AddTwoMatrix(self):
        X = [[12,7,3],
            [4 ,5,6],
            [7,8,9]]

        Y = [[5,8,1],
            [6,7,3],
            [4,5,9]]

        xy =[[0,0,0],
            [0,0,0],
            [0,0,0]]   

        for i in range(len(X)):
            for j in range(len(X[0])):
                xy[i][j] = X[i][j] + Y[i][j]

        for k in xy:
            print(xy)
     
    def Multiplication(self):

        X =[[12,7,3],
            [4 ,5,6],
            [7,8,9]]

        Y = [[5,8,1],
            [6,7,3],
            [4,5,9]]
        # Y = [9]

        xy =[[0,0,0],
            [0,0,0],
            [0,0,0]]   

       
        for i in range(len(X)):
            for j in range(len(X[0])):
                xy[i][j] = X[i][j] * Y[i][j]

        ######## for single value
        # for i in range(len(X)):
        #     for j in range(len(X[0])):
        #         xy[i][j] = X[i][j] * Y[0] 


def main():
   v1 = ("CalculateMatrix")
   v2 = ("Multiplication")
   val= input("Enter your opration: ")

   if v1 == val:
       p1 = LinerAlgebra()
       p1.AddTwoMatrix()
   elif v2 == val:
       p1 = LinerAlgebra()
       p1.Multiplication()   
       

main()       
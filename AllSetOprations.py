
class Myset:

    def __init__(self):
        return None

    def CreateSet(abc):
        setX = set()
        print(setX)

    def Itration(abc):
        setY = set([1,2,3,4,5])
        for i in setY:
           print(i) 

    def AddMember(abc):
        setX = set()
        setX.add("Purple")
        print(setX) 
        setX.update(["Red","Green"])  
        print(setX)   

    def CheckAndRemove(abc):
        r = set([1,2,3,4,5,6])
        myvar = input("Enter Your value: ")
        r.discard(myvar)
        print(r)
            
    
def main():
    v1 = ("Create")
    v2 = ("Itration")
    v3 = ("AddMember")
    v4 = ("CheckAndRemove")
    value = input("Plese enter the opration you wnat to perform: ")
    if v1 == value:
       p1 = Myset()
       p1.CreateSet()
    elif v2 == value:
       p1 = Myset()
       p1.Itration()
    elif v3 == value:
       p1.Myset()   
       p1.AddMember() 
    elif v4 == value:
       a1 = Myset()
       a1.CheckAndRemove()
    
main()         


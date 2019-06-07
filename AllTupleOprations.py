
class TupleOprations:

    def __init__(self):
        return None

    def CreateTuple(abc):
       tuplex= tuple()
       print(tuplex)

    def CreateTupleWithDifferentDataType(abc):
        tuplex=("tuple",True,3.55,1)
        print(tuplex)

    def UnpackTupleInDifferentVAariables(abc):
        tuplex=(2,1,3.55)
        print(tuplex)
        n1,n2,n3 = tuplex
        print(n1 + n2 + n3)
       # print(n1 + + n2 + + n3) 

    def FindRepeatedItems(abc):
        tuplex = (2,1,3,2,4,3,5,5)
        singlevalue = []
        duplicatevalue = []
        print(tuplex)
        listy=list(tuplex)
        for i in listy:
          
            if i not in singlevalue:
                singlevalue.append(i)
            else:
                duplicatevalue.append(i)
        tuplex = tuple(duplicatevalue)
        print(tuplex)

    def ElementExistsWithinTuple(abc):
        tuplex = (2,1,3,2,4,5,5)
        print(tuplex)

        val = input("Enter your value: ")
        print(val in tuplex)

        # if val in tuplex:
        #     print("I am one of them")

def main():

    v1 = ("CreateTuple")
    v2 = ("DifferentDataTypes")
    v3 = ("UnpackTuple")
    v4 = ("RepeatedItems")
    v5 = ("CheckExistingValue")
    val = input("Enter your opration: ")   
    if v1 == val:
        p1 = TupleOprations()
        p1.CreateTuple()
    elif v2 == val:
        p1 = TupleOprations()
        p1.CreateTupleWithDifferentDataType()  
    elif v3 == val:
        p1 = TupleOprations()
        p1.UnpackTupleInDifferentVAariables()     
    elif v4 == val:
        p1 = TupleOprations()
        p1.FindRepeatedItems()
    elif v5 == val:
        p1 = TupleOprations()
        p1.ElementExistsWithinTuple()    
main()            
 
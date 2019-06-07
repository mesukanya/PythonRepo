
class ListClass:

    def  __init(self):
        return None

    def RemoveSpecificElements(abc):
        v1 =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        value = input("Enter number: ")
        v1.remove(value)

        print(v1)

    def CheckCommonValueInList(abc):
        v1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        v2 = ['Red', 'Green', 'White', 'Black', 'Purple', 'Brown']

        for i in v1:
            for j in v2:
                if i == j:
                   print(i)

    def RemoveDuplicates(abc):
        v1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','Yellow','Pink','Pink']
        v2 = []
        for i in v1:
            if i not in v2:
                v2.append(i)
            else:
                v1.remove(i)
        print(v2)   

    def FindSmallestNumber(abc):
        v1 = [2,5,3,1,5]         
        print("Smallest number is ", min(v1))   

    def SumAllNumber(abc):
        finalvalue = 0
        v1 = [2,5,3,1,5]    

        for i in v1:
           finalvalue = finalvalue + i
        print("Sum of all list elements is ", finalvalue)    

                       
def main():
    v1 = ("Remove")
    v2 = ("CheckCommon")
    v3 = ("RemoveDuplicate")
    v4 = ("SmallestNumber")
    v5 = ("Addition")
    val = input("Enter your opration: ")

    if v1 == val:
        p1 = ListClass()
        p1.RemoveSpecificElements()
    elif v2 == val:
        p1 = ListClass()
        p1.CheckCommonValueInList()
    elif v3 == val:
        p1 = ListClass()
        p1.RemoveDuplicates()
    elif v4 == val:
        p1 = ListClass()
        p1.FindSmallestNumber()   
    elif v5  == val:
        p1 = ListClass()
        p1.SumAllNumber() 
main()     
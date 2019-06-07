class DictionaryKey:

    def __init__(self, no):
        self.no = no

    def __init__(self):
       return None

    def MyFun(abc):
        SampleDict = {0:10, 1:20}
        print("Sample dictionary is ",SampleDict)
        
        SampleDict.update(abc.no)
        print ("Sample dictionary after adding value ",SampleDict)

    def ConcatinateFun(abcd):
        dic1 = {1:10, 2:20}
        dic2 = {3:30, 4:40}
        dic3 = {5:50, 6:60}
        dic4 = {}
        for d in (dic1, dic2, dic3):
            dic4.update(d)
        print(dic4)


# p1 = DictionaryKey({2:30})
# p1.MyFun()
def main():
    variable1=("Add value")
    variable2=("Concatinate value")
    value = input("Enter your opration : ")
    if variable1 == value:
        p1 = DictionaryKey({2:30})
        p1.MyFun()
    elif variable2 == value:
        p1 = DictionaryKey()
        p1.ConcatinateFun()
             

main()             
                 

    



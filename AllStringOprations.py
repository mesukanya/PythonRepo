
class MyString:

    def __init__(self):
        return None

    def FindSTringLength(abc):
        val = ("Sukanya")
        print("STring length is ",len(val))

    def CalculateStringCount(self,string):
        dict = {}
        keys = dict.keys()
        for x in string:
           if x in keys:
               dict[x] += 1
           else:
               dict[x] = 1  
        print(dict)   

    def ChangeAllOccurenceOfFirstCharecter(self,val):
        char = val[0]
        val = val.replace(char, '$')
        val = char + val[1:]
        print(val)             

    def ChangeString(self,val):
        v1 = val[-3:]

        if v1 == "ing":
            val += 'ly'
        else:
            val += 'ing'
        print(val)

    def ChangeStringInUpperLowerCase(self,val):

        print("STring in upper case: ", val.upper())
        print ("string in lower case: ", val.lower())

def main():
    v1 = ("CalculateLength")
    v2 = ("CalculateCount")
    v3 = ("ChangeOccurance")
    v4 = ("ChangeTring")
    v5 = ("Changecase")
    val = input("Enter your opration: ")

    if v1 == val:
        p1 = MyString()
        p1.FindSTringLength()
    elif v2 == val:
        p1 = MyString()
        val = input("Enter your value: ")
        p1.CalculateStringCount(val)
    elif v3 == val:
        p1 = MyString()
        val = input("Enter your value: ")
        p1.ChangeAllOccurenceOfFirstCharecter(val)
    elif v4 == val:
        p1 = MyString()
        val = input("Enter your value: ")
        p1.ChangeString(val)
    elif v5 == val:
        p1 = MyString()
        val = input("Enter your value: ")
        p1.ChangeStringInUpperLowerCase(val)    
main()         
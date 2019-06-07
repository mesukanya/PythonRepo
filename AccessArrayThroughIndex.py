
from array import *
ArrayValue = array('i',[1,3,5,7,9])
for i in ArrayValue:
    print(i)
print("Access array values using index")
print(ArrayValue[0])
print(ArrayValue[1])
print(ArrayValue[2])

print("Reverse the order of array")

ArrayValue.reverse()
print(ArrayValue)

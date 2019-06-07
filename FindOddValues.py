def Diff(li1, li2): 
    return (list(set(li1) - set(li2))) 
  
# Driver Code 
li1 = set(["White", "Black", "Red"]) 
li2 = set(["Red", "Green"])
print(Diff(li1, li2)) 
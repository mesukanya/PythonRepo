y = {'carl':40,'alan':2,'bob':1,'danny':3}

i = list(y.items())

i.sort()


print("Acending order ", i)

i = list(y.items())

i.sort(reverse=True)
print("DEcending order ", i)

Dict = dict(i)

print(Dict)


    # Take a Dictionary.
    # Convert it in a list.
    # Now sort the list in ascending or Descending order.
    # Convert again The sorted list to dictionary.
    # Print Output

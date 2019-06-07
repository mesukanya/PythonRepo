
from datetime import date

def diff_dates(date1, date2):
    return abs(date2-date1).days

def main():
    d1 = date(2019,2,15)
    d2 = date(2019,2,28)
    result1 = diff_dates(d2, d1)
 
    print(result1)

main()


# from datetime import date

# FirstDate = input("Enter a Firstdate in YYYY-MM-DD format: ")
# SecondDate = input("Enter a Second in YYYY-MM-DD format: ")

# if FirstDate < SecondDate:
#     print("FirstDate should be greater that 2nd date")
# else:
#     Count = str((FirstDate-SecondDate).days)
#     print("No of dayes " , str)





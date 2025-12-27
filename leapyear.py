year = int(input("enter the year : "))
if(year % 400 == 0 and year % 100 != 0):
    print("the year is an leap year : ", year)
elif(year % 4 == 0):
    print("the year is an leap year : ", year)
else :
    print("it is not an leap year : ", year)

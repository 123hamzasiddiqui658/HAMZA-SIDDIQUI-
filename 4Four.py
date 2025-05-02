def  Agecalculator(y,m,d):
     import datetime
     today=datetime.datetime.now().date()
     dob=datetime.date(y,m,d)
     age=int((today-dob).days/365.25)
     print(age)
y=int(input("Enter Year of Birth:"))
m=int(input("Enter month of Birth:"))
d=int(input("Enter Date of Birth:"))

Agecalculator(y,m,d)
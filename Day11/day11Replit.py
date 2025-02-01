leapYear = input("Do you want the calculations for a leap year? Yes or no?")

if leapYear == "yes" or "Yes":
  seconds = 60
  minutes = 60
  hours = 24
  days = 366
  print(seconds*minutes*hours*days)
else:
  seconds = 60
  minutes = 60
  hours = 24
  days = 365
  print(seconds*minutes*hours*days)
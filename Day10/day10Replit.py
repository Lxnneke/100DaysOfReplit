myBill = float(input("What was the bill?: "))
tip = int(input("What percent tip do you want to leave: 15, 18, or 20 percent?"))
price = myBill + (myBill * (tip/100))
numberOfPeople = int(input("How many people?: "))
answer = price / numberOfPeople
print("You all owe", round(answer, 2))

print("==Final Grade Calculator==")
print()
print()
maxScore = float(input("What is the maximal score you could get?  >  "))
score = float(input(("What score did you get?  >  ")))
print()
print()
finalScore = round(score/maxScore*100, 2)
print("Your percentile is", finalScore, "%")
if finalScore >= 90:
  print("You got an A+! 🥳")
elif finalScore >= 80 and finalScore < 90:
  print("You got an A! 😁")
elif finalScore >= 70 and finalScore < 80:
  print("You got a B! 😊")
elif finalScore >= 60 and finalScore < 70:
  print("You got a C! 🙂")
elif finalScore >= 50 and finalScore < 60:
  print("You got a D! 😕")
else: 
  print("Ouch, you didn't get marked!")
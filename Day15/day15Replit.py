print("Animal sound maker!")
print()
animal = input("What animal do you want?  >  ")
if animal == "cow":
  print("A Cow goes moo!")
  exit = ""
  while exit != "yes":
    exit = input("Do you want to exit?  >  ")
    print("The Cow goes moo!")
elif animal == "dog":
  print("A Dog goes woof!")
  exit = ""
  while exit != "yes":
    exit = input("Do you want to exit?  >  ")
    print("The Dog goes woof!")
elif animal == "cat":
  print("A Cat goes miauw!")
  exit = ""
  while exit != "yes":
    exit = input("Do you want to exit?  >  ")
    print("The Cat goes miauw!")
elif animal == "sheep":
  print("A sheep goes baah!")
  exit = ""
  while exit != "yes":
    exit = input("Do you want to exit?  >  ")
    print("The Sheep goes baah!")
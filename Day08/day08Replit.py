print("======Daily bit of kindness======")
print("    Just to cheer up your day!   ")
print()
name = input("What is your name?  >    ")
print("\033[33m",name, "\033[0m")
print()
print()
day = input("What day is it today?  >    ")
print("\033[33m",day, "\033[0m")
print()
print()
hobbies = input("And what is one of your hobbies?  >    ")
print("\033[33m",hobbies, "\033[0m")
print()
print("Generating your daily kindness message...")
if hobbies == "coding":
  print("Hello", name, "! I hope that this", day, "will be a great day for you. I hope you get to do some", hobbies, "and learn something new. I hope you have a great day!")
elif hobbies == "dancing":
  print("Hello", name, "! I hope that this", day, "will be a great day for you. I hope you get to do some", hobbies, "and you will be able to move along to the music to your hearts content!")
elif hobbies == "writing":
  print("Hello", name, "! I hope that this", day,"will help you to achieve some of your goals, and you will be able to write something new. I hope you will enjoy", hobbies, "today!")
else: 
  print("Hello", name, "! I hope that this", day, "will be a great day for you, where you will be able to enjoy", hobbies)

print("Name the Lyrics game!")
print("(Type in the blank lyrics and see if you are as cool as me.)")
print()
print()
counter = 1
while True:
  lyrics = input("I don't wanna ______ a thing. ")
  if lyrics == "miss" or lyrics == "Miss":
    print("You got it!")
  else:
    print("Nope! Try again!")
    counter +=1
  if lyrics == "miss" or lyrics == "Miss":
    break
print("Thanks for playing!")
print("You got the correct lyrics in", counter, "attempt(s).")
  
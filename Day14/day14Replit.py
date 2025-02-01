from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E")
print()
print("Select your move (R, P or S)")
print()
player1Move = input("Player 1 > ")
player2Move = input("Player 2 > ")
print()
if player1Move == "R" and player2Move == "R":
  print("You both picked Rock, draw!")
elif player1Move == "R" and player2Move == "P":
  print("Player 2 beat Player 1 with Paper!")
elif player1Move == "R" and player2Move == "S":
  print("Player 1 beat Player 2 with Rock!")
elif player2Move =="R" and player1Move == "P":
  print("Player 1 beat Player 2 with Paper!")
elif player2Move == "R" and player1Move == "S":
  print("Player 2 beat Player 1 with Rock!")
elif player1Move == "P" and player2Move == "P":
  print("You both picked Paper, draw!")
elif player1Move == "S" and player2Move == "S":
  print("You both picked Scissors, draw!")
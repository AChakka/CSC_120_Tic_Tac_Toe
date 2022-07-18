board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


game_still_going = True


winner = None

current_player = "X"




def play_game():


  print_board()


  while game_still_going:

    handle_turn(current_player)



 
    switch_turn()
  
  if winner == "X" or winner == "O":
    print(winner + " wins!")
  elif winner == None:
    print("Tied Match.")



def print_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2]  )
  print(board[3] + " | " + board[4] + " | " + board[5]  )
  print(board[6] + " | " + board[7] + " | " + board[8]  )
  print("\n")



def handle_turn(player):

  print(player + "'s turn.")
  position = input("Choose a square from 1 to 9: ")


  valid = False
  while not valid:

    
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a square from 1 to 9: ")
 
    
    position = int(position) - 1

    
    if board[position] == "-":
      valid = True
    else:
      print("You can't place there. Try again")

  
  board[position] = player

  
  print_board()




def switch_turn():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"



play_game()

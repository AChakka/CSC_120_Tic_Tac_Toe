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


    check_game_over()

 
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



def check_game_over():
  check_winner()
  check_tie()



def check_winner():
  global winner
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


def check_rows():
  global game_still_going
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  if row_1 or row_2 or row_3:
    game_still_going = False
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  else:
    return None


def check_columns():
  global game_still_going
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  if column_1 or column_2 or column_3:
    game_still_going = False
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  else:
    return None


def check_diagonals():
  global game_still_going
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  if diagonal_1 or diagonal_2:
    game_still_going = False
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  else:
    return None



def check_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
    return True
  else:
    return False


def switch_turn():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"



play_game()

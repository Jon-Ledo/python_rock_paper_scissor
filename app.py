import random

def play():
  user = input("What's your choice? 'r' for rock, 'p' for paper, and 's' for scissors \n")
  computer = random.choice(['r', 'p', 's'])

  if user == computer:
    return 'tie'
  # In this game, we know that
  # rock > scissor
  # paper > rock
  # scissors > paper

  if is_win(user, computer):
    return 'You win!'

  return 'You lost!' 

def is_win(player, opponent):
  # return true if player wins
  if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
    return True

print(play())
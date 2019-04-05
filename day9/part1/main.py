#!/usr/bin/env python3

import sys

class MarbleMania:
  def __init__(self, num_players, last_marble):
    self.marbles =[0]
    self.current_marble = 0 #index of current marble
    self.next_marble = 1 #value of next marble to be added
    self.num_players = num_players
    self.player_scores = [0] * self.num_players
    self.current_player = 0
    self.last_marble = last_marble

  def print(self):
    for i in range(len(self.marbles)):
      if i == self.current_marble:
        sys.stdout.write('({}) '.format(self.marbles[i]))
      else:
        sys.stdout.write('{} '.format(self.marbles[i]))
    print('')

  def add_marble(self):
    if self.next_marble % 23 == 0:
      #keep next marble
      self.player_scores[self.current_player] += self.next_marble
      self.next_marble += 1

      #remove marble 7 CCW, add to current player score, and update current marble
      self.player_scores[self.current_player] += self.marbles[(self.current_marble-7)%len(self.marbles)] # negative modulo is ok in python
      self.current_marble = (self.current_marble-7)%len(self.marbles)
      del self.marbles[(self.current_marble)%len(self.marbles)]
    else:
      LHM = (self.current_marble+1)%len(self.marbles)
      self.marbles = self.marbles[:LHM+1] + [self.next_marble] + self.marbles[LHM+1:]
      self.current_marble = LHM+1
      self.next_marble+=1

    self.current_player = (self.current_player+1)%self.num_players
    if self.next_marble > self.last_marble:
      #game is done
      return True
    else:
      return False

  def play_game(self):
    #add marlbes until game is over
    while not self.add_marble():
      pass

    #game is over, print high score
    print(max(self.player_scores))

#example inputs
#MarbleMania(5, 25).play_game()
#MarbleMania(10, 1618).play_game()
#MarbleMania(13, 7999).play_game()
#MarbleMania(17, 1104).play_game()
#MarbleMania(21, 6111).play_game()
#MarbleMania(30, 5807).play_game()
MarbleMania(419, 72164).play_game()

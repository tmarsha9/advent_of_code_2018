#!/usr/bin/env python3

import sys

class MarbleMania:
  class List:
    class Node:
      def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    def __init__(self):
      self.head = self.Node(0) # points to "current marble"
      self.head.next = self.head
      self.head.prev = self.head

    def print(self):
      n = self.head.next
      while n != self.head:
        sys.stdout.write('{} '.format(n.value))
        n = n.next
      sys.stdout.write('{}\n'.format(self.head.value))

    def add_marble(self, value):
      new = self.Node(value)
      self.head = self.head.next

      #perform insert after head
      new.prev = self.head
      new.next = self.head.next

      self.head.next.prev = new
      self.head.next = new

      #update to make newly added item the current marble
      self.head = new

    def process_multiple_of_23(self):
      """returns value of removed item"""

      self.head = self.head.prev.prev.prev.prev.prev.prev.prev

      #remove self.head from list
      new_head = self.head.next

      self.head.prev.next = self.head.next
      self.head.next.prev = self.head.prev

      rv = self.head.value
      del self.head
      self.head = new_head

      return rv

  def __init__(self, num_players, last_marble):
    self.marbles = self.List()
    self.next_marble = 1 #value of next marble to be added
    self.num_players = num_players
    self.player_scores = [0] * self.num_players
    self.current_player = 0
    self.last_marble = last_marble

  def add_marble(self):
    if self.next_marble % 23 == 0:
      # don't add next marble to circle, just add to score
      self.player_scores[self.current_player] += self.next_marble

      #also remove marble 7 CCW and add to score
      self.player_scores[self.current_player] += self.marbles.process_multiple_of_23()
    else:
      self.marbles.add_marble(self.next_marble)

    self.current_player = (self.current_player+1)%self.num_players
    self.next_marble+=1
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

#technically input from part 1, but used as another test
#MarbleMania(419, 72164).play_game()

MarbleMania(419, 7216400).play_game()

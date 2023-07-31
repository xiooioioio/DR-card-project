# Example list
from card import Card  
import random 
shuffled_deck = Card.new_deck()

class Player():
  def __init__(self, deck, hand, score):
    self.deck = deck
    self.hand = hand
    self.score = score

class Human(Player):
    def __init__(first_half, six_cards, 0)

class Computer(Player):
    def __init__(second_half,sixcards2, 0)


def six_cards(first_half):
   return first_half[:6]

def six_cards2(second_half):
   return first_half[:6]



# Calculate the midpoint to split the list
midpoint = len(shuffled_deck) // 2

# Split the list into two halves
first_half = shuffled_deck[:midpoint:]
second_half = shuffled_deck[midpoint:]

# Randomize the order of elements in each split
random.shuffle(first_half)
random.shuffle(second_half)

# Print the results
print("First Half (Randomized):", first_half)
print("Second Half (Randomized):", second_half)







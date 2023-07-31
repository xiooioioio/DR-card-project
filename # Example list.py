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


def draw(cards):
       print(first_half)
      
    


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
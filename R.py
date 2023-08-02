from card import Card
import random

shuffled_deck = Card.new_deck()

class Player():
    def __init__(self, deck, hand, score):
        self.deck = deck
        self.hand = hand
        self.score = score

class Human(Player):
    def __init__(self, deck):
        first_half = deck[:len(deck) // 2]  # Get the first half of the deck
        self.hand = first_half[:6]  # Draw six cards from the first half
        self.score = 0  # Initialize the score to zero

class Computer(Player):
    def __init__(self, deck):
        second_half = deck[len(deck) // 2:]  # Get the second half of the deck
        self.hand = second_half[:6]  # Draw six cards from the second half
        self.score = 0  # Initialize the score to zero

# Calculate the midpoint to split the list
midpoint = len(shuffled_deck) // 2

# Split the list into two halves
first_half = shuffled_deck[:midpoint]
second_half = shuffled_deck[midpoint:]

# Randomize the order of elements in each split
random.shuffle(first_half)
random.shuffle(second_half)

# Create instances of Human and Computer players
human_player = Human(first_half)
computer_player = Computer(second_half)

# Print the results
print("First Half (Randomized):", first_half)
print("Second Half (Randomized):", second_half)

# Print the hands of each player
print("Human's Hand:", human_player.hand)
print("Computer's Hand:", computer_player.hand)

# Find the highest card in the computer player's hand
highest_card = None
for card in computer_player.hand:
    if highest_card is None or card.value > highest_card.value:
        highest_card = card

print("Computer's Highest Card:", highest_card)









           



  
 






# Example list
from card import Card  
import random 
shuffled_deck = Card.new_deck()

# Calculate the midpoint to split the list
midpoint = len(shuffled_deck) / 2

# Split the list into two halves
first_half = shuffled_deck[:midpoint]
second_half = shuffled_deck[midpoint:]

# Randomize the order of elements in each split
random.shuffle(first_half)
random.shuffle(second_half)

# Print the results
print("First Half (Randomized):", first_half)
print("Second Half (Randomized):", second_half)







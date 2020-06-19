import random
from treys import Card, Deck, Evaluator

evaluator = Evaluator()
deck = Deck()

print("1v1 Texas Hold'em")

# Draw flop, turn, and river respectively
flop = deck.draw(3)
turn = deck.draw(1)
river = deck.draw(1)
board = flop + [turn] + [river]

hand1 = deck.draw(2)
hand2 = deck.draw(2)
hands = [hand1, hand2]

print("Board:", Card.print_pretty_cards(board))
evaluator.evaluate(board, hand1)

print("Summary:")
evaluator.hand_summary(board, hands)

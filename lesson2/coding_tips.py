# Magic Numbers

NUMBERS_CARDS_IN_HAND = 5

def deal_hand():
    hand = []
    for card_number in range(NUMBERS_CARDS_IN_HAND):
        hand.append(deal_hand())

    return hand

answer = ''
while answer.lower() != 'n':
    print('Continue? (y/n)')
    answer = input()
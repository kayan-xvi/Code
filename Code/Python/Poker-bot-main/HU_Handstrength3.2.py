﻿# The aim of this program is to tell you what your chance of winning the hand is  
 
def make_deck(): 
    '''
    Creates the deck of cards to use
    '''
    suits = ['♠','♣','♥','♦']
    values = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    cards = []
    n = 0
    for suit in range(len(suits)): 
        for value in range(len(values)): 
            cards.append([values[value], suits[suit]])
            n += 1 
    return cards

#---------------------

def convert(deck):
    '''
    Turns all of the letter values into numbers as easier to work with
    '''
    for n in range(len(deck)): 
        #print(deck[n][0])
        if deck[n][0] == 'A': 
            deck[n][0] = 14
        if deck[n][0] == 'K': 
            deck[n][0] = 13 
        if deck[n][0] == 'Q': 
            deck[n][0] = 12
        if deck[n][0] == 'J': 
            deck[n][0] = 11  
    #print(deck)
    return deck
    
#---------------------

def reconvert(deck):
    '''
    Turns all of the numbers into letters for visual purposes 
    '''
    for n in range(len(deck)): 
        #print(deck[n][0])
        if deck[n][0] == 14: 
            deck[n][0] = 'A'
        if deck[n][0] == 13: 
            deck[n][0] = 'K' 
        if deck[n][0] == 12: 
            deck[n][0] = 'Q'
        if deck[n][0] == 11: 
            deck[n][0] = 'J'  
    #print(deck)
    return deck
    
#---------------------

def pick_card(deck):
    '''
    Picks a card and removes this card from the deck, returning this card in form: [value,suit]
    '''
    #print('hand initiated')
    #print(deck)
    import random
    card1n = 52
    #while card1n not in deck: 
     #   pass
    #print(card1n)
    #print('lendeck = {}'.format(len(deck)))
    card1n = random.randint(0,len(deck)-1)
    #print(card1n)
        #print(card2n)
    #print('card1n = {}, card2n = {}'.format(card1n,card2n))
    card1 = deck[card1n]
    #print(card1)
    #print(deck[card1n])
    #print('card1 = {}, card2 = {}'.format(card1,card2))
    card = [card1[0],card1[1]]
    deck.remove(card1)
    #print(len(deck))
    return card, deck

#---------------------

def card_data(cards): 
    '''
    This turns the cards chosen into data to work with for hand classification
    '''
    suits = []
    values = []
    for card in range(len(cards)):
        values.append(cards[card][0])
        suits.append(cards[card][1])
    valuecount = [values.count(i) for i in values]
    suitcount = [suits.count(i) for i in suits]
    dif = max(values) - min (values)
    return valuecount, dif, suitcount, values
    
#---------------------

def royal(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0 
    if max(valuecount) == 1 and 5 in suitcount and dif == 4 and 14 in cards:  
        strength = 9
        values.sort(reverse = True)
        for i in range(len(values)):
            strength *= 100 
            strength += values[i]
    return strength

#---------------------

def strflu(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0 
    if max(valuecount) == 1 and 5 in suitcount and dif == 4:
        strength = 8
        values.sort(reverse = True)
        for i in range(len(values)):
            strength *= 100 
            strength += values[i]
    return strength

#---------------------

def strwheel(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0
    if 5 in suitcount and 5 in values and 4 in values and 3 in values and 2 in values and 14 in values:
        strength = 8
        values.sort(reverse = True)
        values.remove(14)
        values.append(14)
        for i in range(len(values)):
            strength *= 100 
            strength += values[i]
    return strength
    
#---------------------

def quad(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0 
    if 4 in valuecount: 
        strength = 7
        for i in range(len(values)): 
            if valuecount[i] == 4: 
                n = values[i]
                for j in range(4):
                    strength *= 100 
                    strength += n
                break
        values.sort(reverse = True)
        for k in range(len(values)): 
            if values[k] != n:
                strength *= 100 
                strength += values[k]
    return strength

#---------------------

def fh(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0 
    n = 0 
    m = 0
    if 3 in valuecount and 2 in valuecount:
        strength = 6
        for i in range(len(values)): 
            if valuecount[i] == 3: 
                n = values[i]
                for j in range(3):
                    strength *= 100 
                    strength += n
                break
        for i in range(len(values)): 
            if valuecount[i] == 2: 
                m = values[i]
                for j in range(2):
                    strength *= 100 
                    strength += m
                break
    return strength

#---------------------

def flu(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0 
    if 5 in suitcount:
        strength = 5
        values.sort(reverse = True)
        for i in range(len(values)):
            strength *= 100 
            strength += values[i]
    return strength

#---------------------

def stra(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0 
    if max(valuecount) == 1 and dif == 4 or [14,2,3,4,5] in values: 
        strength = 4
        values.sort(reverse = True)
        for i in range(len(values)):
            strength *= 100 
            strength += values[i]
    return strength 

#---------------------

def wheel(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0
    if 5 in values and 4 in values and 3 in values and 2 in values and 14 in values:
        strength = 8
        values.sort(reverse = True)
        values.remove(14)
        values.append(14)
        for i in range(len(values)):
            strength *= 100 
            strength += values[i]
    return strength
    
#---------------------

def trip(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0 
    if 3 in valuecount: 
        strength = 3
        for i in range(len(values)): 
            if valuecount[i] == 3: 
                n = values[i]
                for j in range(3):
                    strength *= 100 
                    strength += n
                break
        values.sort(reverse = True)
        for k in range(len(values)): 
            if values[k] != n:
                strength *= 100 
                strength += values[k]
    return strength 
    
#---------------------

def twopair(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0 
    n = 0 
    m = 0 
    pairs = []
    if valuecount.count(2) == 4: 
        strength = 2
        for i in range(len(values)): 
            if valuecount[i] == 2: 
                n = values[i]
                break
        for i in range(len(values)):
            if valuecount[i] == 2 and values[i] != n: 
                m = values[i]
                break
        pairs.append(n)
        pairs.append(m)
        pairs.sort(reverse = True)
        for j in range(2): 
            for l in range(2):
                strength *= 100 
                strength += pairs[j]
        values.sort(reverse = True)
        for k in range(len(values)): 
            if values[k] != n and values[k] != m :
                strength *= 100 
                strength += values[k]
    return strength
    
#---------------------

def pair(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    strength = 0 
    n = 0
    if 2 in valuecount: 
        strength = 1
        for i in range(len(values)): 
            if valuecount[i] == 2: 
                n = values[i]
                for j in range(2):
                    strength *= 100 
                    strength += n
                break
        values.sort(reverse = True)
        for k in range(len(values)): 
            if values[k] != n:
                strength *= 100 
                strength += values[k]
    return strength

#---------------------

def high(cards): 
    valuecount, dif, suitcount, values = card_data(cards)
    # This autogives a strength of 0 
    strength = 0 
    values.sort(reverse = True)
    for i in range(len(valuecount)):
        strength *= 100 
        strength += values[i]
    return strength
    
#---------------------

def hand_value(cards): 
    '''
    This applies the classification of the hand to the strength
    '''
    strength = 0
    if strength == 0: 
        strength = royal(cards)
    if strength == 0:
        strength = strflu(cards)
    if strength == 0:
        strength = strwheel(cards)
    if strength == 0:
        strength = quad(cards)
    if strength == 0:
        strength = fh(cards)
    if strength == 0:
        strength = flu(cards)
    if strength == 0:
        strength = stra(cards)
    if strength == 0:
        strength = wheel(cards)
    if strength == 0:
        strength = trip(cards)
    if strength == 0: 
        strength = twopair(cards)
    if strength == 0: 
        strength = pair(cards)
    if strength == 0: 
        strength = high(cards)
    return strength

#---------------------

def hand_type(strength):
    power = strength//(10**10)
    classif = ''
    if power == 0: 
        classif = 'High card'
    if power == 1: 
        classif = 'Pair'
    if power == 2: 
        classif = 'Two pair'
    if power == 3: 
        classif = 'Three of a kind'
    if power == 4: 
        classif = 'Straight'
    if power == 5: 
        classif = 'Flush'
    if power == 6: 
        classif = 'Full house'
    if power == 7: 
        classif = 'Four of a kind'
    if power == 8: 
        classif = 'Straight flush'
    if power == 9: 
        classif = 'Royal flush'
    return classif

#---------------------

def judge_value(cards):
    '''
    This function judges the value of any hand put into it in format [[value,suit], ...]
    '''
    converted = convert(cards)
    handstrength = hand_value(converted)
    #print('This is your hands value:')
    #print(handstrength)
    #print('This is your type of hand:')
    #print(hand_type(handstrength))
    return handstrength
    
#---------------------

def make_hand(deck, hand, size): 
    '''
    This function creates a hand of size, size or adds size cards to a hand from deck
    '''
    printout = ''
    reconvert(hand)
    for i in range(size): 
        card, deck = pick_card(deck)
        hand.append(card)
    for i in range(len(hand)):
        for j in range(2):
            printout += str(hand[i][j]) 
        printout += '  '
    return hand, printout, deck

#---------------------

def single_hand(hand, size): 
    '''
    This function finds the best hand of size 5 possible from all given cards 
    '''
    possible = [] 
    maxstrength = 0
    maxhand = []
    for single in itertools.combinations(hand,5): 
        #print('single')
        #print(list(single))
        possible.append(list(single))
    #print(len(possible))
    for hands in possible: 
        #print(hand)
        handstrength = judge_value(hands)
        #print('\n')
        if handstrength > maxstrength:
            maxstrength = handstrength
            #print('TEST: {}'.format(hand))
            maxhand = hands
    #print('Best possible hand:')
    #print(maxhand)
    print(hand_type(maxstrength))
    #print(maxstrength)
    return maxhand, maxstrength

#---------------------
#print(
'''
Hand strength: 
Type-highest-high-middle-low-lowest

Hand type : 
royal = 09 = Royal flush 
strflu = 08 = Straight flush
quad = 07 = Four of a kind
fh = 06 = Full house 
flu = 05 = Flush
stra = 04 = Straight
trip = 03 = Three of a kind 
twopair = 02 = Two pair 
pair = 01 = Pair
high = 00 = High card
'''
#)
#print(
'''
Hand cards: 
14 Ace 
13 King 
12 Queen 
11 Jack 
10 
09 
08 
07
06
05
04
03
02
'''
#)

#---------------------
# MAIN EXECUTION
#---------------------

import itertools
deck = make_deck()
#print(deck)
#temp = ''
p_hand = []
p_hand, p_print, deck = make_hand(deck, p_hand, 2)

print('This is your hand:')
print(p_print)
print('\n')

p_strength = judge_value(p_hand)

c_hand = []
c_hand, c_print, deck = make_hand(deck, c_hand, 2)

print('This is comp hand:')
print(c_print)
print('\n')

#p_strength = judge_value(p_hand)

#print(p_strength)

board = []

board, b_print, deck = make_hand(deck, board, 3)
print('This is the flop:')
print(b_print)
for card in board: 
    p_hand.append(card)
    c_hand.append(card)

print('\nYour hand:')
p_hand, p_strength = single_hand(p_hand, 5)
print('Comp hand:')
c_hand, c_strength = single_hand(c_hand, 5)

board, b_print, deck = make_hand(deck, board, 1)
print('\nThis is the turn:')
print(b_print)
for card in board: 
    if card not in p_hand:
        p_hand.append(card)
    if card not in c_hand:
        c_hand.append(card)
        #print(p_hand)

print('\nYour hand:')
p_hand, p_strength = single_hand(p_hand, 5)
print('Comp hand:')
c_hand, c_strength = single_hand(c_hand, 5)

board, b_print, deck = make_hand(deck, board, 1)
print('\nThis is the river:')
print(b_print)
for card in board: 
    if card not in p_hand:
        p_hand.append(card)
    if card not in p_hand:
        c_hand.append(card)
        #print(p_hand)



print('\nYour hand:')
p_hand, p_strength = single_hand(p_hand, 5)
reconvert(p_hand)
print(p_hand)
print('Comp hand:')
c_hand, c_strength = single_hand(c_hand, 5)
reconvert(c_hand)
print(c_hand)

if p_strength > c_strength: 
    print('Your won')
elif p_strength < c_strength:
    print('You lose')
else: 
    print('You tied')











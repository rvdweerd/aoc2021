# This is Q21-part2

from itertools import product
from functools import lru_cache

DICE_ROLLS = []
for dice in product(range(1, 4), range(1, 4), range(1, 4)):
    DICE_ROLLS.append(sum(dice))

mem={} # our cache for dp mem

#@lru_cache(maxsize=None) # could use decorator for caching
def play(my_pos, my_score, other_pos, other_score):#, mem={}):
    state=(my_pos,my_score,other_pos,other_score)
    
    if state not in mem:
        if my_score >= 21:
            return (1, 0)
        if other_score >= 21:
            return (0, 1)

        my_wins = other_wins = 0
        for roll in DICE_ROLLS:
            # Play one turn:
            new_pos   = (my_pos + roll) % 10
            new_score = my_score + new_pos + 1

            # Other player play:
            ow, mw = play(other_pos, other_score, new_pos, new_score)

            # Update total wins:
            my_wins    += mw
            other_wins += ow
        mem[state] = (my_wins,other_wins)
    return mem[state] #my_wins, other_wins

p1_pos0 = 10
p2_pos0 = 6

wins = play(p1_pos0-1, 0, p2_pos0-1, 0)
best = max(wins)

print('Part 2:', best)
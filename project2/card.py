import stdio
import stdrandom

# randomizes rank
rank = stdrandom.uniformInt(2, 15)

# sets rank to corresponding card number
if rank == 2:
    rankStr = '2'
elif rank == 3:
    rankStr = '3'
elif rank == 4:
    rankStr = '4'
elif rank == 5:
    rankStr = '5'
elif rank == 6:
    rankStr = '6'
elif rank == 7:
    rankStr = '7'
elif rank == 8:
    rankStr = '8'
elif rank == 9:
    rankStr = '9'
elif rank == 10:
    rankStr = '10'
elif rank == 11:
    rankStr = 'Jack'
elif rank == 12:
    rankStr = 'Queen'
elif rank == 13:
    rankStr = 'King'
elif rank == 14:
    rankStr = 'Ace'

# randomizes suit
suit = stdrandom.uniformInt(1, 5)

# sets suit to corresponding card number
if suit == 1:
    suitStr = 'Clubs'
elif suit == 2:
    suitStr = 'Diamonds'
elif suit == 3:
    suitStr = 'Hearts'
elif suit == 4:
    suitStr = 'Spades'

# outputs card
stdio.writeln(rankStr + ' of ' + suitStr)

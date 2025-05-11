# This is the logic for hand rankings.

import collections

card_values = { # Values for card strength
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

hand_names = { # Hand names
    10: "a royal flush",
    9: "a straight flush",
    8: "a four of a kind",
    7: "a full house",
    6: "a flush",
    5: "a straight",
    4: "a three of a kind",
    3: "two pairs",
    2: "one pair",
    1: "a high card"
}

def evaluate_hand(hand):
    nums = [card[:-1] for card in hand] # Splits the hand into its numbers
    suits = [card[-1] for card in hand] # Splits the hand into its suits
    values = sorted([card_values[i] for i in nums]) # Converts card faces to values using the above dictionary
    counts = collections.Counter(nums) # Counts how many of each number appear
    uniques = sorted(set(values)) # Sorts the order of the values

    straight = len(uniques) == 5 and (max(uniques) - min(uniques) == 4) # Can only be a straight with 5 consecutive values, eg. 4-5-6-7-8 (8 - 4 = 4, so it's a straight)
    if uniques == [2, 3, 4, 5, 14]:  # Allows Ace to be used as both 1 & 14
        straight = True
    flush = len(set(suits)) == 1 # Can only be a flush if there is 1 suit

    if straight and flush and values[0] == 14: # Can only be a royal flush if the first value is an Ace
        return (10, values)  # royal flush, hand value is 10
    elif straight and flush: 
        return (9, values)   # straight flush, hand value is 9
    elif 4 in counts.values():
        return (8, get_ranked_values(counts, 4, values))  # four of a kind, hand value is 8
    elif sorted(counts.values()) == [2, 3]:
        return (7, get_ranked_values(counts, 3, values))  # full house, hand value is 7
    elif flush:
        return (6, values)  # flush, hand value is 6
    elif straight:
        return (5, values)  # straight, hand value is 5
    elif 3 in counts.values():
        return (4, get_ranked_values(counts, 3, values))  # 3 of a kind, hand value is 4
    elif list(counts.values()).count(2) == 2:
        return (3, get_ranked_values(counts, 2, values))  # 2 pairs, hand value is 3
    elif 2 in counts.values():
        return (2, get_ranked_values(counts, 2, values))  # 1 pair, hand value is 2
    else:
        return (1, values)  # High Card, hand value is 1

def get_ranked_values(counter, primary_rank, all_values):
    primary = [card_values[n] for n, count in counter.items() if count == primary_rank]
    secondary = [card_values[n] for n, count in counter.items() if count != primary_rank]
    return sorted(primary, reverse=True) + sorted(secondary, reverse=True)

if __name__ == "__main__":
    evaluate_hand()
    get_ranked_values()
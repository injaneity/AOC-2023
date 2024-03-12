def score_hand(hand):
    # set(hand) converts the key (in this case hand) into an unordered set (removing duplicates)
    # for label in set hand loops through each value in the set
    # .count(label) counts the number of apperances of label in hand (the original list)
    # for every value in the set, its counted amount is added to the resulting list label_counts
    temp = hand.replace("J", "")
    print(temp)
    label_counts = [hand.count(label) for label in set(temp)]
    print(label_counts)
    j_counts = [hand.count('J')]
    j_value = int(j_counts[0])
    
    highest = 1
    # new part 2 cases
    for i in range(5, 1, -1):
        if i in label_counts:
            highest = i
            break
    
    if (j_value > 0):
        
        if highest + j_value == 5:
            print("five of a kind")
            return 6
        if highest + j_value == 4:
            print("four of a kind")
            return 5
        if (label_counts.count(3) == 1 and j_value == 1) or (label_counts.count(2) == 2 and j_value == 1):
            print("full house")
            return 4
        if highest + j_value == 3:
            print("three of a kind")
            return 3
        if highest + j_value == 2:
            print("one pair")
            return 1
        
        print("missed case")
    
    # 5 of a kind -> any number of values as long as remaining Js add up to 5
    # 4 of a kind -> 1 + 3, 2 + 2, 3 + 1
    # full house -> 3 + 1 + 1
    # 3 of a kind -> 2 + 1 + 1 + 1
    # two pair -> cannot exist since 3 of a kind takes precedence
    # one pair -> all unique
    # 0 pair -> cannot exist 
    
    if 5 in label_counts:
        # five of a kind
        print("five of a kind")
        return 6 
    
    if 4 in label_counts:
        # four of a kind
        print("four of a kind")
        return 5
    
    if 3 in label_counts:
        if 2 in label_counts:
            # full house
            print("full house")
            return 4
        # three of a kind
        print("three of a kind")
        return 3
    
    if label_counts.count(2) == 2:
        print("two pair")
        # two pair
        return 2
    
    if label_counts.count(2) == 1:
        # one pair
        print("one pair")
        return 1
    
    # high card
    print("high card")
    return 0

# transfer information directly into a dict
# str.split removes whitespaces by default
# map applies the function (str.split) to every item of an iterable (in this case a list)
# for __ in __ directly refers the values to the dictionary during declaration
hands_bids = {hand: int(bid) for hand, bid in map(str.split, open("day7.txt", 'r').readlines()) }

def sortkey(hand):    
    # .index(c) for c in hand returns index that char of hand appears in '234...'
    # effectively converts the characters into its relative weights for comparison
    # appends the score of the hand itself to the front of the list
    return [score_hand(hand)] + ['J23456789TQKA'.index(c) for c in hand]

# sorted(hands_bids, key=sortkey) applies sortkey to the key of hands_bids
# if you want to sort by items, use dict.items() (needs further research - am unsure)
# sorts the keys of the dictionary by the sortkey function -> [score, weight of #1, ...]
# enumerate with (list, start) -> start = 1
# enumerate gives 1: list[0], 2: list[1] etc
# i = 1, 2, ... (following the order) and h = value in dict
# for i, h in ... provides a list of hands_bids[h] * i --> apply sum function
print("1:", sum(hands_bids[h] * i for i, h in enumerate(sorted(hands_bids, key=sortkey), 1)))
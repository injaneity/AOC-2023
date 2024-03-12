infile = open("day7tc.txt", 'r')
list = infile.readlines()

hands = [0] * len(list)
bids = [0] * len(list)
types = {}

for i in range(0, len(list)):
    values = list[i].split(" ")
    hands[i] = values[0]
    bids[i] = values[1].replace("\n", "")
    
print(hands)
print(bids)

def in_list(char, dict):
    for key, value in dict.items():
        if (char == key):
            dict[key] += 1
            return True
    return False
            

def card_type(card):
    dict = {}
    for i in range(0, len(card)):
        
        if (not in_list(card[i], dict)):
            dict[card[i]] = 1
            
    print(dict)
            
    # case 1: five values
    if (len(dict) == 5):
        return 0
        
    # case 2: four values
    if (len(dict) == 4):
        return 1
        
    # case 3: three values --> 3 1 1 or 2 2 1
    if (len(dict) == 3):
        for keys, values in dict.items():
            if values == 3:
                return 3
        return 2
    
    # case 4: two values --> 3 2 or 4 1
    if (len(dict) == 2):
        for keys, value in dict.items():
            if values == 4:
                return 5
        return 4
    
    return 6
                    
# sort it
for i in range(0, len(list)):
    types[hands[i]] = card_type(hands[i])
    
sorted_dict = sorted(types.items(), key=lambda x:x[1])

types = dict(sorted_dict)

for keys in dict:
    
    

print(types)
    

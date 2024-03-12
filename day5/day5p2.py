infile = open("day5.txt", "r")
input = infile.read()

list = input.split("\n\n")

# seeds
temp = list[0].split(":")
seeds = temp[1].split("\n")
seeds = (seeds[0].strip()).split(" ")        
    
# all the conditions
map = [0] * 7
for i in range(1, 8):
    temp = list[i].split(":")
    data = temp[1].split("\n")
    map[i - 1] = data[1::]

lowest = pow(2, 50)
# from seed

def is_dupe(i):
    
    for j in range(0, i):
        
        # case 1: falls within the range {1, 2, 3, 4} vs {1, 2 ,3}
        if startend[0] >= int(seeds[(i-j) * 2]) and startend[1] <= int(seeds[(i - j) * 2 - 1]):
            return True
        
        # case 2: start outside the range but end inside {3, 4} vs {1, 2, 3, 4} --> {1, 2}
        if startend[1] <= int(seeds[(i - j) * 2 - 1]):
            startend[1] = int(seeds[(i - j) * 2 - 1]) - 1
            continue
            
        # case 3: start inside the range but end outside {1, 2} vs {1, 2, 3, 4} --> {3, 4}
        if startend[0] >= int(seeds[(i-j) * 2]):
            startend[0] = int(seeds[(i - j) * 2]) + 1
            continue
        
        # case 4: no change because all outside range
    return False


for i in range(0, int(len(seeds)/2)):
    
    startend = [int(seeds[i*2]), int(seeds[i*2]) + int(seeds[i*2 + 1]) + 1]
    
    count = 1
    
    # check with all previous seeds
    if (is_dupe(i)):
        continue
    
    for j in range(startend[0], startend[1]):
        
        idx = j
        
        for i in range(0, 7):
            
            for j in range(0, len(map[i])):
            
                # dest - source - range
                temp = map[i][j].split(" ")
                
                # check in range
                if (idx >= int(temp[1]) and idx < int(temp[1]) + int(temp[2])):
                    idx = int(temp[0]) + (idx - int(temp[1]))
                    break
                
        if (idx < lowest):
            lowest = idx
            
    
print(lowest)
        
infile.close()


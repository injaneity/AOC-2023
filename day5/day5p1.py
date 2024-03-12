infile = open("day5tc.txt", "r")
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

for seed in seeds:
    
    print(seed)
        
    idx = int(seed)
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


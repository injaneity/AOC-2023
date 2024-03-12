infile = open("day5.txt", "r")
input = infile.read()

list = input.split("\n\n")

# seeds
temp = list[0].split(":")
seeds = temp[1].split("\n")
seeds = (seeds[0].strip()).split(" ")

seedslist = [0] * int(len(seeds)/2)

for i in range(0, int(len(seeds)/2)):
    seedslist[i] == seeds[i * 2]

# all the conditions
map = [0] * 7
for i in range(1, 8):
    temp = list[i].split(":")
    data = temp[1].split("\n")
    map[i - 1] = data[1::]
    
# check for seed
def seed_check(idx):
    
    print(idx)
    
    for j in range(0, int(len(seeds)/2)):
        if (idx >= int(seeds[j * 2]) and idx <= int(seeds[j * 2]) + int(seeds[j * 2 + 1]) + 1):
            return True
    return False
    
location = 84206669
while(location < 80000000 * 2):
    
    idx = location
    print(location)
    
    count = 0
    for i in range(6, -1, -1):
                
        for j in range(0, len(map[i])):
        
            # dest - source - range
            temp = map[i][j].split(" ")
            
            # check if location in dest
            if (idx >= int(temp[0]) and idx < int(temp[0]) + int(temp[2])):
                
                # if in dest -> 51, 52, 53, 54 (range 4)
                # 53 -> 4 == 53 - 51 + 2
                # in source -> 2, 3, 4, 5
                idx = idx - int(temp[0]) + int(temp[1])
                break
                
                
    # compare idx against seeds
    if (seed_check(idx)):
        print("FOUND IDX")
        print(idx)
        print(location)
        break
    
    location += 1

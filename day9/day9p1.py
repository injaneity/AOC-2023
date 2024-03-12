lines = [items.replace("\n", "").split(" ") for items in open("day9tc.txt", 'r').readlines()]

def is_all_zeroes(list):
    print(list)
    for item in list:
        if int(item) != 0:
            return False
    return True

# create list of differences

sum = 0
for i in range(0, len(lines)):
    
    current_list = lines[i]
    diff_list = []

    latest = -1
    while(latest == -1 or not is_all_zeroes(diff_list[latest])):
        
        sub_list = []
        for j in range(0, len(current_list) - 1):
            sub_list.append(int(current_list[j + 1]) - int(current_list[j]))
                    
        diff_list.append(sub_list)
        latest += 1
        current_list = diff_list[latest]
            
    value = int(lines[i][len(lines[i]) - 1])
    for j in range(len(diff_list) - 2, -1, -1):
        value += int(diff_list[j][len(diff_list[j]) - 1])
        
    sum += value
    
print(sum)



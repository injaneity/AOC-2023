lines = [items.replace("\n", "").split(" ") for items in open("day9.txt", 'r').readlines()]

def is_all_zeroes(list):
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
        # add differences to temp list
        for j in range(0, len(current_list) - 1):
            sub_list.append(int(current_list[j + 1]) - int(current_list[j]))
        
        # add temp to overall list of temp
        diff_list.append(sub_list)
        latest += 1
        current_list = diff_list[latest]
    
    # take first value
    first_value = int(lines[i][0])
    # add differences back to last value
    to_change = 0
    for j in range(len(diff_list) - 2, -1, -1):
        to_change += int(diff_list[j][0]) * int(pow(-1, j - 1))
        
    sum += first_value + to_change

    
print(sum)



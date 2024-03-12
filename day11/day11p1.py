list = [i for i in open("day11tc.txt", 'r').read().split("\n")]

for i in list:
    print(i)

def is_all_space(row, col, is_row):
    
    if (is_row):
        for i in list[row]:
            if i != '.':
                return False
            
    else:
        for i in range(len(list)):
            if list[i][col] != '.':
                return False
            
    return True

copy = []

# check every row
for i in range(0, len(list)):
    if (is_all_space(i, 0, True)):
        copy.append(list[i])
    copy.append(list[i])
    
# check every column
for i in range(0, len(list[0])):
    if (is_all_space(0, i, False)):
        for j in range(0, len(list)):
            copy[j].append(list[j][i])
            
    for j in range(0, len(list)):
        copy.append(list[j][i])
        
        
        
for i in copy:
    print(i)

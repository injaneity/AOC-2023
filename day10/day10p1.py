input = [i.replace("\n", "") for i in open("day10tc1.txt", 'r').readlines()]

arr = []
xyz = [0, 0, 1]
for i in range(0, len(input)):
    sub_arr = []
    for j in range(0, len(input[i])):
        if (input[i][j] == 'S'):
            start_x = i
            start_y = j
        sub_arr.append(input[i][j])
    
    arr.append(sub_arr)

xyz[0] = start_x
xyz[1] = start_y
arr[start_x][start_y] = 0

def check_left(xyz):
    left_char = ['-','L','F']
    if (xyz[1] != 0 and arr[xyz[0]][xyz[1] - 1] in left_char):
        return True
    return False
    
def check_right(xyz):
    right_char = ['-','7','J']
    if (xyz[1] != len(arr[0]) - 1 and arr[xyz[0]][xyz[1] + 1] in right_char):
        return True
    return False

def check_up(xyz):
    up_char = ['7','F','|']
    if (xyz[0] != 0 and arr[xyz[0] - 1][xyz[1]] in up_char):
        return True
    return False
    
def check_down(xyz):
    down_char = ['L','J','|']
    if (xyz[0] != len(arr[0]) - 1 and arr[xyz[0] + 1][xyz[1]] in down_char):
        return True
    return False
    
def check_direction(xyz):
    # case 1: S (check all)
    # case 2: move up -> L, J, |
    # case 3: move left -> J, 7, -
    # case 4: move right -> L, F, -
    # case 5: move down -> F, 7, |
                     
    
    if(check_up(xyz)):
        xyz[0] -= 1
        arr[xyz[0]][xyz[1]] = xyz[2]
        xyz[2] += 1
        return True
    
    if(check_down(xyz)):
        arr[xyz[0] + 1][xyz[1]] = arr[xyz[0]][xyz[1]] + 1
        xyz[0] += 1
        return True
    
    if(check_left(xyz)):
        value = arr[xyz[0]][xyz[1]]
        if (value != 0 and arr[xyz[0]][xyz[1] - 1] > value):
            return False
        arr[xyz[0]][xyz[1] - 1] = arr[xyz[0]][xyz[1]] + 1
        xyz[1] -= 1
        return True
    
    if(check_right(xyz)):
        arr[xyz[0]][xyz[1] + 1] = arr[xyz[0]][xyz[1]] + 1
        xyz[1] += 1
        return True
    
    return False



for i in range(0, 30):
    if (not check_direction(xyz)):
        if (xyz[0] == start_x and xyz[1] == start_y):
            break
        xyz[0] = start_x
        xyz[1] = start_y
        xyz[2] = 1

for i in arr:
    print(i)

        
        

        
infile = open("day8tc.txt", 'r').readlines()
input = [i for i in infile[0].replace("\n","")]


for i in range(0, 10):
    for j in range(0, len(input)):
        input.append(input[j])


    
print(input)


dict = {}
for i in range(2, len(infile)):
    if (len(infile[i]) > 1):
        temp = infile[i].split('=')
        dict[temp[0].strip()] = (temp[1].strip()).replace("(", "") .replace(")", "")
        
print(dict)

# key = value1 and value2
# key != value or key != value2

start = "AAA"
count = 0
for direction in input:
    
    print(direction)
    
    if direction == 'L':
        temp = dict[start].split(",")
        start = temp[0].strip()
        
    if direction == 'R':
        temp = dict[start].split(",")
        start = temp[1].strip()
        
    print(start)
    count += 1
    
    if (start == 'ZZZ'):
        break
    
print(start)
print(count)
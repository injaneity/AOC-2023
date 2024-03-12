infile = open("day8tc.txt", 'r').readlines()
input = [i for i in infile[0].replace("\n","")]

for i in range(0, 10):
    for j in range(0, len(input)):
        input.append(input[j])

dict = {}
for i in range(2, len(infile)):
    if (len(infile[i]) > 1):
        temp = infile[i].split('=')
        dict[temp[0].strip()] = (temp[1].strip()).replace("(", "") .replace(")", "")

nodes = []
for key in dict:
    if 'A' in key:
        nodes.append(key)
        
list = []

for i in range(0, len(nodes)):
    
    count = 0
    for direction in input:
        if direction == 'L':
            temp = dict[nodes[i]].split(",")
            nodes[i] = temp[0].strip()
            
        if direction == 'R':
            temp = dict[nodes[i]].split(",")
            nodes[i] = temp[1].strip()
            
        count += 1
            
        if 'Z' in nodes[i]:
            list.append(count)
            break
        
from math import gcd
lcm = 1
for i in list:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)
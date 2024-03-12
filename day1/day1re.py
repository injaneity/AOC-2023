input = [i.replace("\n", "") for i in open("day1tc.txt", 'r').readlines()]
print(input)

sum = 0

for line in input:
    
    part = 0
    
    for i in line:
        if i.isdigit():
            part += int(i)
            break
            
    for i in line[::-1]:
        if i.isdigit():
            part = part * 10 + int(i)
            break
            
    sum += part
    
print(sum)
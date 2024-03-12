infile = open("day6.txt", 'r')
list = infile.readlines()

time = ((list[0]).strip()).split(":")
rec = ((list[1]).strip()).split(":")

# clean up time
time = time[1::]
time = time[0].split(" ")
count = 0
for i in time:
    if (len(i) > 0):
        time[count] = i
        count += 1
        
time = time[:count:]
    

print(time)

# clean up distance
rec = rec[1::]
rec = rec[0].split(" ")
count = 0
for i in rec:
    if (len(i) > 0):
        rec[count] = i
        count += 1
        
rec = rec[:count:]

print(rec)

sum = 0

for i in range(0, len(time)):
    
    part = 0
    for j in range(1, int(time[i])):
        speed = j * 1
        distance = (int(time[i]) - j) * speed
        
        if distance > int(rec[i]):
            part += 1
            
            
    print(part)
    
    if sum == 0:
        sum = part
    elif (part != 0):
        sum *= part
        
print(sum)
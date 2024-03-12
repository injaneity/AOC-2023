infile = open("day6.txt", 'r')
list = infile.readlines()

time = ((list[0]).strip()).split(":")
rec = ((list[1]).strip()).split(":")

# clean up time        
time = int(time[1].replace(" ", ""))

# clean up distance
rec = int(rec[1].replace(" ", ""))

sum = 0
    
for j in range(1, time):
    speed = j * 1
    distance = (time - j) * speed
    
    if distance > rec:
        sum += 1
        
        
print(sum)

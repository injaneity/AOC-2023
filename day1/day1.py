input = """
jzhfcmvb8fiveqgq18fivevlpgdnkbq
"""

list = input.splitlines()


nums = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
        }

bw_nums = {
    'eno': '1',
    'owt': '2',
    'eerht': '3',
    'ruof': '4',
    'evif': '5',
    'xis': '6',
    'neves': '7',
    'thgie': '8',
    'enin': '9'
        }

    
def check_substr(substr, nums):
    for key in nums:
        if (substr.find(key) == 0):
            return ord(nums[key]) - ord('0')
        
    return 0

## assumes that every thing is a digit
sum = 0

for i in list:
    
    part = 0
    
    fw_count = 0
    
    for j in i:
        
        if (j.isdigit()):
            part += ord(j) - ord('0')
            break
        
        substr = (str(i[fw_count::]))
        if (check_substr(substr, nums) != 0):
            part += check_substr(substr, nums)
            break 
        
        fw_count += 1
    
    bw_count = 0
    
    
    for k in i[::-1]:
        
        if (k.isdigit()):
            part *= 10
            part += ord(k) - ord('0')
            break
        
        substr = (str(i[len(i) - bw_count::-1]))
        if (check_substr(substr, bw_nums) != 0):
            part *= 10
            part += check_substr(substr, bw_nums)
            break
        
        bw_count += 1
        
    sum += part
            
print("sum is " + str(sum))
        
def two_sum(nums, target):
   
    seen = {}
    
    for current_index, num in enumerate(nums):
        complement = target - num
 
        if complement in seen:
            return [seen[complement], current_index]
        
        seen[num] = current_index
        
    return []


print(two_sum([2,3,4,6],10))


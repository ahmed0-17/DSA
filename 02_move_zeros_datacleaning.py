def move_zeroes(nums: list[int]) -> None:
    
    write_index = 0
     
    for read_index in range(len(nums)):
    
        if nums[read_index] != 0:
    
            nums[write_index] = nums[read_index]
            write_index += 1

    while write_index < len(nums):
        nums[write_index] = 0
        write_index += 1
    return nums

# print(move_zeroes([1,0,5,6,0,5,4]))

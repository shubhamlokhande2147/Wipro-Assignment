def sequence_123(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

# Test the function
print(sequence_123([1, 1, 2, 3, 1]))  # Output: True
print(sequence_123([1, 1, 2, 4, 3]))  # Output: False

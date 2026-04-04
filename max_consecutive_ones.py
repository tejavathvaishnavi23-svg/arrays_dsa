#Max consecutive ones
#Given a list of 0s and 1s, find the maximum number of consecutive 1s.

def max_consecutive_ones(nums):
    count = 0
    max_count = 0

    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count

nums = [1, 1, 0, 1, 1, 1]
print("Max consecutive ones:", max_consecutive_ones(nums))

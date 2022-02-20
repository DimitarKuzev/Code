def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            max_num += num        # '56057'
            # max_num = num       # '56043'
            # max_num += 1      # '50422'
            # num = max_num     # '50412' # (Fill in the missing line here)
    return max_num
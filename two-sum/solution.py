def two_sum(nums, target):
    seen = set()
    for num in nums:
        if target - num in seen: return True
        seen.add(num)
    return False

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        print(length)
        num_set = set(nums)
        set_length = len(num_set)
        if set_length < length:
            return True
        else:
            return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       num_set = set(nums)
       num_set_length = len(num_set)
       if len(nums) > num_set_length:
            return True
       return False
   


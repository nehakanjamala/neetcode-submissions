class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # number : index 0:1 1:2

        for i,num in enumerate(nums): #0:1, 1:2 7
            needed = target - num #9-7=2
            if needed in seen:
                return[seen[needed], i] 
            else:
                seen[num] = i #seen[2]
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    result = nums[i]+nums[j]
                    if result == target:
                        l1 = list()
                        l1= [i,j]
                        return l1
                        break
        
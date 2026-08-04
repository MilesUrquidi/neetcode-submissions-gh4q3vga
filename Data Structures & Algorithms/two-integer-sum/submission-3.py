class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = {}

        for i,j in enumerate(nums):
            diff = target - j
            if diff in answer:
                return [answer[diff], i]
            else:
                answer[j] = i
                

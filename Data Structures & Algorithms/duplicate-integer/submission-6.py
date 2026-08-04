class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracking = set()

        for num in nums:
            if num in tracking:
                return True
            else:
                tracking.add(num)
        return False
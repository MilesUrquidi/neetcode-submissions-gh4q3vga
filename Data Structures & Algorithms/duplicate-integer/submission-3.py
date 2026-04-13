class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeats = set()
        for n in nums:
            if n not in repeats:
                repeats.add(n)
            else:
                return True
        return False
        
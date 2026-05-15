class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        testSet = set()

        for i in nums:
            if i in testSet:
                return True
            else:
                testSet.add(i)
        return False
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #map charcount to list of anagrams

        for w in strs:
            count = [0] * 26

            for c in w:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(w)

        return list(res.values())
class Solution:
    # O(m*nlogn)
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            sortedStr = ''.join(sorted(s))
            if sortedStr in hashMap:
                hashMap[sortedStr].append(s)
            else:
                hashMap[sortedStr] = [s]
        
        return list(hashMap.values())

    # Optimal solution: O(m*n*26) = O(m*n)
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char)-ord("a")] += 1
            
            res[tuple(count)].append(s)
        
        return res.values()

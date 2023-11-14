class Soltuion:
    # Hash map O(n)
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        
        for char in t:
            if char not in s_dict or s_dict[char] == 0:
                return False
            else:
                s_dict[char] -= 1
        
        return True

    # Sorting O(nlogn)
    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
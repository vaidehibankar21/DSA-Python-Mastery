"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        return sorted(s) == sorted(t)
"""

## Time: O(n log n) — sorting both strings.
## Space: O(n) — sorted lists require additional space.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False
        return True

# Time: \(O(n)\) average — each string is traversed once.

# Space: O(k) where k is the number of distinct characters. In the general case, this is O(n)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)

        return list(groups.values())

"""

## Time: O(nklog k) — sort each of the n words, each of length at most k.

## Space: O(nk) — store the dictionary keys and grouped words.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1
            
            groups[tuple(count)].append(word)
        
        return list(groups.values())

# Time: O(nk) — count each character once.

# Space: O(nk) overall to store the groups and keys, with 26 counters per word temporarily.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)
        return False

## Time O(n) average, space O(n)

# Whenever a question asks whether an array contains duplicates, think of a set first.
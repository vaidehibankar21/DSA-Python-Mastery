class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                count = 1

                while current + 1 in num_set:
                    current += 1
                    count += 1
                
                longest = max(longest, count)
        
        return longest

## start counting only if the previous number is missing

## Optimized using set	Time: O(n)average, space: O(n)
## Solution is O(n) average time because each number is inserted into the set once, and sequences are counted only from their starting numbers.
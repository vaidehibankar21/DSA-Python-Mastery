"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n):
            product = 1
            
            for j in range(n):
                if i != j:
                    product *= nums[j]

            result.append(product)

        return result
"""


from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result

# Time complexity: O(n). We traverse the array twice.
# Auxiliary space: O(1), excluding the output array. We use only prefix and suffix variables besides the output.
# Output space: O(n) for result.
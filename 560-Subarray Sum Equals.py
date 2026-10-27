"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            total = 0

            for j in range(i, n):
                total += nums[j]

                if total == k:
                    count += 1

        return count

"""

# Time: O(n^2), because we examine every possible subarray.

# Auxiliary space: O(1)


from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num

            needed = current_sum - k
            count += prefix_count.get(needed, 0)

            prefix_count[current_sum] = (
                prefix_count.get(current_sum, 0) + 1
            )

        return count

"""The key idea is to avoid checking every subarray separately.

Suppose the prefix sum up to the current position is current_sum.

If an earlier prefix sum was current_sum - k, then the elements between that earlier position and the current position sum to k.

Mathematically:
\[
\text{subarray sum} = \text{current sum} - \text{previous sum}
\]

We want:
\[
k = \text{current sum} - \text{previous sum}
\]

Rearrange:
\[
\text{previous sum} = \text{current sum} - k
\]

So, for every element, we check whether current_sum - k exists in our hash map."""

# Time: O(n)

# Auxiliary space: O(n)
# The optimized solution traverses the array once. Hash map lookups and updates take (O(1) average time.
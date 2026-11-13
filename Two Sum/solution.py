from typing import List

class Solution:
    """
    LeetCode 1: Two Sum
    https://leetcode.com/problems/two-sum/
    
    Approach: One-Pass Hash Map
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map storing { number: index }
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement has already been processed
            if complement in seen:
                return [seen[complement], i]
            
            # Store current number with its index for future lookups
            seen[num] = i
            
        return []


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard case
    assert solver.twoSum([2, 7, 11, 15], 9) == [0, 1]
    
    # Test Case 2: Out of order
    assert solver.twoSum([3, 2, 4], 6) == [1, 2]
    
    # Test Case 3: Duplicate elements
    assert solver.twoSum([3, 3], 6) == [0, 1]
    
    # Test Case 4: Negative numbers
    assert solver.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]
    
    print("All test cases passed successfully!")

class Solution:
    """
    LeetCode 20: Valid Parentheses
    https://leetcode.com/problems/valid-parentheses/
    
    Approach: LIFO Stack with Hash Map
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    """
    def isValid(self, s: str) -> bool:
        # Fast exit for odd length strings
        if len(s) % 2 != 0:
            return False
            
        # Map closing brackets to their corresponding opening brackets
        matching = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        stack = []
        
        for char in s:
            if char in matching:
                # Character is a closing bracket:
                # 1. Stack must not be empty.
                # 2. Top of stack must match the required opening bracket.
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()
            else:
                # Character is an opening bracket: push onto stack
                stack.append(char)
                
        # String is valid only if all opened brackets were successfully matched
        return len(stack) == 0


if __name__ == "__main__":
    solver = Solution()
    
    # Test cases
    assert solver.isValid("()") == True
    assert solver.isValid("()[]{}") == True
    assert solver.isValid("(]") == False
    assert solver.isValid("([)]") == False
    assert solver.isValid("{[]}") == True
    assert solver.isValid("]") == False        # Premature closer / stack underflow
    assert solver.isValid("((") == False       # Unclosed brackets at end
    assert solver.isValid("(([]){})") == True  # Deeply nested valid
    
    print("All test cases passed successfully!")

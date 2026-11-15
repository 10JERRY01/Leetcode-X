from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution:
    """
    LeetCode 21: Merge Two Sorted Lists
    https://leetcode.com/problems/merge-two-sorted-lists/

    Approach: Iterative Two-Pointer with Dummy Sentinel Node
    - Time Complexity: O(n + m)
    - Space Complexity: O(1) auxiliary space
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy sentinel node simplifies head handling
        dummy = ListNode(-1)
        current = dummy

        # Traverse both lists while nodes remain in both
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Splice the remainder of the non-empty list in O(1)
        current.next = list1 if list1 is not None else list2

        return dummy.next


# --- Helper methods for local testing ---
def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


if __name__ == "__main__":
    solver = Solution()

    # Test Case 1: Standard interleaved lists
    l1 = build_linked_list([1, 2, 4])
    l2 = build_linked_list([1, 3, 4])
    merged = solver.mergeTwoLists(l1, l2)
    assert linked_list_to_list(merged) == [1, 1, 2, 3, 4, 4]

    # Test Case 2: Both empty lists
    l1 = build_linked_list([])
    l2 = build_linked_list([])
    merged = solver.mergeTwoLists(l1, l2)
    assert linked_list_to_list(merged) == []

    # Test Case 3: One empty list
    l1 = build_linked_list([])
    l2 = build_linked_list([0])
    merged = solver.mergeTwoLists(l1, l2)
    assert linked_list_to_list(merged) == [0]

    # Test Case 4: Asymmetric lengths
    l1 = build_linked_list([5])
    l2 = build_linked_list([1, 2, 3])
    merged = solver.mergeTwoLists(l1, l2)
    assert linked_list_to_list(merged) == [1, 2, 3, 5]

    print("All test cases passed successfully!")

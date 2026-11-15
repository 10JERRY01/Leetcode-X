# LeetCode 21: Merge Two Sorted Lists

[LeetCode Problem Link](https://leetcode.com/problems/merge-two-sorted-lists/)

## Problem Description
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** linked list by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

### Examples
- **Example 1:**
  - Input: `list1 = [1,2,4], list2 = [1,3,4]`
  - Output: `[1,1,2,3,4,4]`

- **Example 2:**
  - Input: `list1 = [], list2 = []`
  - Output: `[]`

- **Example 3:**
  - Input: `list1 = [], list2 = [0]`
  - Output: `[0]`

---

## 4 Progressive Hints
1. **Two Pointers Comparison:** Compare `list1.val` and `list2.val`. Pick the smaller node, attach it to your merged list, and advance that list's pointer.
2. **The "Dummy Head" Sentinel:** Use a sentinel node `dummy = ListNode(-1)` and a `current` pointer to eliminate special-case checks for the head of the new list. Return `dummy.next` at the end.
3. **$O(1)$ Remainder Splice:** When one list is exhausted, you do not need to iterate through the rest of the other list. Simply attach the remaining sublist in one step: `current.next = list1 or list2`.
4. **In-Place Rewiring:** Do not create new `ListNode` instances; rewire existing pointers in-place for $O(1)$ auxiliary space.

---

## Interactive Animated Visual Explainer
Open `explainer.html` in any web browser to see the step-by-step visual animation with head comparison, pointer tracking, dummy node anchoring, and $O(1)$ tail splicing.

---

## Complexity
- **Time Complexity:** $O(n + m)$ — Where $n$ and $m$ are the lengths of `list1` and `list2`. Each node is inspected once.
- **Space Complexity:** $O(1)$ — In-place pointer rewiring; no additional nodes allocated.

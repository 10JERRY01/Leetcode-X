# LeetCode 1: Two Sum

[LeetCode Problem Link](https://leetcode.com/problems/two-sum/)

## Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice. You can return the answer in any order.

### Examples
- **Example 1:**
  - Input: `nums = [2,7,11,15], target = 9`
  - Output: `[0,1]`
  - Explanation: Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

- **Example 2:**
  - Input: `nums = [3,2,4], target = 6`
  - Output: `[1,2]`

- **Example 3:**
  - Input: `nums = [3,3], target = 6`
  - Output: `[0,1]`

---

## 4 Progressive Hints
1. **The Target Equation:** For any element $x = \text{nums}[i]$, what exact number $y$ must exist in the array so that $x + y = \text{target}$? The needed number is $\text{target} - x$, called the **complement**.
2. **Eliminate the $O(n^2)$ Bottleneck:** Instead of checking every pair with nested loops, ask: *What data structure allows you to look up whether an element has been seen before in $O(1)$ average time?*
3. **Key vs. Value in Hash Map:** The problem asks for the **indices**, not just the numbers. Map each `number -> its index`.
4. **One-Pass & Edge Cases:** If you search the hash map for the complement **before** storing the current number, you can do it in a single pass. This naturally handles duplicates like `[3, 3]` with `target = 6` and prevents self-pairing.

---

## Interactive Animated Visual Explainer
Open `explainer.html` in any web browser to see the step-by-step visual animation with playback controls, array pointer tracking, and hash map updates.

---

## Complexity
- **Time Complexity:** $O(n)$ — Single pass through the list with $O(1)$ average dictionary lookup.
- **Space Complexity:** $O(n)$ — Stores up to $n$ elements in the dictionary.

# LeetCode 20: Valid Parentheses

[LeetCode Problem Link](https://leetcode.com/problems/valid-parentheses/)

## Problem Description
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the **same type** of brackets.
2. Open brackets must be closed in the **correct order**.
3. Every close bracket has a corresponding open bracket of the same type.

### Examples
- **Example 1:**
  - Input: `s = "()"`
  - Output: `true`

- **Example 2:**
  - Input: `s = "()[]{}"`
  - Output: `true`

- **Example 3:**
  - Input: `s = "(]"`
  - Output: `false`

- **Example 4:**
  - Input: `s = "([)]"`
  - Output: `false`

- **Example 5:**
  - Input: `s = "{[]}"`
  - Output: `true`

---

## 4 Progressive Hints
1. **Order Matters (LIFO):** For nested brackets like `"({[]})"`, the most recently opened bracket must be the first one closed. A Last-In, First-Out (LIFO) **Stack** is the natural choice.
2. **Why Counters Fail:** Simple counters track quantities but miss nesting order entirely (e.g., `"([)]"` has matching counts but is invalid).
3. **Map Closers to Openers:** Push opening brackets (`(`, `{`, `[`). For closing brackets, check if `stack[-1]` matches the required opening pair using a dictionary `{')': '(', '}': '{', ']': '['}`.
4. **Edge Cases:** Handle premature closers on an empty stack (`s = "]"`) and unclosed brackets remaining at the end (`s = "(("`). The string is only valid if `len(stack) == 0`.

---

## Interactive Animated Visual Explainer
Open `explainer.html` in any web browser to see the step-by-step stack simulation with push, pop, mismatch detection, and playback controls.

---

## Complexity
- **Time Complexity:** $O(n)$ — Single pass through string of length $n$. Each push and pop takes $O(1)$ time.
- **Space Complexity:** $O(n)$ — In the worst-case (all openers), the stack holds up to $n$ characters.

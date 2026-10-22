# dsa-patterns-java

![Java](https://img.shields.io/badge/Java-17-orange) ![Problems](https://img.shields.io/badge/roadmap-892%20problems-blue) ![Approach](https://img.shields.io/badge/organised%20by-pattern-green)

Data structures and algorithms in **Java**, solved **pattern by pattern** (two pointers, sliding window, prefix sum, Kadane, binary search on answer, monotonic stack, recursion and backtracking, trees, DP, graphs).
Every solution starts with the approach, the time and space complexity, and the mistake I made on the first try.

The roadmap merges **Striver's A2Z sheet** (392 problems), **Love Babbar's 450** (181 problems) and pattern lists from LeetCode, without repeats: **892 problems** in total.

## Progress

<!-- PROGRESS:START -->
**2 problems solved** · Basic 2 · Core 0 · Pro 0 · 0 redone · 🔥 1-day streak · 1 active days

| Track | Done | Total | Progress |
|---|---:|---:|---|
| Plan 1 (core, Oct–Jan) | 2 | 400 | `░░░░░░░░░░░░░░░░░░░░` |
| Plan 2 (advanced) | 0 | 492 | `░░░░░░░░░░░░░░░░░░░░` |
| Striver A2Z questions | 1 | 392 | `░░░░░░░░░░░░░░░░░░░░` |
| Love Babbar 450 questions | 1 | 181 | `░░░░░░░░░░░░░░░░░░░░` |
| ★ Interview favourites | 0 | 31 | `░░░░░░░░░░░░░░░░░░░░` |

<details><summary>Week by week</summary>

| Folder | Topic | Done |
|---|---|---:|
| [`W01-java-logic-building`](W01-java-logic-building/) | Java + Logic building | 1 / 63 |
| [`W02-arrays-strings-matrix-first-contact`](W02-arrays-strings-matrix-first-contact/) | Arrays, Strings, Matrix — first contact | 1 / 51 |
| [`W03-sorting-array-faqs-two-pointers`](W03-sorting-array-faqs-two-pointers/) | Sorting + Array FAQs + Two Pointers | 0 / 29 |
| [`W04-kadane-prefix-sum-hashing`](W04-kadane-prefix-sum-hashing/) | Kadane + Prefix Sum + Hashing | 0 / 28 |
| [`W05-sliding-window-strings-i`](W05-sliding-window-strings-i/) | Sliding Window + Strings I | 0 / 25 |
| [`W06-strings-ii-intervals-matrix`](W06-strings-ii-intervals-matrix/) | Strings II + Intervals + Matrix | 0 / 22 |
| [`W07-binary-search`](W07-binary-search/) | Binary Search | 0 / 26 |
| [`W08-recursion-backtracking-sorting-bits`](W08-recursion-backtracking-sorting-bits/) | Recursion + Backtracking + Sorting + Bits | 0 / 29 |
| [`W09-linked-list`](W09-linked-list/) | Linked List | 0 / 36 |
| [`W10-stack-queue`](W10-stack-queue/) | Stack & Queue | 0 / 32 |
| [`W11-trees-bst`](W11-trees-bst/) | Trees + BST | 0 / 32 |
| [`W12-heap-greedy-dp-graph-basics`](W12-heap-greedy-dp-graph-basics/) | Heap + Greedy + DP + Graph basics | 0 / 27 |
| [`plan2/`](plan2/) | Advanced topics (after Plan 1) | 0 / 492 |

</details>

<sub>Updated 23 Oct 2026 by `scripts/progress.py`</sub>
<!-- PROGRESS:END -->

## How it is organised

The core plan runs 12 weeks, one topic family per week, ordered the way placement rounds test them. Each folder has its own README listing that week's problems with links and a ✅ for the ones solved.

| Folder | Topic |
|---|---|
| `W01-java-logic-building` | Java + Logic building |
| `W02-arrays-strings-matrix-first-contact` | Arrays, Strings, Matrix — first contact |
| `W03-sorting-array-faqs-two-pointers` | Sorting + Array FAQs + Two Pointers |
| `W04-kadane-prefix-sum-hashing` | Kadane + Prefix Sum + Hashing |
| `W05-sliding-window-strings-i` | Sliding Window + Strings I |
| `W06-strings-ii-intervals-matrix` | Strings II + Intervals + Matrix |
| `W07-binary-search` | Binary Search |
| `W08-recursion-backtracking-sorting-bits` | Recursion + Backtracking + Sorting + Bits |
| `W09-linked-list` | Linked List |
| `W10-stack-queue` | Stack & Queue |
| `W11-trees-bst` | Trees + BST |
| `W12-heap-greedy-dp-graph-basics` | Heap + Greedy + DP + Graph basics |
| `plan2/` | Advanced: DP, graphs (DSU, MST, SCC), tries, string algorithms |
| `revision/` | ★ problems rewritten from scratch one week later |
| `notes/` | Weekly pattern notes |
| `ERROR_LOG.md` | Every mistake, and the fix |

## Solution format

```java
/*
 * Problem : Two Sum  ★
 * Plan ID : A324 | P1 · W2 · Day 12 · 26 Oct
 * Source  : Striver
 * Link    : https://leetcode.com/problems/two-sum/
 * Level   : Basic
 * Status  : Solved
 *
 * Approach:
 *   Brute force checks every pair: O(n^2).
 *   Store value -> index in a HashMap; for each element look up target - nums[i].
 *
 * Time : O(n)    Space : O(n)
 * Mistake: put the element in the map before checking, so it matched itself.
 */
```

## Workflow

1. Learn the pattern, then try every problem alone first.
2. Commit each solution on its own: `git commit -m "A324 Two Sum - HashMap O(n)"`.
3. Log mistakes in `ERROR_LOG.md`.
4. Run `python scripts/progress.py` to update this README and the week folders.
5. Sunday: redo the week's mistakes, rewrite ★ problems in `revision/`, write `notes/week-XX.md`.

## Sources

Striver A2Z DSA Sheet (takeUforward) · Love Babbar DSA 450 · LeetCode · GeeksforGeeks

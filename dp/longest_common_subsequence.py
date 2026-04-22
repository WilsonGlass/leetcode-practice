"""
Given two strings text1 and text2, return the length of their longest
common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some
characters (can be none) deleted without changing the relative order of the remaining characters.

For example "ace" is a subsequence fo "abcde"

A common subsequence of two strings is a subsequence that is common to both strings

text1 = "abcde"
text2 = "ace"

      ""  a  c  e
  ""   0  0  0  0
  a    0  ?

text1[0]='a' vs text2[0]='a' — they match! So look diagonal dp[0][0] + 1 = 1
      ""  a  c  e
  ""   0  0  0  0
  a    0  1  ?

text1[0]='a' vs text2[1]='c' — no match. Take max of left dp[1][1]=1 or above dp[0][2]=0 → 1
      ""  a  c  e
  ""   0  0  0  0
  a    0  1  1  ?

text1[0]='a' vs text2[2]='e' — no match. Max of left 1 or above 0 → 1
      ""  a  c  e
  ""   0  0  0  0
  a    0  1  1  1
  b    0  ?

text1[1]='b' vs text2[0]='a' — no match. Max of left 0 or above 1 → 1
      ""  a  c  e
  ""   0  0  0  0
  a    0  1  1  1
  b    0  1  ?

text1[1]='b' vs text2[1]='c' — no match. Max of left 1 or above 1 → 1
      ""  a  c  e
  ""   0  0  0  0
  a    0  1  1  1
  b    0  1  1  ?

text1[1]='b' vs text2[2]='e' — no match. Max of left 1 or above 1 → 1
      ""  a  c  e
  ""   0  0  0  0
  a    0  1  1  1
  b    0  1  1  1
  c    0  ?

text1[2]='c' vs text2[0]='a' — no match. Max of left 0 or above 1 → 1
      ""  a  c  e
  ""   0  0  0  0
  a    0  1  1  1
  b    0  1  1  1
  c    0  1  ?

text1[2]='c' vs text2[1]='c' — match! Diagonal dp[2][1] + 1 = 1 + 1 = 2
      ""  a  c  e
  ""   0  0  0  0
  a    0  1  1  1
  b    0  1  1  1
  c    0  1  2  ?

text1[2]='c' vs text2[2]='e' — no match. Max of left 2 or above 1 → 2
      ""  a  c  e
  ""   0  0  0  0
  a    0  1  1  1
  b    0  1  1  1
  c    0  1  2  2
  d    0  1  2  2   ← 'd' matches nothing in "ace", so nothing grows
  e    0  1  2  ?

text1[4]='e' vs text2[2]='e' — match! Diagonal dp[4][2] + 1 = 2 + 1 = 3
      ""  a  c  e
  ""   0  0  0  0
  a    0  1  1  1
  b    0  1  1  1
  c    0  1  2  2
  d    0  1  2  2
  e    0  1  2  3  ← answer
"""

def longest_common_subsequence(text1: str, text2: str) -> int:
    # Matrix of size (len(text1)+1) * (len(text2)+1), filled with 0s
    # Extra row/col of zeros acts as our base case (emptry strings has LCS of 0)
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i-1] == text2[j-1]:
                # Characters match - extend the diagonal (previous best without these chars)
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # No match - best we can do is skip one char from either string
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Bottom-right corner has the answer for the full strings
    return dp[len(text1)][len(text2)]

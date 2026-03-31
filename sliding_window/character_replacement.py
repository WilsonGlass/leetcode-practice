"""
You are given a string s and an integer k. You can choose
any character of the string and change it to any other
uppercase English character. You can perform this operation
at most k times

Return the length of the longest substring containing the same
letters you can get after performing the above operations
"""
from collections import defaultdict, Counter


# my solution
def character_replacement(s: str, k: int) -> int:
    left = 0
    right = 0
    longest = 0
    while right < len(s):
        character_counts = Counter(s[left:right+1])
        most_common_char = max(character_counts, key=character_counts.get)
        rest_counts = [freq for char, freq in character_counts.items() if char != most_common_char]
        if sum(rest_counts) <= k:
            longest = max(longest, right - left + 1)
            right += 1
            continue
        else:
            left += 1
    return longest

# need to study optimal solution with sliding window should be O(nlogn)
def optimal_solution(s: str, k: int) -> int:
    max_count = 0
    left = 0
    freq = defaultdict(int)

    for right in range(len(s)):
        freq[s[right]] += 1
        max_count = max(max_count, freq[s[right]])

        if right - left + 1 - max_count > k:
            freq[s[left]] -= 1
            left += 1

    return len(s) - left


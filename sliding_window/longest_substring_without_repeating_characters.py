from collections import defaultdict

def my_solution_longest_substring_without_repeating_characters(s: str) -> int:
    """
    MY SOLUTION:
    Find the length of the longest substring of a given string without repeating characters
    e.g. abccabcabcc output is 3 because of abc and cab, both have length 3
    Notes:
    After writing this, I'm realizing that this is not a sliding window and is O(nlogn) which is not optimal.
    :param s:
    """
    left, right = 0, 0
    curr_seen = []
    max_len = 0
    while right < len(s):
        if s[right] in curr_seen:
            left += 1
            right = left
            max_len = max(max_len, len(curr_seen))
            curr_seen = []
            continue
        curr_seen.append(s[right])
        right += 1
    return max_len

def optimal_solution(s: str) -> int:
    """
    Let left and right be on the left to start and get a dictionary with all characters mapped to zero to start with
    Let the right side iterate through the string and increment the number associated with each character as you read them
    If the right counters mapped character is greater than one, decrement the left character's associated value by 1 and
    move it to the right once.
    Each time you move the right over one, you re-evaluate the maximum value. Keep in mind that right and left are indices
    so you must add one to get a real "length."
    :param s:
    :return:
    """
    longest = 0
    left = 0
    counter: dict[str, int] = defaultdict(int) # sets all values in the dictionary to default 0
    for right in range(len(s)):
        counter[s[right]] += 1
        while counter[s[right]] > 1:
            counter[s[left]] -= 1
            left += 1
        longest = max(longest, right - left + 1)
    return longest


if __name__ == "__main__":
    input_str = "abccabcabcc"
    res1 = my_solution_longest_substring_without_repeating_characters(input_str)
    res2 = optimal_solution(input_str)
    print(res1, res2)
from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    To group together anagrams e.g. ate -> tea
    Create a dictionary with default of empty lists
    iterate through all of the strings, create a dictionary such that the key is just the sorted string
    append the actual string as the value such that all of the anagrams will be grouped together

    Return all of the values (not the sorted key)

    I was tempted to do a count with Counter, but that is not necessary here.
    """
    ans = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        ans[key].append(s)
    return list(ans.values())
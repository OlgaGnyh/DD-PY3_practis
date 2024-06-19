def is_anagram(s: str, t: str) -> bool:
    ...
    if sorted(s) == sorted(t):

        return True
    else:
        return False


print(is_anagram("rat", "car"))

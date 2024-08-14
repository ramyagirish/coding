# anagram problem
from collections import Counter

def anagram(s1: str, s2: str) -> bool:
    '''
    In this function we take two strings and we see if they are anagrams, 
    made of same characters and with same frequencies/counts
    Input
    s1, s2 -> two strings to be compared, usually one-word strings
    Output
    return value is a boolean to signify whether or not they are anagrams
    '''
    if (len(s1)==0) or (len(s2)==0):
        raise Exception("one or both strings are empty")
    if len(s1) != len(s2):
        return False
    count_s1 = Counter(list(s1.lower()))
    count_s2 = Counter(list(s2.lower()))
    return count_s1 == count_s2


print(anagram("Danger", "gardEn"))
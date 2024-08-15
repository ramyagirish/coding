# anagram problem
from collections import Counter
from typing import List

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

def binary_search(arr: List[int], high: int, low: int, x: int) -> int:
    '''
    In this function we perform binary search, here the strong assumption
    is that the array in which we search is already sorted.
    Input
    arr -> array to be where target is searched
    high -> highest index of sub array used for search
    low -> lowest index of sub array used for search
    x -> target to search
    Output
    returns index of target if found in arr else returns -1
    '''
    if len(arr)==0:
        return -1
    if high >= low:
        mid = (high+low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, mid-1, low, x)
        elif arr[mid] < x:
            return binary_search(arr, high, mid+1, x)
        else:
            return -1
    else:
        return -1
    
def binary_search_opt(arr: List[int], x: int) -> int:
    '''
    In this function we perform binary search, here the strong assumption
    is that the array in which we search is already sorted.
    Input
    arr -> array to be where target is searche
    x -> target to search
    Output
    returns index of target if found in arr, this is the index of first occurance 
    else returns -1
    '''
    if len(arr)==0:
        return -1
    arr = sorted(arr)
    if arr[-1] == x:
        return len(arr) - 1
    if arr[0] == x:
        return 0
    low, high = 0, len(arr) - 1
    while high >= low:
        mid = (high+low)//2
        if (arr[mid] == x) and (arr[mid-1] < x):
            return mid
        elif arr[mid] < x:
            low = mid+1
        else:
            high = mid-1
    else:
        return -1
    
def first_last_1(arr: List[int], target: int) -> List[int]:
    '''
    In this function we take an array, sort it if its not and
    find the first and last index of element(s) matching target
    Input
    arr -> array to be where target is searched
    target -> integer to be search
    Output 
    returns list with first and last element if found else retun=rns [-1,-1]
    '''
    arr = sorted(arr)
    try:
        ind = arr.index(target)
        return [ind, ind + arr.count(target) - 1]
    except ValueError:
        return [-1,-1]
    
def first_last(arr: List[int], target: int) -> List[int]:
    '''
    In this function we take an array, sort it if its not and
    find the first and last index of element(s) matching target
    Input
    arr -> array to be where target is searched
    target -> integer to be search
    Output 
    returns list with first and last element if found else retun=rns [-1,-1]
    '''
    arr = sorted(arr)
    ind = binary_search(arr, len(arr)-1, 0, target)
    if (ind > 0) and (target in arr[:ind]):
        init = ind
        temp = arr[:init]
        while target in temp:
            if init > 0:
                init -= 1
                temp = arr[:init]
        ind = init
    if ind != -1:
        count = 0
        init = ind
        temp = arr[init:]
        while(target in temp):
            count += 1
            init += 1
            temp = arr[init:]
        return [ind, ind + count - 1]
    else:
        return [ind,ind]
   

p = [3,4,1,7,9,9,9,8,9,4,12,14]
print(binary_search_opt(p, 9))


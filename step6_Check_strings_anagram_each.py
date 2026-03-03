'''Check if two Strings are anagrams of each other
Problem Statement: Given two strings, check if two strings are anagrams of each other or not.
'''
def are_anagrams(s1, s2): #function to check if two strings are anagrams of each other
    if len(s1) != len(s2): #if the lengths of the strings are different, return false
        return False
    if sorted(s1) == sorted(s2): #if the sorted characters of both strings are the same, return true
        return True
    return False #if the sorted characters of both strings are different, return false
#example
s1 = "listen" #input
s2 = "silent" #input
print(are_anagrams(s1, s2)) #output: true
'''tc: O(n log n) where n is the length of the input strings. This
is because we are sorting the characters of both strings, which takes O(n log n) time.
sc: O(n) because we are using new strings that are the sorted versions of the input strings, which takes O(n) space.'''
#optimal approach
def are_anagrams_optimal(s1, s2): #function to check if two strings
    if len(s1) != len(s2): #if the lengths of the strings are different, return false
        return False
    count = {} #initialize a dictionary to count the occurrences of each character in the first string
    for char in s1: #iterate through the characters of the first string
        count[char] = count.get(char, 0) + 1 #increment the count of the character in the dictionary
    for char in s2: #iterate through the characters of the second string
        if char not in count or count[char] == 0: #if the character is not in the dictionary or its count is zero, return false
            return False
        count[char] -= 1 #decrement the count of the character in the dictionary
    return True #if we have compared all characters and found no mismatch, return true
#example
s1 = "listen" #input

s2 = "silent" #input
print(are_anagrams_optimal(s1, s2)) #output: true
'''tc: O(n) where n is the length of the input strings. This is because we are counting the occurrences of each character in the first string and comparing it with the characters in the second string, which takes O(n) time.
sc: O(1) because we are using a dictionary to count the occurrences of each character, and the number of unique characters is limited by the character set (e.g., ASCII), which can be considered constant space.'''
 
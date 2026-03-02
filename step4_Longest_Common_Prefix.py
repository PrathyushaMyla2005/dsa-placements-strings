'''Problem Statement: Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".'''
def longest_common_prefix(strs): #function to find the longest common prefix
    if not strs: #if the input list is empty.return an empty string
        return ""
    strs.sort() #sort the list of strings
    first = strs[0] #get the first string in the sorted list
    last = strs[-1] #get the last string in the sorted list
    i = 0 #initialize index to 0
    while i < len(first) and i < len(last) and first[i] == last[i]: #while the index is within the bounds of both strings and the characters at the index are the same
        i += 1 #increment the index
    return first[:i] #return the substring of the first string from the start to the index
#example
strs = ["flower","flow","flight"] #input
print(longest_common_prefix(strs)) #output: "fl"
'''tc: O(n log n) where n is the number of strings in the input list. This is because we are sorting the list of strings.
sc: O(1) because we are using only a constant amount of extra space to store the variables.'''
'''optimal approach
We can also solve this problem using a vertical scanning approach. We can compare the characters of the
strings at the same index until we find a mismatch. The longest common prefix will be the substring from the start to the index of the mismatch. This approach has a time complexity of O(m*n) where m is the length of the longest string and n is the number of strings in the input list. The space complexity is O(1) because we are using only a constant amount of extra space to store the variables.'''
def longest_common_prefix_vertical(strs): #function to find the longest common prefix using vertical scanning
    if not strs: #if the input list is empty.return an empty string
        return ""
    for i in range(len(strs[0])): #iterate through the characters of the first string
        char = strs[0][i] #get the character at the current index
        for j in range(1, len(strs)): #iterate through the rest of the strings
            if i >= len(strs[j]) or strs[j][i] != char: #if the index is out of bounds for the current string or the character at the index is different from the character in the first string
                return strs[0][:i] #return the substring of the first string from the start to the index
    return strs[0] #if we have compared all characters and found no mismatch, return the first string as the longest common prefix  
#example
strs = ["flower","flow","flight"] #input
print(longest_common_prefix_vertical(strs)) #output: "fl"
'''tc: O(m*n) where m is the length of the longest string and n is the number of strings in the input list. This is because we are comparing each character of the strings until we find a mismatch.
sc: O(1) because we are using only a constant amount of extra space to store the variables.'''

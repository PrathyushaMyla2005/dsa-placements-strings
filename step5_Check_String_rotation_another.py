'''Check if one string is rotation of another
Problem Statement: Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position. For example, if s = "abcde", then it will be "bcdea" after one shift.
Examples
Example 1:
Input:
 s = "rotation", goal = "tionrota"
Output:
 true
Explanation:
 After multiple left shifts on "rotation", we get:
    1st shift → "otationr"
    2nd shift → "tationro"
    3rd shift → "ationrot"
    4th shift → "tionrota"
    So the goal string can be obtained by rotating the original string.
Example 2:
Input:
 s = "hello", goal = "lohelx"
Output:
 false'''
def is_rotation(s,goal): #function to check if one string is rotation of another
    if len(s) != len(goal): #if the lengths of the strings are different, return false
        return False
    for i in range(len(s)): #iterate through the characters of the first string
        if s[i:] + s[:i] == goal: #if the substring from the current index to the end concatenated with the substring from the start to the current index is equal to the goal string, return true
            return True
    return False #if we have compared all rotations and found no match, return false
#example
s = "rotation" #input
goal = "tionrota" #input
print(is_rotation(s,goal)) #output: true
'''tc: O(n^2) where n is the length of the input string. This
is because we are generating all possible rotations of the string and comparing them to the goal string.
sc: O(n) because we are using a substring of the input string to generate the rotations
and the space used by the substring is proportional to the length of the input string.'''
#optimal approach
def is_rotation_optimal(s,goal): #function to check if one string is rotation of
    if len(s) != len(goal): #if the lengths of the strings are different, return false
        return False
    return goal in s + s #check if the goal string is a substring of the concatenation of the input string with itself
#example
s = "rotation" #input
goal = "tionrota" #input
print(is_rotation_optimal(s,goal)) #output: true
'''tc: O(n) where n is the length of the input string. This is because
we are checking if the goal string is a substring of the concatenation of the input string with itself, which takes O(n) time.
sc: O(n) because we are using a new string that is the concatenation of the input string with itself, which takes O(n) space.'''
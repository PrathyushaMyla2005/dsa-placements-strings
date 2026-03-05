'''parentheses.
Problem Statement: Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.
Example 1:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3'''
def maxDepth(s):#create the function
    max_depth = 0 #initialize the maximum depth to 0
    current_depth = 0 #initialize the current depth to 0
    for char in s: #iterate through each character in the string
        if char == '(': #if the character is an opening parenthesis
            current_depth += 1 #increment the current depth
            max_depth = max(max_depth, current_depth) #update the maximum depth if necessary
        elif char == ')': #if the character is a closing parenthesis
            current_depth -= 1 #decrement the current depth
    return max_depth #return the maximum depth
# Example usage
s = "(1+(2*3)+((8)/4))+1"
print(maxDepth(s)) # Output: 3
'''tc: O(n) where n is the length of the input string s, as we need to iterate through each character in the string once.
sc: O(1) as we are using only a constant amount of extra space to store the maximum depth and current depth.'''

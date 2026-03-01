'''Remove Outermost Parentheses
Problem Statement: A valid parentheses string is defined by the following rules:
It is the empty string "".
If A is a valid parentheses string, then so is "(" + A + ")".
If A and B are valid parentheses strings, then A + B is also valid.
A primitive valid parentheses string is a non-empty valid string that cannot be split into two or more non-empty valid parentheses strings.
Given a valid parentheses string s, your task is to remove the outermost parentheses from every primitive component of s and return the resulting string.'''
def removeOuterParentheses(s):#function to remove outermost parentheses
    result = "" #initialize result string
    level = 0#initialize level to keep track of the depth of parentheses
    for char in s: #iterate through each character in the input string
        if char == '(':#if the character is an opening parenthesis
            if level > 0:#if we are inside a valid parentheses string, add the character to the result  
                result += char #add the opening parenthesis to the result string
            level += 1#increment the level as we have encountered an opening parenthesis
        elif char == ')':#if the character is a closing parenthesis
            level -= 1#decrement the level as we have encountered a closing parenthesis
            if level > 0:#`if we are still inside a valid parentheses string after encountering a closing parenthesis, add the character to the result`
                result += char#add the closing parenthesis to the result string if we are still inside a valid parentheses string
    return result #return the final result string
s = "(()())(())" #input string
# Call the function to remove outermost parentheses and print the result
print(removeOuterParentheses(s))
'''tc: O(n) where n is the length of the input string s, as we need to iterate through each character in the string once.
sc: O(n) in the worst case, if all characters in the input string are parentheses
and we need to store the result string, which can be as long as the input string. However, in practice, the space complexity may be less than O(n) if there are many primitive components in the input string, as we will be removing the outermost parentheses from each component.'''

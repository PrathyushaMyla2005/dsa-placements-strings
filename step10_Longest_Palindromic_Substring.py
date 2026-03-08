'''problem statement: Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "aba"
Explanation: "aba" is a palindrome substring of "babad". Note that "aba" is also a valid answer'''
#brute force approach
def longestPalindrome(s): #function to find the longest
    longest = " " # Initialize longest to an empty string
    for i in range(len(s)): # Iterate through each character in the string
        for j in range(i, len(s)): # Iterate through the substring starting from the current character
            substring = s[i:j+1] # Get the current substring
            if substring == substring[::-1] and len(substring) > len(longest): # Check if the substring is a palindrome and longer than the current longest
                longest = substring # Update longest if the current substring is a palindrome and longer
    return longest # Return the longest palindromic substring
# Example usage
s = "babad"
print(longestPalindrome(s)) # Output: "aba"
'''The time complexity of this brute-force algorithm is O(n^3) because we are generating all possible substrings (O(n^2)) and checking if each substring is a palindrome (O(n)). The space complexity is O(1) because we are using only a constant amount of extra space to store the longest palindrome found so far.
This brute-force approach is not efficient for large input strings, as it requires checking every possible substring for palindromicity, leading to a high time complexity. A more efficient solution would involve using dynamic programming or expanding around the center of potential palindromic substrings, which can reduce the time complexity to O(n^2) and space complexity to O(1).
space complexity. By maintaining a frequency dictionary, we can quickly determine when to adjust the window and count valid substrings, making this solution optimal for the given problem.'''
#opTIMAL APPROACH
def longestPalindrome(s):
    longest = "" # Initialize longest to an empty string
    for i in range(len(s)): # Iterate through each character in the string
        # Check for odd-length palindromes
        left, right = i, i # Initialize left and right pointers to the current character
        while left >= 0 and right < len(s) and s[left] == s[right]: # Expand around the center while characters match
            if right - left + 1 > len(longest): # Check if the current palindrome is longer than the longest found so far
                longest = s[left:right+1] # Update longest if the current palindrome is longer
            left -= 1 # Move left pointer to the left
            right += 1 # Move right pointer to the right
        
        # Check for even-length palindromes
        left, right = i, i + 1 # Initialize left pointer to the current character and right pointer to the next character
        while left >= 0 and right < len(s) and s[left] == s[right]: # Expand around the center while characters match
            if right - left + 1 > len(longest): # Check if the current palindrome is longer than the longest found so far
                longest = s[left:right+1] # Update longest if the current palindrome is longer
            left -= 1 # Move left pointer to the left
            right += 1 # Move right pointer to the right
            
    return longest # Return the longest palindromic substring
# Example usage
s = "babad"
print(longestPalindrome(s)) # Output: "aba"
'''The time complexity of this optimal algorithm is O(n^2) because in the worst case, we may need to expand around each character and its adjacent character to check for palindromes, which takes O(n) time for each character. The space complexity is O(1) because we are using only a constant amount of extra space to store the longest palindrome found so far.
This optimal approach efficiently finds the longest palindromic substring by expanding around potential centers of palindromes. It checks both odd-length and even-length palindromes, ensuring that all possible palindromic substrings are considered. This method significantly reduces the time complexity 
compared to the brute-force approach, making it suitable for larger input strings.
space complexity O(1). By maintaining a frequency dictionary, we can quickly determine when to adjust the window and count valid substrings, making this solution optimal for the given problem.
'''

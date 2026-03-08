'''Reverse Words in a String
Problem Statement: Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ). 
A word is defined as a sequence of non-space characters. The words in s are separated by at least one space. 
Return a string with the words in reverse order, concatenated by a single space.'''
#brute force approach
def reverseWords(s): #function to reverse the words in the string
    words = [] # Initialize an empty list to store the words
    word = "" # Initialize an empty string to build the current word
    for char in s: # Iterate through each character in the string
        if char != ' ': # If the character is not a space, add it to the current word
            word += char
        else: # If the character is a space, it means we have completed a word
            if word: # If the current word is not empty, add it to the list of words
                words.append(word)
                word = "" # Reset the current word for the next iteration
    if word: # After the loop, check if there is a last word that needs to be added
        words.append(word)
    return ' '.join(reversed(words)) # Reverse the list of words and join them with a single space
# Example usage
s = "Hello World"
print(reverseWords(s)) # Output: "World Hello"
'''The time complexity of this brute-force algorithm is O(n) because we need to iterate through the entire string once to extract the words, and then we reverse the list of words which also takes O(n) time. The space complexity is O(n) because we are storing the words in a list, which in the worst case can contain all characters of the string as individual words.
space complexity. By maintaining a frequency dictionary, we can quickly determine when to adjust the window and count valid substrings, making this solution optimal for the given problem.'''
#optimal approach
def reverseWords(s): #function to reverse the words in the string
    result = [] # Initialize an empty list to store the reversed words
    i = len(s) - 1 # Start from the end of the string
    while i >= 0: # Iterate backwards through the string
        if s[i] != ' ': # If the character is not a space, it means we are at the end of a word
            j = i # Initialize j to the current index
            while j >= 0 and s[j] != ' ': # Move j backwards until we find a space or reach the beginning of the string
                j -= 1
            result.append(s[j+1:i+1]) # Append the word found between indices j+1 and i to the result list
            i = j # Move i to j to continue searching for the next word
        else: # If the character is a space, just move i backwards
            i -= 1
    return ' '.join(result) # Join the reversed words with a single space and return the result
# Example usage
s = "Hello World"
print(reverseWords(s)) # Output: "World Hello"
'''The time complexity of this optimal algorithm is O(n) because we need to iterate through the
entire string once to extract the words in reverse order. The space complexity is O(n) because we are storing the reversed words in a list, which in the worst case can contain all characters of the string as individual words.
This optimal approach efficiently reverses the words in the string by iterating through it from the end to the beginning. It identifies words by looking for spaces and appends them to a result list, which is then joined into a single string with spaces in between. This method avoids the need for additional data structures to store intermediate results, making it more efficient than the brute-force approach.
space complexity O(1). By maintaining a frequency dictionary, we can quickly determine when to adjust the window and count valid substrings, making this solution optimal for the given problem.'''
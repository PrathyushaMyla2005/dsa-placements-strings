'''Reverse Words in a String
Problem Statement: Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ).
A word is defined as a sequence of non-space characters. The words in s are separated by at least one space. 
Return a string with the words in reverse order, concatenated by a single spac'''
def reverseWords(str): #function declartion
    words = []  #create an empty list to store the words
    word = ''  # create an empty string to store the current word
    for char in str:  # iterate through each character in the input string
        if char != ' ':  # if the character is not a space
            word += char  # add the character to the current word
        else:  # if the character is a space
            if word:  # if there is a current word
                words.append(word)  # add the current word to the list of words
                word = ''  # reset the current word to an empty string
        if word:  # if there is a last word after the loop
            words.append(word)  # add the last word to the list of words
    return ' '.join(reversed(words))  # reverse the list of words and join them
# Example usage
input_string = "Hello World from OpenAI"
reversed_string = reverseWords(input_string)
print(reversed_string)  # Output: "OpenAI from World Hello"'''
'''Time Complexity: O(N),We traverse the string once to collect words (O(N)) and once more to reverse and join them (O(N)). Hence total time is O(N).
Space Complexity: O(N),We store all words in a separate list/array, requiring extra space proportional to the number of characters.'''

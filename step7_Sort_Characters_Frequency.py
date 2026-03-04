'''
Sort characters by frequency and alphabetically
Problem Statement: You are given a string s. Return the array of unique characters, sorted by highest to lowest occurring characters.
If two or more characters have same frequency then arrange them in alphabetic order'''
def sort_characters_frequency(s): # function definition
    frequency = {} # initialize an empty dictionary to store the frequency of characters
    for char in s: # iterate through the string
        frequency[char] = frequency.get(char, 0) + 1 # update the frequency of the character in the dictionary
    sorted_characters = sorted(frequency.keys(), key=lambda x: (-frequency[x], x)) # sort the characters by frequency and alphabetically
    return sorted_characters # return the sorted characters
s = "tree" # given input string
print("Sorted characters by frequency:", sort_characters_frequency(s)) # call function and print the
'''Time Complexity: O(n log n) where n is the number of unique characters in the string as we are sorting the characters based on their frequency and alphabetically.
Space Complexity: O(n) where n is the number of unique characters in the string as we are storing the frequency of characters in a dictionary and the sorted characters in a list.'''
'''trace   the example in the code
s = "tree"
frequency = {'t': 1, 'r': 1, 'e': 2}
sorted_characters = sorted(frequency.keys(), key=lambda x: (-frequency[x], x))
sorted_characters = sorted(['t', 'r', 'e'], key=lambda x: (-frequency[x], x)) 
sorted_characters = sorted(['t', 'r', 'e'], key=lambda x: (-1, 't'))
sorted_characters = sorted(['t', 'r', 'e'], key=lambda x: (-1, 'r'))
sorted_characters = sorted(['t', 'r', 'e'], key=lambda x: (-2, 'e'))
sorted_characters = ['e', 'r', 't']
The sorted characters by frequency are ['e', 'r', 't'], where 'e' occurs 2 times, 'r' and 't' occur 1 time each. Since 'r' and 't' have the same frequency, they are sorted alphabetically.
'''
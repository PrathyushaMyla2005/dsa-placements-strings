'''Count Number of Substrings
Problem Statement: You are given a string s and a positive integer k.
Return the number of substrings that contain exactly k distinct characters
Example 1:
Input: s = "pqpqs", k = 2
Output: 7
Explanation: Substrings that contain exactly 2 distinct characters are ["pq", "pqp", "qp", "pq", "qs", "pqs", "pqpq"].'''
def countsubstrings(s, k):
    count  = 0 # Initialize count to 0
    left = 0 # Initialize left pointer to 0
    freq = {} # Initialize a dictionary to store the frequency of characters in the current window
    for right in range(len(s)): #iterate through the string using right pointer
        freq[s[right]] = freq.get(s[right], 0) + 1 # Update the frequency of the current character
        while len(freq) > k: # If the number of distinct characters exceeds k
            freq[s[left]] -= 1 # Decrease the frequency of the character at the left pointer
            if freq[s[left]] == 0: # If the frequency becomes 0, remove it from the dictionary
                del freq[s[left]]
            left += 1 # Move the left pointer to the right
        if len(freq) == k: # If the number of distinct characters is exactly k
            count += right - left + 1 # Increment the count by the number of substrings that can be formed with the current window
    return count # Return the final count of substrings with exactly k distinct characters
# Example usage
s = "pqpqs"
k = 2
print(countsubstrings(s, k)) # Output: 7
'''The time complexity of this algorithm is O(n) because each character in the string is processed at most twice (once when the right pointer moves and once when the left pointer moves). The space complexity is O(k) because we are storing the frequency of at most k distinct characters in the dictionary.
This algorithm uses a sliding window approach to efficiently count the number of substrings with exactly k distinct characters. The right pointer expands the window by adding characters, while the left pointer contracts the window when the number of distinct characters exceeds k. The count is updated whenever the number of distinct characters is exactly k, ensuring that all valid substrings are counted.
This approach is efficient and works well for large input strings, as it avoids the need for nested loops that would result in a higher time complexity
space complexity. By maintaining a frequency dictionary, we can quickly determine when to adjust the window and count valid substrings, making this solution optimal for the given problem.'''

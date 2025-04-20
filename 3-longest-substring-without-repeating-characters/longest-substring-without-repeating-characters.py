class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # HashMap to store the last seen index of characters
        left = 0  # Left pointer of the sliding window
        max_length = 0

        for right in range(len(s)):
            if s[right] in char_index:
                left = max(char_index[s[right]] + 1, left)  # Move left past the duplicate
            
            char_index[s[right]] = right  # Update the last seen index
            max_length = max(max_length, right - left + 1)  # Update max length

        return max_length


        
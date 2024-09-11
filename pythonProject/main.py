def length_of_longest_substring(s: str) -> int:
    # Hash map to store the last indices of characters
    char_index_map = {}
    max_length = 0
    start = 0

    for end, char in enumerate(s):
        # If the character is found in the map and its index is within the current window
        if char in char_index_map and char_index_map[char] >= start:
            # Move the start to the next position of the last occurrence of the character
            start = char_index_map[char] + 1
        # Update the last occurrence of the character
        char_index_map[char] = end
        # Calculate the max length
        max_length = max(max_length, end - start + 1)

    return max_length


# Example
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3

def is_anagram_template(string_s: str, string_t: str) -> bool:
    # If the lengths aren't identical, they cannot be anagrams
    if len(string_s) != len(string_t):
        return False
        
    # We will track character counts here
    char_counts = {}
    
    # Fill the frequency map for the first string
    for char in string_s:
        char_counts[char] = char_counts.get(char, 0) + 1
        
    # Decrement counts using the second string to verify matches
    for char in string_t:
        # If a character isn't in our map, string_t has an extra character
        if char not in char_counts:
            return False
        char_counts[char] -= 1
        # If count drops below zero, string_t has too many of this character
        if char_counts[char] < 0:
            return False
            
    # If all checks pass, it's a perfect match
    return True
string_s = "rat"
string_t = "car"
print(is_anagram_template("abc", "def"))
def reverse_string(s):
    left ,right =0, len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return s
word=input("Enter a word to reverse: ")
print(reverse_string(list(word)))
print(reverse_string(["h","e","l","l","o"]))

# task 1 : Check if a string is palindrome or not
string="ana"

reverse_string=string[::-1]
print(reverse_string)
if string==reverse_string:
    print("Palindrome")
else:
    print("Not Palindrome")

left: int = 0
right: int = len(string) - 1
while left < right:
    if string[left] != string[right]:
        print("Not Palindrome")
        break
    left += 1
    right -= 1
else:
    print("Palindrome")
for i in range(len(string)//2):
    if string[i]!=string[len(string)-1-i]:
        print("Not Palindrome")
        break
else:
    print("Palindrome")

# task 2 : Count frequency of each character in a string
sentence="dhbcbnmdwpk"
sen_list=list(sentence)
for char in sen_list:
    print(f"{char} occurs {sen_list.count(char)} times")

#task 3 : Reverse words in a sentence (“hello world” → “world hello”)
sentences="hello world"
words=sentences.split() 
print(" ".join(words[::-1]))  # Reverse the order of words and join them with a comma and space

#task 4 :  Check if two strings are anagrams of each other

word1="listen"
word2="silent"
if sorted(word1) == sorted(word2):
    print("Anagrams")
else:
    print("Not Anagrams")

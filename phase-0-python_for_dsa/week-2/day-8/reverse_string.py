def reverse(word):
    n=len(word)
    if n<=1:
        return word
    return reverse(word[1:])+word[0]
print(reverse("hello"))
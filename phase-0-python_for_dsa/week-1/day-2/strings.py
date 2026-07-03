single_quoted_string = 'This is a "single" \'quoted\' string.'
double_quoted_string = "This is a \"double\" quoted string."
triple_quoted_string = """Triple quoted strings may span multiple lines
 - all associated whitespace will be included in the string literal.
"""
print("spam" "eggs")
# Strings are immutable in Python, meaning that once a string is created, it cannot be changed. Any operation that modifies a string will create a new string object.
msg='hello universe ß'
# capitalize the first letter of the string
m1=msg.capitalize()  
print(m1)
print(msg)

# casefold() converts the string to lowercase
m2=msg.casefold()  
print(m2)

# center() centers the string within a specified width, padding it with a specified character
m3=msg.center(20,"-")
print(m3)

# count() counts the occurrences of a substring in the string
m4=msg.count("e",5)
m4=msg.count("")
print(m4)
print(len(msg))

# encode() encodes the string into bytes using a specified encoding (default is UTF-8)
m5=msg.encode()
print(m5)

# find() returns the lowest index of the substring if found, otherwise -1
m6=msg.find("e",2)
print(m6)

# index() returns the lowest index of the substring if found, otherwise raises a ValueError
m7=msg.index("e",3)
print(m7)

# format() formats the string using placeholders and values
m8="{}".format(msg)
m8=f"hey,{msg}"
print(m8)

# join() joins the elements of an iterable (like a list or tuple) into a single string, using the specified separator
m9=",".join(["hello","universe","ß"])
m9="-".join('Python')
print(m9)

# split() splits the string into a list of substrings based on a specified separator (default is whitespace)
m10=msg.split(" ")
print(m10)

# splitlines() splits the string into a list of lines, breaking at line boundaries
m11=msg.splitlines()
print(m11)

# replace() replaces occurrences of a substring with another substring, optionally limiting the number of replacements
m12=msg.replace("e","E",1)
print(m12)

# strip() removes leading and trailing whitespace (or specified characters) from the string
m13=msg.strip("h")
print(m13)

# upper() converts all characters in the string to uppercase
m14=msg.upper()
print(m14)

# lower() converts all characters in the string to lowercase
m15=msg.lower()
print(m15)

# title() converts the first character of each word to uppercase and the rest to lowercase
m17=msg.title()
print(m17)

# swapcase() converts uppercase characters to lowercase and vice versa
m16=msg.swapcase()
print(m16)

# startswith() checks if the string starts with a specified substring, returning True or False
m18=msg.startswith("h")
print(m18)

# endswith() checks if the string ends with a specified substring, returning True or False
m19=msg.endswith("ß")
print(m19)

# zfill() pads the string with zeros on the left, to fill a specified width
m20=msg.zfill(20)
print(m20)

# partition() splits the string into a tuple of three parts: the part before the separator, the separator itself, and the part after the separator
m21=msg.partition(" ")
print(m21)

print(ord("a"))
print(chr(97))

# wrong way in string building as O(n^2) time complexity
s="hello universe ß"
result=""
for c in s:
    result += c
print(result)

# right way in string building as O(n) time complexity
chars=[]
for c in s:
    chars.append(c)
print(chars)
result="".join(chars)
print(result)

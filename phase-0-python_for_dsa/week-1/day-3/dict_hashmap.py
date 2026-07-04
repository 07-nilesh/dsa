# Creation
d={}
d=dict()
d={"a":1,"b":2,"c":3}

# operations
d["d"]=4    # Add a new key-value pair
print(d)    # Print the dictionary
d["a"]=10   # Update the value of an existing key
print(d)    # Print the dictionary
#print(d["g"])  # Print the value of key -keyerror if not found
print(d.get("g"))  # Print the value of key - returns None if not found
print(d.get("g", "Key not found"))  # Print the value of key - returns default value if not found
print("a" in d)  # Check if key exists in dictionary
print(len(d))  # Print the number of key-value pairs in the dictionary
del d["b"]  # Delete a key-value pair
print(d)    # Print the dictionary
popped=d.pop("c", None)  # Remove a key-value pair and return its value
print(d)    # Print the dictionary
print(popped)  # Print the value of the removed key-value pair

#iteration
for key in d:  # Iterate through the keys of the dictionary
    print(key)
for key, value in d.items():  # Iterate through the key-value pairs of the dictionary
    print(key, value)
for value in d.values():  # Iterate through the values of the dictionary
    print(value)

# defaultdict - mostly used in competitive programming
from collections import defaultdict
freq=defaultdict(int)  # Create a defaultdict with default value 0
print(freq["a"])  # Print the value of key "a" - returns 0 if not found
freq["a"] += 1  # Increment the value of key "a" by 1
print(freq["a"])  # Print the value of key "a"

graph =defaultdict(list)  # Create a defaultdict with default value as an empty list []
graph[0].append(1)  # Add an edge from node 0 to node 1
graph[0].append(2)  # Add an edge from node 0 to node
print(graph)  # Print the graph

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)  # Append the value to the list of the corresponding key
print(sorted(d.items()))  # Print the sorted key-value pairs of the dictionary

d = {}
for k, v in s:
    d.setdefault(k, []).append(v)  # Append the value to the list of the corresponding key
print(sorted(d.items()))  # Print the sorted key-value pairs of the dictionary

s = 'mississippi'
d = {}
for k in s:
    d[k] = d.get(k, 0) + 1  # Increment the count of the character
print(sorted(d.items()))  # Print the sorted key-value pairs of the dictionary
d=defaultdict(int)
for k in s:
    d[k] += 1  # Increment the count of the character
print(d)  # Print the sorted key-value pairs of the dictionary

from collections import Counter
s = 'mississippi'
d = Counter(s)  # Create a Counter object to count the occurrences of each character
print(d)  # Print the Counter object
print(d.most_common(2))  # Print the two most common characters and their counts
print(d["a"])  # Print the count of the character "a"
print(d["i"])  # Print the count of the character "i"
print(sorted(d.elements()))  # Print an iterator over elements repeating each as many times as its count
print(d.total())  # Print the total of all counts
print(list(d))  # Print a list of unique elements
print(set(d))  # Print a set of unique elements
print(dict(d))  # Print a dictionary of elements and their counts
print(d.items())  # Print a view of the elements and their counts
print(+d)  
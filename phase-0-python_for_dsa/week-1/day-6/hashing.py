# how python hashing works internally

# hash() function - convert any object to an integer
print(hash("helllo"))  #6969277158368001454
print(hash(42)) #42
print(hash((1,2)))  #works tuples are hashable
#print(hash([1,2])) TypeError: unhashable type: 'list
#print(hash({1,2})) TypeError: unhashable type: 'set'
#print(hash({1:'a'}))   TypeError: unhashable type: 'dict'
# Using dict (key-value pairs)
marks = {"Nilesh": 85, "Rahul": 90, "Priya": 78}
print(marks["Rahul"])       # 90
# Hash of the key
print(hash("Rahul"))        # Dict uses this to locate the value

# Using set (unique elements, fast lookup)
fruits = {"apple", "banana", "cherry"}
print("banana" in fruits)   # True
print("grape" in fruits)    # False
# Behind the scenes:
print(hash("banana"))       # Shows the hash used internally


#Hashable (can be dictkey/set elements): int,float.str.tuple.bool
# unhashable(cannot):list,dict,set

# problem : given a list of lists , find duplicates
data=[[1,2],[3,4],[1,2]]
seen=set()
for row in data:
    key=tuple(row)
    if key in seen:
        print("duplicate:", row)
    seen.add(key)

#group anagrams - sorted string as key
from collections import defaultdict
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key=tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())
print(group_anagrams(["silent","listen"])) #[['silent', 'listen']]
print(group_anagrams(["ease","vase"]))  # [['ease'], ['vase']]
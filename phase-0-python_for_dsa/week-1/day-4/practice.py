from collections import Counter
from collections import defaultdict
word="abracadabra"
freq=Counter(word)
print(freq)
for value in word:
    if freq[value]==1:
        print(value)
        break

arr=[1,3,1,2,3]
unique=set()
duplicates=[]
for i in arr:
    if i in unique:
        duplicates.append(i)
    else:
        unique.add(i)
print(duplicates)

ls=['listen','silent','earth','heart']
grp=defaultdict(list)
for word in ls:
    key=tuple(sorted(word))
    grp[key].append(word)
print(list(grp.values()))





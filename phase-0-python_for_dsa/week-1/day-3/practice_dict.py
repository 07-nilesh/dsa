details={"name":"John","age":30,"city":"New York"}
name=details.get("name","Not Found")  
print(name)
check="city" in details
print(check)


for key in details:
    print(key)
for value in details.values():
    print(value)
for key,value in details.items():
    print(key,value)

from collections import Counter
freq= Counter("abracadabra")
print(freq)    

from collections import defaultdict
d=defaultdict(int)

print(d["a"])  # returns 0
c=defaultdict(list)
c["a"].append(1)
print(c["a"])  # returns [1]
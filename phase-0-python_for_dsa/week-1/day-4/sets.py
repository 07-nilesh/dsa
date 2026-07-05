s=set() # create a empty set
s={1,2,3}
print(s)
s.add(4)
s.update([5,6])
print(s)
s.remove(6)
s.discard(5)
print(s)
if 4 in s:
    print("found")

# fast duplicate removal
s1=[1,2,(4,5)]
unique=set(s1)
print(unique)

my_set={1,2,3}
#my_set.remove(99)
my_set.discard(99)
arr=[3,1,4,1,5,9,2,6]
arr.sort() #modifies the list in-place, returns None TC: O(nlogn)
print(arr) #only defines for list

new_list=sorted(arr)    #newlist TC : O(nlogn) accepts any iterable
print(new_list)         # leaves original list intact, returns a new sorted list

#descending
arr.sort(reverse=True)
print(arr)

#sort by absolute value
arr.sort(key=lambda x: abs(x))
print(arr)

# sort tuples by 2nd than 1st
a=[(1,2),(4,2),(5,1)]
a.sort(key=lambda x:( x[1],x[0]))
print(a)

s=["hello","world","universe","abb"]
s.sort(key=len)
print(s)

points = [(1, 5), (4, 1), (2, 3)]
points.sort(key=lambda x:x[1])
print(points)
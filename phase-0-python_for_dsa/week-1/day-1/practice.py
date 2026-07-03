# 1.Create a 2D matrix 4x4 filled with zeros from scratch
arr=[[0]*4 for _ in range(4)]
print(arr)

# 2.reverse a list 3 different ways (slicing, loop, built-in)
arr1=list(range(10))
# Using slicing
print(arr1[::-1])
# Using loop
reversed_arr=[]
for i in range(len(arr1)-1,-1,-1):
    reversed_arr.append(arr1[i])
print(reversed_arr)
# Using built-in function
arr1.reverse()
print(arr1)
arr1.sort(reverse=True)
print(arr1)

# 3.Sort a list of strings by their length
strings=["apple","banana","kiwi","grape","watermelon"]
# Using sorted with key
sorted_strings=sorted(strings, key=len)
print(sorted_strings)
# Using sort with key
strings.sort(key=len)
print(strings)

# 4.Find the second largest element in a list without sorting
# directly finding the second largest element
arr1=[3,5,1,8,2,7]

def second_largest(arr):
    first=second=float('-inf')
    for num in arr:
        if num>first:
            #new largest found, old largest becomes second largest
            second=first
            first =num
        elif first>num>second:
            #new second largest found
            second=num
    return second

print(second_largest(arr1))

arr1=[3,5,1,8,2,7]
first=second=float('-inf')
for i in range(len(arr1)):
    
    if arr1[i]>first:
        second=first
        first=arr1[i]
    elif first>arr1[i]>second:
        second=arr1[i]
print(second)

#5.Create list 5 ways (literal, range, comprehension, * operator, list())
list1=[1,2,3,4,5]
list2=list(range(6,11))
list3=[x for x in range(11,16)]
list4=[1]*5
list5=list([1,2,3,4,5])
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)

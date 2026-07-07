t1=(1,2,3,)
t2=1,2,3,
t3=(1,)
t4=(1)  # tuples are created using comma not parenthesis()
print(type(t1))
print(type(t2))
print(type(t3))
print(type(t4))
#t5=tuple(5)  #TypeError: 'int' object is not iterable
#print(t5)
empty_t=()
empty_t1=tuple()

# tuple are generally smaller and faster than list
import sys
ls= [12,2,33,1,3,213]
tup= (12,2,33,1,3,213)
print(sys.getsizeof(ls))
print(sys.getsizeof(tup))

# immutability applies to tuple conatiner not object
t=(1,[2,3])
t[1].append(4)
print(t)
# print(t.append(2))  AttributeError: 'tuple' object has no attribute 'append

#accessing
fruits=('apple','banana','cherry','dates')
print(fruits[0])
print(fruits[1:3])
print(fruits[::-1])
print(fruits[-2])
#nested tuples
nested_tuples=((1,2),(3,4),(5,6))
print(nested_tuples[0][1])

#tuples are heterogeneous
t=(42,"hello",[1,2,3],{"key":"value"})
print(t[3]["key"])

#unpacking
a,b,c=1,2,3
print(a,b,c)
#a,b=1,2,3  ValueError: too many values to unpack (expected 2)
a,*b=1,2,3,4
print(a,b)
a,*b,c=1,2,3,4
print(a,b,c)
a,*b=[1,2,3,4]
print(a,b)
a,*b="hello"
print(a,b)

# iterating
fruits=('apple','banana','cherry')
for fruit in fruits:
    print(fruit)

#enumerate gives us tuple object
colors=('red','blue','green','yellow')
for index,color in enumerate(colors):
    print(index,color)

pairs=[(1,'a'),(2,'b'),(3,'c')]
for num,letter in pairs:
    print(num,letter)

# concatenation 
t1=(1,2,3,)
t2=(4,5)
result=t1+t2
print(result)
res=t1*0
print(res)
t4=(1,2,3)
t5=(1,2,4)
print(t1==t4)
print(t1==t5)
print(t1<=t5)

#membership check
print("green"not in colors)

#methods
print(t1.count(1))
print(t1.index(3))
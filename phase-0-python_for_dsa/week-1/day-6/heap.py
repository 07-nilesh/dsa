import heapq

# build min heap (heapify)
# TC : O(n), Space : O(1)

A =[-4,3,1,0,2,5,10,8,12,9]
heapq.heapify(A)  
print(A)

# Heap push (insert elemnts)
# TC : O(log n)
heapq.heappush(A,4)
print(A)

# Heap pop (extract min)
# TC : O(log n)
min=heapq.heappop(A)
print(A)
print(min)

# Heap Push Pop : Time : O(log n)
heapq.heappushpop(A,99)
print(A)

#peek at min : time O(1)
print(A[0])

# heap sort
# TC : O(nlog n),  Space: O(n)
# NOTE : O(1) space is possible via swapping, but this is complex
def heapsort(arr):
    heapq.heapify(arr)
    n=len(arr)
    new_list=[0]*n
    print(new_list)

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i]=minn
    return new_list
print(heapsort([-4,3,1,0,2,5,10,8,12,9]))

# Max heap
B=[-4,3,1,0,2,5,10,8,12,9]
n=len(B)
for i in range(n):
    B[i]=-B[i]
heapq.heapify(B)
print(B)
largest=-heapq.heappop(B)
print(largest)
heapq.heappush(B,-7)
print(B)

# Build heap from scratch - Time : O(nlogn)
C=[-4,3,1,0,2,5,10,8,12,9]
heap=[]
for x in C:
    heapq.heappush(heap,x)
    print(heap)

# K largest elements 
nums=[3, 1, 4, 1, 5, 9, 2, 6]
k=3
lar=heapq.nlargest(k,nums)
print(lar)
small=heapq.nsmallest(k,nums)
print(small)
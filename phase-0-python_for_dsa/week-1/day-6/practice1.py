import heapq

# ── 1. TUPLES IN HEAPS (Priority Queue Pattern) ──
pq = []

# Task format: (priority_level, task_name)
# Lower priority number = higher urgency
heapq.heappush(pq, (3, "Fix subtle bug"))
heapq.heappush(pq, (1, "Production server down!"))
heapq.heappush(pq, (3, "Attend team sync"))

# Pop elements — it sorts by priority first. 
# If priorities match, it sorts alphabetically by task name!
print(heapq.heappop(pq))  # (1, 'Production server down!')
print(heapq.heappop(pq))  # (3, 'Attend team sync') -> 'A' comes before 'F'
print(heapq.heappop(pq))  # (3, 'Fix subtle bug')


# ── 2. TUPLES AS SORTING KEYS ──
students = [
    ("Nilesh", 95),
    ("Amit", 95),
    ("Rahul", 88)
]

# Goal: Sort by score descending (highest first). If scores match, sort alphabetically.
# We return a tuple in the lambda key: (-score, name)
students.sort(key=lambda x: (-x[1], x[0]))
print(students)  # [('Amit', 95), ('Nilesh', 95), ('Rahul', 88)]

products = [("laptop", 1200), ("phone", 800), ("mouse", 25), ("keyboard", 25)]
sort_product=sorted(products,key=lambda x:(x[1],x[0]))
print(sort_product)
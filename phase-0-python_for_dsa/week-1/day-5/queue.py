#queue -FIFO
from collections import deque

print_jobs=deque()

# enqueue - add element to rightside -O(1)
print_jobs.append("resume.pdf")
print_jobs.append("Project.docx")
print_jobs.append("routine.txt")
print(print_jobs)
print_jobs.appendleft("todolist.txt")
print(print_jobs)
print(print_jobs[2])

#peek at first or left side -O(1  )
next_job=print_jobs[0]
print(next_job)

#peek at last 0r right side - O(1)
last_job=print_jobs[-1]
print(last_job)

#dequeue - remove from left -O(1)
processed_job = print_jobs.popleft()
print(print_jobs)
print(processed_job)
#remove from right
processed_job1 = print_jobs.pop()
print(print_jobs)
print(processed_job1)
# Queue — NEVER use list.pop(0) — it's O(n)!
# Use collections.deque for O(1) operations on both ends
print(type(print_jobs))
#deque also works as sliding window
dq =deque(maxlen=3)  # automatically drops oldest when full
dq.append(1)
print(dq)
dq.append(2)
print(dq)
dq.append(3)
print(dq)
dq.append(4) #-drops 1 automatically
print(dq)
print(dq[2])


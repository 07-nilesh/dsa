# stack - LIFO
browser_history=[]

# append to top of stack -O(1)
browser_history.append("google.com")
browser_history.append("github.com")
browser_history.append("notion.so")
print(browser_history)

# peek on top of stack - O(1)
top_page=browser_history[-1]
print(top_page)

#pop from stack - O(1)
last_visited=browser_history.pop()
print(last_visited)

#ask if something is in stack - O(1)
if browser_history:
    print("True")

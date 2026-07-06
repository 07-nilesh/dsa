browser_history=[]
# append
browser_history.append("google.com")
browser_history.append("github.com")
browser_history.append("notion.so")
print(browser_history)

# peek
top_page=browser_history[-1]
print(top_page)

#pop
last_visited=browser_history.pop()
print(last_visited)

#Isempty
if browser_history:
    print("True")
    
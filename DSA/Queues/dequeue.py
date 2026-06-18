from collections import deque
q=deque()
q.append(10)
q.append(20)
q.append(30)
q.appendleft(5)
x=q.pop()
y=q.popleft()

print(q)
print(x)
print(y)

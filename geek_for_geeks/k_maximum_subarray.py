from collections import deque
k=3
arr = [1,2,3,1, 4, 5, 2, 3, 6]
max_arr=[]
dq=deque()
for  i in range(len(arr)):
    if dq and dq[0]==i-k:
        dq.popleft()
    while dq and arr[dq[-1]]<arr[i]:
        dq.pop()
    dq.append(i)
    if i>=k-1:
        max_arr.append(arr[dq[0]])
print(max_arr)
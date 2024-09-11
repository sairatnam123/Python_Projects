# Enter your code here. Read input from STDIN. Print output to STDOUT
N= int (input())
l=[]
for i in range(N):
  l.append(input())
k=int(input())

distinct_array=[]
index=0
for i in range(N):
  if l.count(l[i])<2:
    distinct_array.append(l[i])
    index=index+1
if len(distinct_array) >= k:
  print(distinct_array[k-1])
else:
  print('')
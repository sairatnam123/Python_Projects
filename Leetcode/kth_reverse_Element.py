
n=int(input())
k=int(input())

s=""
for i in range(n):
  char=input()
  s=s+char

reverse=""
for i in range(n-1,-1,-1):
    reverse=reverse+s[i]

print(reverse[k-1])

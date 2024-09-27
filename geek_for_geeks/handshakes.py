#User function Template for python3
import math

def combinations(n,k):
    return math.factorial(n)//(math.factorial(k)*math.factorial(n-k))

def catalog_numbers(n):
    return combinations(2*n,n)//(n+1)

def count1(N):
    # code here
    if N%2!=0 :
        return 0
    n=N//2
    return catalog_numbers(n)

N=6
print(count1(N))
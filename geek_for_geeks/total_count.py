"""You are given an array arr[] of positive integers and a threshold value k.
For each element in the array, divide it into the minimum number of small integers such that each divided integer is less than or equal to k.
Compute the total number of these integer across all elements of the array.

Examples:

Input: k = 3, arr[] = [5, 8, 10, 13]
Output: 14
Explanation: Each number can be expressed as sum of different numbers less than or
equal to k as 5 (3 + 2), 8 (3 + 3 + 2), 10 (3 + 3 + 3 + 1), 13 (3 + 3 + 3 + 3 + 1).
So, the sum of count of each element is (2+3+4+5)=14."""
def totalCount( k, arr):
    # code here
    total_count = 0
    for i in range(len(arr)):
        total_count += arr[i] // k
        if arr[i] % k != 0:
            total_count += 1
    return total_count
array= [5, 8, 10, 13]
k1 = 3
print(totalCount(k=k1,arr=array))

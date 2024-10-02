def minimizeCost(arr,k):
    # code her
    dp = [float('inf')] * len(arr)
    dp[0] = 0
    for i in range(1, len(arr)):
        for j in range(max(0, i - k), i):
            dp[i] = min(dp[i], dp[j] + abs(arr[i] - arr[j]))
    return dp[-1]

array=[10,20,40,50,30]
step=3
print(minimizeCost(arr=array,k=step))
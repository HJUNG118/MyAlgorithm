n = int(input())
dp = [0]*(3*n)
arr = [0]*(3*n)
for i in range(n):
    arr[i] = int(input())

dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[0]+arr[2], dp[1], arr[1]+arr[2])
for i in range(3, n):
    dp[i] = max(arr[i]+dp[i-2], arr[i]+arr[i-1]+dp[i-3], dp[i-1])
print(dp[n-1])
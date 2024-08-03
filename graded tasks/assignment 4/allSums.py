def allSumsDP(arr):
    if not arr:
        return {0}

    max_sum = sum(arr)
    dp = [set() for _ in range(len(arr) + 1)]
    dp[0] = {0}

    for i in range(1, len(arr) + 1):
        for s in range(max_sum, -1, -1):
            if s in dp[i - 1] or (s - arr[i - 1] >= 0 and s - arr[i - 1] in dp[i - 1]):
                dp[i].add(s)

    return dp[-1]
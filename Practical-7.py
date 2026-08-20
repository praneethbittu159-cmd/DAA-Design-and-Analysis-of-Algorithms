def coin_change(coins, amount):
    # dp[i] = minimum coins needed to make amount i
    dp = [float('inf')] * (amount + 1)

    # 0 coins are needed to make amount 0
    dp[0] = 0

    # Calculate minimum coins for every amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If amount cannot be made
    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


coins = [1, 2, 5]
amount = 11

print("Minimum coins required:", coin_change(coins, amount))
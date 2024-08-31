def coin_change(coins, amount):

    # initialize dp array with amount+1 values, all set to infinity
    dp = [float("inf")] * (amount + 1)

    # Base case: 0 coins are needed to make the amount 0
    dp[0] = 0  # dp[coin_value] = no. of coins needed

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


coins = [1, 2, 5]  # each value represents value of the coin
amount = 11
print(
    coin_change(coins, amount)
)  # output: 3(11 = 5+5+1). Two coins of 5 and one coin of 1

"""
Problem: Coin Change (Dynamic Programming)
You are given an array coins representing coin denominations and an integer amount representing a target amount of money. Your goal is to determine the minimum number of coins needed to make up that amount. If the amount cannot be made up by any combination of the given coins, return -1.

Explanation:
Initialize the DP array:

We initialize dp[0] = 0 since no coins are needed to form 0.
All other values in the dp array are set to infinity initially (float('inf')), indicating that they are unreachable.
Build the DP Table:

For each coin in the coins array, we iterate from the value of that coin up to amount. We update the dp[i] value by checking if including the current coin reduces the number of coins needed.
Transition:

If we use the coin coin, we add 1 to dp[i - coin] because we're adding one more coin to the subproblem that solves for i - coin. We choose the minimum of the current value of dp[i] and dp[i - coin] + 1.
Return Result:

After processing, if dp[amount] is still infinity, it means the amount cannot be formed with the given coins, so we return -1. Otherwise, we return the value of dp[amount], which represents the minimum number of coins needed.
"""

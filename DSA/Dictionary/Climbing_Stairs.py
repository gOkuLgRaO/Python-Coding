class Solution:
    """
    The memoization solution improves the recursive solution by introducing memoization, which avoids
    redundant calculations. We use an unordered map (memo) to store the already computed results for each step n.
    Before making a recursive call, we check if the result for the given n exists in the memo. If it does, we
    return the stored value; otherwise, we compute the result recursively and store it in the memo for future reference.
    """

    def stairs(self, n: int) -> int:
        memo = {}
        return self.stair_counter(n, memo)

    def stair_counter(self, n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.stair_counter(n - 1, memo) + self.stair_counter(n - 2, memo)

        return memo[n]


if __name__ == "__main__":
    nums = int(input("Enter the number of stairs"))
    solution = Solution()
    print(solution.stairs(nums))

"""
To calculate the number of ways to climb the stairs, we can observe that when we are on the nth stair,
we have two options:

either we climbed one stair from the (n-1)th stair or
we climbed two stairs from the (n-2)th stair.
By leveraging this observation, we can break down the problem into smaller sub problems and apply the concept of 
the Fibonacci series.
The base cases are when we are on the 1st stair (only one way to reach it) and the 2nd stair (two ways to reach it).
By summing up the number of ways to reach the (n-1)th and (n-2)th stairs, we can compute the total number of 
ways to climb the stairs. This allows us to solve the problem efficiently using various dynamic programming techniques
such as recursion, memoization, tabulation, or space optimization.
"""

class Solution:
    @staticmethod
    def stock(prices):
        left = 0  # buy
        right = 1  # sell
        max_profit = 0

        while right < len(prices):
            curr_profit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(curr_profit, max_profit)
            else:
                left = right
            right += 1
        return max_profit


if __name__ == "__main__":
    solution = Solution()
    nums = list(map(int, input("Enter the prices of the stock each day").split()))
    print(Solution.stock(nums))

"""
Find the best time to buy and sell stock for maximum profit. 
"""

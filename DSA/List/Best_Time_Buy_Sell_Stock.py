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

    @staticmethod
    def stock2(prices):
        current_sum = 0
        max_sum = 0
        for i in range(1, len(prices)):
            current_sum = max(current_sum, current_sum + prices[i])
            max_sum = max(current_sum, max_sum)

        return max_sum


if __name__ == "__main__":
    solution = Solution()
    nums = list(map(int, input("Enter the prices of the stock each day").split()))
    print(Solution.stock(nums))
    print(Solution.stock2(nums))

"""
Find the best time to buy and sell stock for maximum profit. 
"""

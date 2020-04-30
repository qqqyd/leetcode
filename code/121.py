"""
121. 买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。
示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

我的思想：
记录到目前为止的最大利润

优解思想：
思想相同，减少条件判断

收获：

"""

def solution(prices):
    # prices: List[int]
    low = float('INF')
    profit = 0
    for price in prices:
        if price < low:
            low = price
        else:
            profit = max(high-low, profit) 
    return profit
    
def excellent(prices):
    # prices: List[int]
    low = float('INF')
    profit = 0
    for price in prices:
        profit = max(price-low, profit) 
        low = min(price, low)
    return profit

if __name__ == '__main__':
    prices = []
    print(solution(prices))

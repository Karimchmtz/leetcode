class Solution:
    def finalPrices(self, prices):
        
        def findJ(prices: list, index):
            if index >= len(prices) - 1:
                return -1
            itemPrice = prices[index]
            for i in range(index + 1, len(prices)):
                if prices[i] <= itemPrice:
                    return i
            return -1

        res = []
        i = 0
        for elm in prices:
            j = findJ(prices, i)
            if j != -1:
                res.append(elm - prices[j])
            else:
                res.append(elm)
            i += 1
        return res
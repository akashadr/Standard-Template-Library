def maxProfit(price, start, end):
 

    if (end == start):

        return 0;


    profit = 0;

    for i in range(start, end):
        j=i+1
 
        if(price[j] > price[i]):

            profit += (price[j] - price[i])

    return profit
 

if __name__ == '__main__':

    price = [7,1,5,3,6,4]

    n = len(price)
 

    print(maxProfit(price, 0, n - 1))

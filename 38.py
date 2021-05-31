def minimumCost(cost, n):
 

    step1 = 0

    step2 = 0
 

    for i in range(n):

        step0 = cost[i] + min(step1, step2)
 
        step2 = step1

        step1 = step0

    return min(step1, step2)
 

if __name__ == "__main__":

    a = [1,100,1,1,1,100,1,1,100,1]

    n = len(a)

    print(minimumCost(a, n))
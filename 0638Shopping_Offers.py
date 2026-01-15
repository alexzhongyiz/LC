import functools
def shoppingOffers(price, special, needs):
    n = len(price)
    maxprice = sum([price[i]*needs[i] for i in range(n)])
    @functools.lru_cache()
    def dfs(currneed):
        # for i in range(len(currneed)):
        #     if currneed[i]< 0:
        if any(need < 0 for need in currneed):
            return maxprice
        if sum(currneed) ==0:
            return 0
        tmp = sum(price[i]*list(currneed)[i] for i in range(n))
        
        for j in range(len(special)):
            new_need = list(currneed)
            specialprice = special[j][-1]
            for k in range(n):
                new_need[k] -= special[j][k]
            tmp = min(tmp,specialprice+dfs(tuple(new_need)))
        return tmp
    return dfs(tuple(needs))

    
print(shoppingOffers([2,5],[[3,0,5],[1,2,10]],[3,2]))
print(shoppingOffers([2,3,4],[[1,1,0,4],[2,2,1,9]],[1,2,1]))
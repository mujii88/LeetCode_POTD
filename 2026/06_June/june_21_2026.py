# Problems Name:
            # 1833. Maximum Ice Cream Bars

# Python Implementation


class Solution:
    def maxIceCream(self, costs, coins: int) -> int:
        costs.sort()
        count=0
        i=0
        while i<len(costs) and  costs[i]<=coins:
            count+=1
            coins-=costs[i]
            i+=1

        return count        




# c++ implementation

class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        sort(costs.begin(),costs.end());
        int count=0;
        for (int i:costs){
            if (i<=coins){
                coins-=i ;
                count+=1;
            }

        }
        return count;
        
    }
};
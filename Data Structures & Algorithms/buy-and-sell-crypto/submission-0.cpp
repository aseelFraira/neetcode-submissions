class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price = prices[0];
        int n = prices.size();
        int right = 0;
        int max_profit = 0;
        while(right < n){
            int profit = prices[right] - min_price;
            if(profit > max_profit) max_profit = profit;
            if(prices[right] < min_price){
                min_price = prices[right];
            }
            right++;
        }
        return max_profit;
        
    }
};

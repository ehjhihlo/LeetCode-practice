class Solution {
public:
    int arrangeCoins(int n) {
        long long first= 1;
        long long last = n+1LL;
        while(first<last){
            long long k = (first+last)/2;
            long long r = k*(1+k)/2;
            if(r>n){
                last = k;
            }
            else{
                first = k+1;
            }
        }
        return first-1;
    }
};

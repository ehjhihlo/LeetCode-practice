int maxSubArray(int* nums, int numsSize){
    int sum = 0;
    int maxsum = -10000;
    for(int i=0;i<numsSize;i++){
        if(sum>0){
            sum += nums[i];
        }
        else{
            sum = nums[i];
        }
        if(sum > maxsum){
            maxsum = sum;
        }
    }
    return maxsum;
}

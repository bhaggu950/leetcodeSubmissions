class Solution {
    public int maxSubArray(int[] nums) {
        int max=nums[0], temp;
        int i,j;
        for(i=0;i<nums.length;i++)
        {
            temp=0;
            for(j=i;j<nums.length;j++)
            {
                temp=temp+nums[j];
                if(temp>max)
                {
                    max=temp;
                }
            }   
        }
        return max;
    }
}

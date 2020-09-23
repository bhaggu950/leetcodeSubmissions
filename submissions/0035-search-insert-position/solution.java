class Solution {
    public int searchInsert(int[] nums, int target) {
        int pos=0;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]==target)
            {
                pos=i;
                break;
            }
            else if(nums[i]>target)
            {
                pos=i;
                break;
            }
            else
            {
                
            }
            if(i==nums.length-1)
            {
                pos=i+1;
            }
        }
        return pos;
    }
}

class Solution {
    public int removeElement(int[] nums, int val) {
        int in_len=nums.length, out_len=0, i=0;
        for(int j=0;j<in_len;j++)
        {
            if(nums[j]!=val)
            {
                nums[i]=nums[j];
                i++;
                out_len++;
            }
        }
        return out_len;
    }
}

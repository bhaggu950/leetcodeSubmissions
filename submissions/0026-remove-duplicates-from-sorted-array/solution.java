class Solution {
    public int removeDuplicates(int[] nums) {
        int i=0, j, max=0, in_len=nums.length, out_len=0;
        max=(in_len==0)?0:nums[in_len-1];
        if(max<0)
        {
            max=0;
        }
        int min = (in_len==0)?0:nums[0];
        if(min>0)
        {
            min=0;
        }
        int stat_plus[] = new int[max+1];
        int stat_minus[] = new int[Math.abs(min)+1];
        for(j=0;j<in_len;j++)
        {
            if(nums[j]>=0)
            {
                if(stat_plus[nums[j]]==0)
                {
                    stat_plus[nums[j]]=1;
                    nums[i]=nums[j];
                    out_len++;
                    i++;
                }
                else
                {
                    
                }
            }
            else
            {
                if(stat_minus[Math.abs(nums[j])]==0)
                {
                    stat_minus[Math.abs(nums[j])]=1;
                    nums[i]=nums[j];
                    out_len++;
                    i++;
                }
                else
                {
                    
                }
            }
        }
        return out_len;
    }
}

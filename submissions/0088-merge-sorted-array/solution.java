class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i, j;
        for(i=0;i<n;i++)
        {
            nums1[i+m]=nums2[i];
        }
        for(i=0;i<m+n;i++)
        {
            for(j=i;j<m+n;j++)
            {
                if(nums1[j]<nums1[i])
                {
                    int temp=nums1[i];
                    nums1[i]=nums1[j];
                    nums1[j]=temp;
                }
            }
        }
    }
}

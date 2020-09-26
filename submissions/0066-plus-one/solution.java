class Solution {
    public int[] plusOne(int[] digits) {
        int len = digits.length;
        int carry=1, i, j;
        int rev[] = new int[len+1];
        for(i=len-1,j=0;i>=0 && j<len;i--,j++)
        {
            if(carry==1)
            {
                rev[j]=(digits[i]+carry)%10;
                carry=(digits[i]+carry)/10;
            }
            else
            {
                rev[j]=digits[i];
                carry=0;
            }            
        }
        if(j==len && carry==1)
        {
            rev[j]=1;
        }
        else
        {
            rev[j]=0;
        }
        int rev_len=rev.length;
        int ans[] = new int[rev[rev_len-1]==0?len:rev_len];
        if(rev[rev_len-1]==0)
        {
            for(i=len-1,j=0;i>=0 && j<len; i--,j++)
            {
                ans[j]=rev[i];
            }
        }
        else
        {
            for(i=rev_len-1,j=0;i>=0 && j<rev_len-1; i--,j++)
            {
                ans[j]=rev[i];
            }
        }
        return ans;
    }
}

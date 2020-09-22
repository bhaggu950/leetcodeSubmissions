class Solution {
    public int strStr(String haystack, String needle) {
        if(needle.length()==0)
        {
            return 0;
        }
        int pos=-1, n_len=needle.length(), h_len=haystack.length(), j=0, count=0;
        for(int i=0;i<=h_len-n_len;i++)
        {
            count=0;
            for(j=0;j<n_len;j++)
            {
                if(needle.charAt(j)==haystack.charAt(i+j))
                {
                    count++;
                    if(count==n_len)
                    {
                        pos=i;
                        return pos;
                    }
                }
            }
        }
        return pos;
    }
}

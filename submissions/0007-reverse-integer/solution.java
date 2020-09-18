class Solution {
public int reverse(int x) {
    int ans=0, temp=x, rem;
    while(temp!=0)
    {
        rem=temp%10;
        temp/=10;
        if(ans > Integer.MAX_VALUE/10 || (ans == Integer.MAX_VALUE/10 && rem>7))
            return 0;
        if(ans < Integer.MIN_VALUE/10 || (ans == Integer.MIN_VALUE/10 && rem<-8))
            return 0;
        ans=ans*10+rem;
        
    }
    return ans;
    }
};

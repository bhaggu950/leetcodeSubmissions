class Solution {
    public boolean isPalindrome(int x) {
        int rem, ans=0, temp=x;
        while(temp!=0)
        {
            rem=temp%10;
            temp/=10;
            ans=ans*10+rem;
        }
        if(ans==Math.abs(x))
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}

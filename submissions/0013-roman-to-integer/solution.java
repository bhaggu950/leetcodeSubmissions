class Solution {
    public int romanToInt(String s) {
        int ans=0, temp=0;
        for(int i=0; i<s.length(); i++)
        {
            if(s.charAt(i)=='I')
            {
                ans+=1;
                temp=1;
            }
            else if(s.charAt(i)=='V')
            {
                if(i!=0&&s.charAt(i-1)=='I')
                {
                    ans+=3;
                }
                else
                {
                    ans+=5;
                }
                temp=0;
            }
            else if(s.charAt(i)=='X')
            {
                if(i!=0&&s.charAt(i-1)=='I')
                {
                    ans+=8;
                    temp=0;
                }
                else
                {
                    ans+=10;
                    temp=2;
                }
            }
            else if(s.charAt(i)=='L')
            {
                if(i!=0&&s.charAt(i-1)=='X')
                {
                    ans+=30;
                    temp=0;
                }
                else
                {
                    ans+=50;
                    temp=0;
                }
            }
            else if(s.charAt(i)=='C')
            {
                if(i!=0&&s.charAt(i-1)=='X')
                {
                    ans+=80;
                    temp=0;
                }
                else
                {
                    ans+=100;
                    temp=3;
                }
            }
            else if(s.charAt(i)=='D')
            {
                if(i!=0&&s.charAt(i-1)=='C')
                {
                    ans+=300;
                    temp=0;
                }
                else
                {
                    ans+=500;
                    temp=0;
                }
            }
            else if(s.charAt(i)=='M')
            {
                if(i!=0&&s.charAt(i-1)=='C')
                {
                    ans+=800;
                    temp=0;
                }
                else
                {
                    ans+=1000;
                    temp=0;
                }
            }
            else
            {
                
            }
        }
        return ans;
    }
}

class Solution {
    public boolean isValid(String s) {
        int sym[] = new int[s.length()];
        int temp1=0, temp2=0, temp3=0, i=0;
        for(int j=0;j<s.length();j++)
        {
            char c=s.charAt(j);
            if(c=='(')
            {
                temp1++;
                sym[i++]=1;
            }
            else if(c=='[')
            {
                temp2++;
                sym[i++]=2;
            }
            else if(c=='{')
            {
                temp3++;
                sym[i++]=3;
            }
            else if(c==')')
            {
                if(i!=0 && sym[i-1]==1)
                {
                    temp1--;
                    i--;
                }
                else
                {
                    return false;
                }
            }
            else if(c==']')
            {
                if(i!=0 && sym[i-1]==2)
                {
                    temp2--;
                    i--;
                }
                else
                {
                    return false;
                }
            }
            else if(c=='}')
            {
                if(i!=0 && sym[i-1]==3)
                {
                    temp3--;
                    i--;
                }
                else
                {
                    return false;
                }
            }
            else
            {
                
            }
        }
        if(temp1==0 && temp2==0 && temp3==0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}

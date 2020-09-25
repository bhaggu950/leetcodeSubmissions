class Solution {
    public int lengthOfLastWord(String s) {
        int length=0;
        char blank=' ';
        for(int i=0;i<s.length();i++)
        {
            char c=s.charAt(i);
            if(c!=blank)
            {
                length++;
            }
            else if(c==blank && i+1 != s.length() && s.charAt(i+1) != blank)
            {
                length=0;
            }
            else
            {
                
            }
        }
        return length;
    }
}

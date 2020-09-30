/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        int min = (head == null)?0:head.val, max=0, x;
        ListNode dummy = new ListNode(0);
        ListNode curr=head, ans=dummy;
        while(curr!=null)
        {
            max=curr.val;
            curr=curr.next;
        }
        int neg[] = new int[Math.abs(min)+1];
        int pos[] = new int[Math.abs(max)+1];
        curr=head;
        while(curr!=null)
        {
            x=curr.val;
            if(x<0)
            {
                if(neg[Math.abs(x)]==0)
                {
                    ans.next=new ListNode(x);
                    ans=ans.next;
                    neg[Math.abs(x)]=1;
                }
            }
            else
            {
                if(pos[x]==0)
                {
                    ans.next=new ListNode(x);
                    ans=ans.next;
                    pos[x]=1;
                }
            }
            curr=curr.next;
        }
        return dummy.next;
    }
}

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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode p=l1, q=l2, curr=dummy;
        while(p!=null && q!=null)
        {
            int x = (p.val<=q.val)?p.val:q.val;
            curr.next=new ListNode(x);
            curr = curr.next;
            if(x==p.val)
            {
                p=p.next;
            }
            else
            {
                q=q.next;
            }
        }
        if(p==null)
        {
            while(q!=null)
            {
                curr.next=new ListNode(q.val);
                curr=curr.next;
                q=q.next;
            }
            return dummy.next;
        }
        if(q==null)
        {
            while(p!=null)
            {
                curr.next=new ListNode(p.val);
                curr=curr.next;
                p=p.next;
            }
            return dummy.next;
        }
        return dummy.next;
    }
}

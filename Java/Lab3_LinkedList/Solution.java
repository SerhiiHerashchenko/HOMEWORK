package Lab3_LinkedList;

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode temp1 = list1;
        ListNode temp2 = list2;
    
        final ListNode newList = new ListNode();
        ListNode head = newList;
        final ListNode ans = newList;
        
        if (temp1.val != -101 && temp2.val != -101) {
            while(temp1 != null && temp2 != null){
                if(temp1.val < temp2.val){
                    final ListNode newNode = new ListNode(temp1.val);
                    head.next = newNode;
                    head = head.next;
                    temp1 = temp1.next;
                }
                else{
                    final ListNode newNode = new ListNode(temp2.val);
                    head.next = newNode;
                    head = head.next;
                    temp2 = temp2.next;
                }
            }
        }
        while(temp1 != null && temp1.val != -101){
            final ListNode newNode = new ListNode(temp1.val);
            head.next = newNode;
            head = head.next;
            temp1 = temp1.next;
        }
        while(temp2 != null && temp2.val != -101){
            final ListNode newNode = new ListNode(temp2.val);
            head.next = newNode;
            head = head.next;
            temp2 = temp2.next;
        }
        if (list1.val == -101 && list2.val == -101) {
            return temp1;
        }
        head = ans.next;
        return head;
    }
}

package Lab3_LinkedList;

class ListNode {
    int val = -101;
    ListNode next;
    ListNode(){}
    ListNode(int val){
        this.val = val;
        this.next = null;
    }
    ListNode(int val, ListNode next){
        this.val = val;
        this.next = next;
    }

    @Override
    public String toString() {
        if (this.val == -101) {
            return "[]";
        }

        ListNode head = this;
        String returnString = "[";
        while(head.next != null){
            returnString += head.val +",";
            head = head.next;
        }
        returnString += head.val +"]";
        return returnString;
    }
}

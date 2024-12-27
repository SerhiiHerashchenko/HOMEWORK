package Lab3_LinkedList;

public class MainClass {
    public static void main(String[] args) {
        //Example 1
        System.out.print("Ex 1:");
        ListNode head1 = new ListNode(1);
        head1.next = new ListNode(2);
        head1.next.next = new ListNode(4);

        ListNode head2 = new ListNode(1);
        head2.next = new ListNode(3);
        head2.next.next = new ListNode(4);

        ListNode answer = new Solution().mergeTwoLists(head1, head2);
        System.out.println(answer.toString());

        //Example 2
        System.out.print("Ex 2:");

        head1 = new ListNode();
        head2 = new ListNode();

        answer = new Solution().mergeTwoLists(head1, head2);
        System.out.println(answer.toString());

        //Example 3
        System.out.print("Ex 3:");

        head1 = new ListNode(0);
        head2 = new ListNode();

        answer = new Solution().mergeTwoLists(head1, head2);
        System.out.println(answer);
    }
}

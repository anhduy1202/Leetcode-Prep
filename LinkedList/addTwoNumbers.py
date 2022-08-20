from ListNode import ListNode

def addTwoNumbers(l1,l2):
    dummy = ListNode()
    curr = dummy
    carry = 0 
    while l1 or l2:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0

        new_val = l1_val + l2_val + carry
        carry = new_val // 10
        new_val = new_val % 10

        curr.next = ListNode(val=new_val)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    if carry:
        curr.next = ListNode(val=carry)
    return dummy.next

Node3 = ListNode(val=3)
Node4 = ListNode(val=4)
Node4_1 = ListNode(val=4,next=Node3)
Node2 = ListNode(val=2,next=Node4_1)
Node6 = ListNode(val=6,next=Node4)
Node5 = ListNode(val=5,next=Node6)
print(addTwoNumbers(Node2,Node5))
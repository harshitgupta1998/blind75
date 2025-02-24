### 141. Linked List Cycle
Walkthrough
###
1. We can solve this problem using set or fast/slow pointer 
2. Check with set if the value is present else return False i.e TC -  O(N) SC - O(N)
3.  We can use slow and fast pointer and slow will eventually catch up with fast pointer i.e TC -  O(N) SC - O(1)
```
  ### Slow and fast
      def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
  ###  USing set
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        set1=set()
        curr=head
        while curr:
            if curr.val in set1:
                return True
            else:
                set1.add(curr.val)
                curr=curr.next
        return False
        
```
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```
Example 2:
```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```
Example 3:
```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

Constraints:

- The number of the nodes in the list is in the range [0, 104].
- -105 <= Node.val <= 105
- pos is -1 or a valid index in the linked-list.

*Follow up*: Can you solve it using O(1) (i.e. constant) memory?

<details>
  <summary><h3>Show Hint 1</h3></summary>
  <p>Use the two pointer approach, but in a slightly different way. Study about fast pointer and slow pointer concept and implement it.</p>
</details>

---
<details>
  <summary><h3>Pseudocode</h3></summary>
  <pre>
    ListNode slow = head
    ListNode fast = head
    while fast not equal null and fast.next not equal null
      slow -> slow.next
      fast -> fast.next.next
      if slow equals fast
        return true
    return false
  </pre>
</details>

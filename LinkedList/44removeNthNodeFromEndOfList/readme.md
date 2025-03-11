### 19. Remove Nth Node from End of List

WalkThrough:
1. Take a value n and store the length of the node in first iteration
2. Using second itercation if n==len then head.next or iterate and return cur.next==cur.next.next, two pass O(N)
3. We can double pointer from same side for one iteration
```
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        N=0
        while cur:
            cur=cur.next
            N+=1
        
        removeindex=N-n
        if removeindex==0:
            return head.next
        i=0
        cur=head
        for i in range(N-1):
            if i+1==removeindex:
                cur.next=cur.next.next
                break
            cur=cur.next
        return head
OR
        def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
          dummy=ListNode(0,head)
          left=dummy
          right=head
          while n>0:
              right=right.next
              n-=1
          while right:
              left=left.next
              right=right.next
          left.next=left.next.next
          return dummy.next


```

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```
Example 2:
```
Input: head = [1], n = 1
Output: []
```
Example 3:
```
Input: head = [1,2], n = 1
Output: [1]
```

Constraints:

- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

*Follow up*: Could you do this in one pass?

<details>
  <summary><h3>Show Hint 1</h3></summary>
  <p>The same two pointer technique also keep track of length of nodes.</p>
</details>

---
<details>
  <summary><h3>Pseudocode</h3></summary>
  <pre>
    dummy -> ListNode()
    l -> dummy
    r -> head
    while n greaterThan 0 and r not equal null
      r -> r.next
      n -> n - 1
    while r not equal null
      l -> l.next
      r -> r.next
    l.next -> l.next.next
    return dummy.next
  </pre>
</details>

### 206. Reverse Linked List
Walkthrough
###
1. Recursion i.e TC -  O(N) SC - TC O(N)
2. We can iterative check the variable for curr, prev and use it to flip the pointer i.e TC -  O(N) SC - O(1) Space Optimised

```

  ### Iterative
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative
        prev,curr=None, head
        while curr:
            temp=curr.next
            curr.next=prev
            curr=temp
        return prev

####
  Recursion
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: # Basecase
            return None
        newhead=head # save the head in a temp 
        if head.next: 
            newhead=self.reverseList(head.next) # call function recursive on head.next
            head.next.next=head # reverse the pointer 
        head.next=None # mark the last pointer as None
        return newhead

```

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```
Example 2:
```
Input: head = [1,2]
Output: [2,1]
```
Example 3:
```
Input: head = []
Output: []
```

Constraints:

- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

*Follow up*: A linked list can be reversed either iteratively or recursively. Could you implement both?

<details>
  <summary><h3>Show Hint 1</h3></summary>
  <p>Just break the link and shift the pointers in loop, prev, curr, nxt makes nxt equals to curr's next and curr's next points to prev now prev equals curr curr equals nxt. If recursion makes the head next's points to the head and makes head's next to none.</p>
</details>

---
<details>
  <summary><h3>Pseudocode</h3></summary>
  <pre>
    loop :
      prev -> none, curr -> head
      while curr
        nxt -> curr.next
        curr.next -> prev
        prev -> curr
        curr -> nxt
      return prev
    recursion :
      if head is null or head.next is null then return head
      node -> recurse(head.next)
      head.next.next -> head
      head.next -> none
      return node
  </pre>
</details>

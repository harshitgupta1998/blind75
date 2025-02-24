### 21. Merge Two Sorted Lists



Walkthrough
###
1. We can solve this problem using recursion or iteration 
2. For recursion we have to understand the base case first for both node list1 and list2 and the recursive call the function TC -  O(N+M) SC - O(N+M)
3. For iteration we can create a dummy node and dummy pointer and check based on while condition until all elments are added and then add the remaining i.e TC -  O(N+M) SC - O(1)

```
  ### Recusrsion
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      # Check the base case
        if list1 is None:
            return list2
        if list2 is None:
            return list1
    # Check the condition for list1 and list2
  ''' The current node in list1 is smaller (or equal), so it becomes part of the merged list.
The function recursively merges the remaining part of list1 (list1.next) with the entire list2 by calling self.mergeTwoLists(list1.next, list2).
Once the recursion completes, the node from list1 will point to the merged result.'''
        if list1.val<=list2.val:
            list1.next=self.mergeTwoLists(list1.next,list2)
            return list1
        
        else:
            list2.next=self.mergeTwoLists(list1,list2.next)
            return list2


    ### Iteration
        # Intialize the pointer and header
        dummy=node=ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                # attach the list 1 to the node 
                node.next=list1
                list1=list1.next
            else:
                node.next=list2
                list2=list2.next
            # update the node to point to next 
            node=node.next
        # append the remaining 
        node.next=list1 or list2

        return dummy.next
        
```


You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```
Example 2:
```
Input: list1 = [], list2 = []
Output: []
```
Example 3:
```
Input: list1 = [], list2 = [0]
Output: [0]
```

Constraints:

- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

<details>
  <summary><h3>Show Hint 1</h3></summary>
  <p>Use the merge sort approach create an empty node and make the next smallest element.</p>
</details>

---
<details>
  <summary><h3>Pseudocode</h3></summary>
  <pre>
    dummy -> ListNode()
    tail -> dummy
    while l1 not equals null and l2 not equals null
      if l1.val isLessThan l2.val
        tail.next -> l1
        l1 -> l1.next
      else
        tail.next -> l2
        l2 -> l2.next
    if l1 not equals null
      tail.next -> l1
    else if l2 not equals null
      tail.next -> l2
    return dummy.next
  </pre>
</details>

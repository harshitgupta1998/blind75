### 226. Invert Binary Tree (Easy)
Walkthrough
###
1.Trees always think if we can use BFS or DFS more efficiently (Always check the base case if root exist)
2. Here, we can use DFS amd recursively call the function on left and right  i.e TC -  O(N) SC - O(N)
3. BFS we can maintain a queue and append root then pop the left element anc append the left and right of that node until empty  i.e TC -  O(N) SC - O(N)

```
  ### DFS we check the left and right if the root exist
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left,root.right=root.right,root.left
      # Recursively call the function on left and right
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

### BFS we can check the queue
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue=deque([root])
        while queue:
            # Will take the value root first
            node=queue.popleft()
            node.left,node.right=node.right,node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # Return root as we are updating in place
        return root
```
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```
Example 2:
```
Input: root = [2,1,3]
Output: [2,3,1]
```
Example 3:
```
Input: root = []
Output: []
```

Constraints:

- The number of nodes in the tree is in the range (0, 100).
- -100 <= Node.val <= 100

<details>
  <summary><h3>Show Hint 1</h3></summary>
  <p>Traverse tree swap the left node with right by setting the current left to current right and its vice versa and finally return the root node.</p>
</details>

---
<details>
  <summary><h3>Pseudocode</h3></summary>
  <pre>
    if root equals null
      return null
    left -> root.left
    right -> root.right
    root.left -> invertTree(right)
    root.right -> invertTree(left)
    return root
  </pre>
</details>

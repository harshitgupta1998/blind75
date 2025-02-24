### 104. Maximum Depth Binary Tree (Easy)
Walkthrough 
1. We can use recursive DFS and add 1 for each iteration TC -> O(N) SC-> O(height)
2. We can use BFS we can use a deque and popleft before appending the values and increment the level accordingly TC -> O(N) SC-> O(N)

```
# DFS Recursively
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
# BFS
      def maxDepth(self, root: Optional[TreeNode]) -> int:
      # mainitain a deque
        queue=deque()
        if not root:
            return 0
        else:
            # start by appending the root
            queue.append(root)
        
        level=0
      # each while loop will update the level
        while queue:
          # check all the elements in the queue 
            for i in range(len(queue)):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return level
```
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```
Example 2:
```
Input: root = [1,null,2]
Output: 2
```

Constraints:

- The number of nodes in the tree is in the range 0 - 10^4.
- -100 <= Node.val <= 100

<details>
  <summary><h3>Show Hint 1</h3></summary>
  <p>Just like tree traversal and just return the maximum of left and right tree + 1 at the end.</p>
</details>

---
<details>
  <summary><h3>Pseudocode</h3></summary>
  <pre>
    maxDepth(node)
      if root is null then return 0
      maxLeft -> maxDepth(node.left)
      maxRight -> maxDepth(node.right)
      return maximum(maxLeft, maxRight) + 1
  </pre>
</details>

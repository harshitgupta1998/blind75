# [30](https://leetcode.com/problems/number-of-islands/) Number of Islands
WalkThrough:
1. Define the rows, cols, base case, visit set to intial based on question.
2. Then iteratively call the dfs or bfs function on all valid position
3. mainitain the values and stop when stopping condition is reached

```
    # bfs we can use popleft and dfs we can use pop
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        islands=0
        dirc=[[0,1],[1,0],[0,-1],[-1,0]]
        visit=set()
       
        def bfs(r,c):
            queue=collections.deque()
            visit.add((r,c))
            queue.append((r,c))
            while queue:
                r,c=queue.popleft()
                for dr,dc in dirc:
                    nr,nc=r+dr,c+dc
                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visit and grid[r][c]=="1":
                        queue.append((nr,nc))
                        visit.add((nr,nc))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visit:
                    bfs(i,j)
                    islands+=1
        return islands


```

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

Example 2:

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

Constraints:

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.

<details>
  <summary><h3>Show Hint 1</h3></summary>
  <p>Usual DFS algorithm for 2D matrix for prev row & col, next row & col</p>
</details>

---
<details>
  <summary><h3>Show Hint 2</h3></summary>
  <p>Think about the base case for row & col index. And no recursion need for element which is '0' or already visited. Keep track of visited place.</p>
</details>

---
<details>
  <summary><h3>Show ALgorithm</h3></summary>
  <pre>
    dfs:
      if row isLessThan 0 or col isLessThan 0 or row equals ROWLEN or col equals COLLEN
        return
      if grid.at(row,col) equals '0' or isVisited.at(row,col)
        isVisited.at(row,col) -> 0
      dfs -> call row - 1, col
      dfs -> call row, col + 1
      dfs -> call row + 1, col
      dfs -> call row, col - 1
      
  </pre>
</details>

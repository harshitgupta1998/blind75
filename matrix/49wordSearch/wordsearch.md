### 79. Word Search
 Walk Through:
1. Using brute force to iterate all rows and cols, maintain a path to store visited (r,c)
2. Use dfs and keep append all 4 directions, break when i == len (word)
```

    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS=len(board)
        COLS=len(board[0])
        path=set()
        def dfs(r,c,i):
            if i==len(word):
                return True
            if r>=ROWS or c>=COLS or r<0 or c<0 or (r,c) in path or word[i]!=board[r][c]:
                return False
            path.add((r,c)) # add the path to know it is visited
           
            res= dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1,i+1)   
            path.remove((r,c)) # won't go back to the grid it came from
            return res
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0):
                    return True
        return False

```

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?

### 70. Climbing Stairs

Walkthrough
1. We can come up with recursive solution, we can be some O(2^N) solution having many repetitive tasks.
2. This can be optimised using DP top-down approach and having memomization to avoid recomputation of the values.
3. Again we can solve using bottom up approach and using tabular approach refering the last two values and returning dp[n-1]


```
  def numDecodings(self, s: str) -> int:
      # top-down
      dp = {len(s) : 1}
      def dfs(i):
          # when counting use this method to return 1
          if i in dp:
              return dp[i]
          if s[i]=='0':
              return 0
          res=dfs(i+1)

          if i<len(s)-1:
              if s[i]=='1' or (s[i]=='2' and s[i+1]<'7'):
                  res+=dfs(i+2)
          dp[i]=res
          return res

      return dfs(0)
        
  # bottom-up
  for i in range(len(s) - 1, -1, -1):
      if s[i]=='0':
          dp[i]=0
      else:
          dp[i]=dp[i+1]
      if i+1<len(s) and (s[i]=='1'or (s[i]=='2' and s[i+1] in "0123456")):
          dp[i]+=dp[i+2]
  return dp[0]
```


You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```
Example 2:
```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

Constraints:

- 1 <= n <= 45

<details>
  <summary><h3>Show Hint 1</h3></summary>
  <p>This one is very easy just think the output of certain inputs and identify the patterns will hekp you to solve this problem that's all.</p>
</details>

---
<details>
  <summary><h3>Pseudocode</h3></summary>
  <pre>
    one -> 1
    two -> 1
    for i -> 1 to n - 1
      temp -> one
      one -> one + two
      two -> temp
    return one
  </pre>
</details>

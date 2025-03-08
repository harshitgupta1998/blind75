### 5. Longest Palindromic Substring

Walkthrough
1.  We can use 2 pointers start from left and calc all the substr O(N^3)
2.  We can bring the pointer to the center of the string and check the left and right
3.  We will  have to handle the odd and even length separately in that case. O(N^2) SP: O(N)
4.  Using 2D matrix we can use DP to solve the problem. O(N^2) SP:O(N^2)

```
    def longestPalindrome(self, s: str) -> str:
        res=""
        reslen=0
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
               
                if reslen<r-l+1:
                    res=l
                    reslen=r-l+1
                l-=1
                r+=1
        
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
               
                if reslen<r-l+1:
                    res=l
                    reslen=r-l+1
                l-=1
                r+=1
        return s[res:res+reslen]

or

    def longestPalindrome(self, s: str) -> str:
        #         Walkthrough
        # 1.  We can use 2 pointers start from left and calc all the substr O(N^3)
        # 2.  We can bring the pointer to the center of the string and check the left and right
        # 3.  We will  have to handle the odd and even length separately in that case. O(N^2) SP: O(N)
        # 4.  Using 2D matrix we can use DP to solve the problem. O(N^2) SP:O(N^2)
        if len(s)<=1:
            return s
        maxlen=1
        maxstr=s[0]
        dp=[[False for i in range(len(s))] for j in range(len(s))]

        for i in range(len(s)):
            dp[i][i]=True
            for j in range(i):
                if s[j]==s[i] and (i-j<=2 or dp[j+1][i-1]):
                    dp[j][i]=True
                    if i-j+1 > maxlen:
                        maxlen=i-j+1
                        maxstr=s[j:i+1]
        return maxstr
```


Given a string s, return the longest palindromic substring in s.

Example 1:
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```
Example 2:
```
Input: s = "cbbd"
Output: "bb"
```

Constraints:

- 1 <= s.length <= 1000
- s consist of only digits and English letters.

<details>
  <summary><h3>Show Hint 1</h3></summary>
  <p>Use DP approach in memoization. Try t0 use the previously computed palindrome.</p>
</details>

---
<details>
  <summary><h3>Show Hint 2</h3></summary>
  <p>Can also use two pointer approach. By separating loop for odd and even length palindrome.</p>
</details>

---
<details>
  <summary><h3>Show Hint 3</h3></summary>
  <p>For each iteration increase the right pointer and decrease left pointer while both characters are equal and update if the current length of palindrome string is greater than previous one.</p>
</details>

---
<details>
  <summary><h3>Pseudocode</h3></summary>
  <pre>
    res -> ""
    resultLength -> 0
    for i -> 1 to lengthOf(s)
      l -> 1, r -> i
      //for odd length
      while l greaterThanOrEqualTo 0 and r lessThan lengthOf(s) and s.charAt(l) equals s.charAt(r)
        if r - l + 1 isGreaterThan resultLength then
          res -> s.substring(l to r+1)
          resultLength -> r - l + 1
        l -> l - 1
        r -> r - 1
      //for even length
      l -> i, r -> i + 1
      while l greaterThanOrEqualTo 0 and r lessThan lengthOf(s) and s.charAt(l) equals s.charAt(r)
        if r - l + 1 isGreaterThan resultLength then
          res -> s.substring(l to r + 1)
          resultLength -> r - l + 1
        l -> l - 1
        r -> r - 1
    return res
  </pre>
</details>

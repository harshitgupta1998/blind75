### 3. Longest Substring Without Repeating Character
Walkthrough:

1. We can use left and right pointer starting from left, then maintain a len var to store the max length
2. We can also push and pop from the set, while maintaining the max len and return it.   TC O(2*N)
3. Optimal we can do is, instead of moving l by 1 we can try to directly move it to position of character and instead of set we can use map or dict. TC O(N)

```
    # O(2N)
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0: #check base case
            return 0
        # initial th`e values
        res=0
        l=0
        set1=set()
        for r in range(len(s)):
            if s[r] in set1:
                # because we need to pop until the duplicate in set
                while l<r and s[r] in set1:
                    set1.remove(s[l])
                    l+=1
            set1.add(s[r])
            res=max(res,r-l+1)
        return res
    TC O(N)
    def lengthOfLongestSubstring(self, s: str) -> int:
    map=[-1]*256
    left,right,length=0,0,0
    n=len(s)
    while right<n:
        if map[ord(s[right])] != -1:
            left=max(map[ord(s[right])]+1,left)
        map[ord(s[right])]=right
        length=max(length,(right-left+1))
        right+=1
    return length

```

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```
Example 2:
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
Example 3:
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

Constraints:

- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.

<details>
  <summary><h3>Show Hint 1</h3></summary>
  <p>Use of both Hashtabla and sliding window will make it easy. And also have another pointer to keep track of length of window.</p>
</details>

---
<details>
  <summary><h3>Show Hint 2</h3></summary>
  <p>Check hastable if character exists if not then max the result or else if string at index is less than l pointer then max the result else make l to last occurence of s at index.</p>
</details>

---
<details>
  <summary><h3>Pseudocode</h3></summary>
  <pre>
    exists -> hashtable()
    l -> 0
    res -> 0
    for r -> 0 to s.length
      if s.atIndex(r) not in hashtable.keys() then res -> maximum(res, r - l + 1)
      else
        if hashtable[s.atIndex(r)] is lessThan l then res -> maximum(res, r- l + 1)
        else
          l -> hashtable[s.atIndex(r)]
    return res
  </pre>
</details>

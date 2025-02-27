### 125. Valid Palindrome


Walkthrough
###
1. Brute force it is to iterate the entire list and store the alphanumeric values then check nums==nums[::-1] i.e TC -  O(N^2) SC - O(1)
2. declare left and right pointer then increment the left or decrement the right if they are not alphanum else check is s[l].lower()==s[r].lower() if not return false
```
  ### Make sure to use isalnum() and not isalpha()
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            print(s[l],s[r])
            
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif (s[l].lower())==(s[r].lower()):
                l+=1
                r-=1
                
            
            else:
                return False
        return True

        
```

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```
Example 2:
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```
Example 3:
```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

Constraints:

- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.

<details>
  <summary><h3>Show Hint 1</h3></summary>
  <p>You can easily solve it in linear time, but only thing is you don't need to consider special character by just reversing string and check it with forward string.</p>
</details>

---
<details>
  <summary><h3>Show Hint 2</h3></summary>
  <p>Use 2 pointer method 1 pointer for forward string and another one is for backward string.</p>
</details>

---
<details>
  <summary><h3>Pseudocode</h3></summary>
  <pre>
    toCheck -> alphanumericCharacteres()
    forwardStr -> ""
    reversedStr -> ""
    l -> 0
    r -> s.length()
    s -> s.toLower()
    while (l lessThan s.length() and r > -1)
      if s.charAt[l] in toCheck then forwardStr -> forwardStr + s.charAt[l]
      if s.charAt[r] in toCheck then reversedStr -> reversedStr + s.charAt[r]
      l -> l + 1
      r -> r - 1
    return true if forwardStr == reversedStr else false
  </pre>
</details>

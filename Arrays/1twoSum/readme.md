## 1. Two Sum


Walkthrough
###
1. Brute force it is to iterate the entire list in O(N^2) and see if nums[i}+nums[j]==target return [i,j] i.e TC -  O(N^2) SC - O(1)
2. we can use a set here where we can store the value in set and see if the value is already in set
3. or directly map={} store map[nums[i]]=i then see if the target - nums[i] is in the map and return [map[nums[i],i] i.e TC -  O(N) SC - O(N)

```
  ### We can use enumerate to access the value and key at once
 def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={} 
        for i in range(len(nums)):
            if target-nums[i] in map:
                return [map[target-nums[i]],i]
            else:
                map[nums[i]]=i
        
```

## question 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
### Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```
```

```


<details>
  <summary><h2>Show Hint 1</h2></summary>
  <p>The most brute force way is to consider every combination of the array, but there is an optimal way to take combination by fixing a number x.</p>
</details>

---
<details>
  <summary><h2>Show Hint 2</h2></summary>
  <p>If you have a number, let's say 'x,' we know that 'target - x' yields some values. Check whether that number exists in the array</p>
</details>

---
<details>
  <summary><h2>Show Hint 3</h2></summary>
  <p>Instead of still doing it in a brute force manner, try to think of a data structure that can help you solve it in linear time.</p>
</details>

---
<details>
  <summary><h2>Show Hint 4</h2></summary>
  <p>Use hashmap to solve by storing the 'target - x' as a key and index as a value.</p>
</details>

---
<details>
  <summary><h2>PseudoCode</h2></summary>
  <pre>
    hashmap -> map()
    for index, number in array
      difference -> target - x
      if difference is in target
        return [hashmap[difference], index]
    return []
  </pre>
</details>

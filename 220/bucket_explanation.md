# 🪣 Bucket Pattern: Complete Guide

**Master Guide for Proximity Problems with O(n) Time Complexity**

---

## 🎯 Problem Understanding

### LeetCode Problem: Contains Duplicate III

**Given:** Integer array `nums`, integers `indexDiff` and `valueDiff`  
**Find:** If there exists pair of indices `(i, j)` such that:
- `i != j` (different indices)
- `abs(i - j) <= indexDiff` (close indices)  
- `abs(nums[i] - nums[j]) <= valueDiff` (close values)

**Example:**
```
Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: Indices (0,3) satisfy all conditions
```

### Why This Problem is Tricky

- **Dual Constraints:** Both spatial (index) and value proximity required
- **Efficiency Challenge:** Naive O(n²) approach too slow for large inputs
- **Edge Cases:** Negative numbers, zero boundaries, exact matches

---

## 🔍 Why Bucket Pattern?

### The Core Insight

> **Key Realization:** If we group values into buckets of size `valueDiff + 1`, then any two values in the same bucket will differ by at most `valueDiff`. Values in adjacent buckets might also satisfy the constraint.

### Bucket Strategy Breakdown

```
Bucket Strategy for valueDiff = 2:
┌─────────────┬─────────────┬─────────────┬─────────────┐
│  Bucket -1  │  Bucket 0   │  Bucket 1   │  Bucket 2   │
│ [-5,-4,-3]  │  [0,1,2]    │  [3,4,5]    │  [6,7,8]    │
└─────────────┴─────────────┴─────────────┴─────────────┘
```

**Rules:**
1. **Same bucket:** Guaranteed match (difference ≤ valueDiff)
2. **Adjacent buckets:** Need to verify distance ≤ valueDiff  
3. **Non-adjacent buckets:** Impossible to satisfy constraint

---

## ⚙️ Algorithm Deep Dive

### Core Implementation

```python
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0:
            return False
        
        bucket = {}
        w = valueDiff + 1  # Bucket size
        
        for i, num in enumerate(nums):
            m = num // w  # Bucket ID
            
            # Check same bucket (guaranteed match)
            if m in bucket:
                return True
            
            # Check adjacent buckets
            if m - 1 in bucket and abs(num - bucket[m - 1]) < w:
                return True
            if m + 1 in bucket and abs(num - bucket[m + 1]) < w:
                return True
            
            # Add current number to its bucket
            bucket[m] = num
            
            # Maintain sliding window
            if i >= indexDiff:
                del bucket[nums[i - indexDiff] // w]
        
        return False
```

### Algorithm Steps

1. **Initialize:** Create empty bucket map, set bucket size = `valueDiff + 1`
2. **For each element:**
   - Calculate bucket ID using integer division
   - Check if same bucket contains any element (instant match)
   - Check adjacent buckets and verify distance constraint
   - Add current element to its bucket
   - Remove elements outside sliding window

---

## 📊 Complete Example Walkthrough

### Example: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0

**Setup:** `w = 0 + 1 = 1` (bucket size)

#### Step 1: Process index 0, num = 1
```
Bucket ID: 1 // 1 = 1
Buckets: {} (empty)
Check: No buckets to check
Action: bucket[1] = 1
Result: bucket = {1: 1}
```

#### Step 2: Process index 1, num = 2  
```
Bucket ID: 2 // 1 = 2
Buckets: {1: 1}
Check same bucket (2): Not found
Check bucket 1: Found value 1, abs(2-1) = 1 < 1? False
Check bucket 3: Not found
Action: bucket[2] = 2
Result: bucket = {1: 1, 2: 2}
```

#### Step 3: Process index 2, num = 3
```
Bucket ID: 3 // 1 = 3  
Buckets: {1: 1, 2: 2}
Check same bucket (3): Not found
Check bucket 2: Found value 2, abs(3-2) = 1 < 1? False
Check bucket 4: Not found
Action: bucket[3] = 3
Result: bucket = {1: 1, 2: 2, 3: 3}
```

#### Step 4: Process index 3, num = 1 🎉
```
Bucket ID: 1 // 1 = 1
Buckets: {1: 1, 2: 2, 3: 3}  
Check same bucket (1): Found value 1! ✅
FOUND MATCH at indices (0,3)!
Return True
```

---

## 📈 Complexity Analysis

| Approach | Time Complexity | Space Complexity | Explanation |
|----------|----------------|------------------|-------------|
| Brute Force | O(n × indexDiff) | O(1) | Check all pairs within range |
| **Bucket Pattern** | **O(n)** | **O(indexDiff)** | Each element processed once |
| SortedSet | O(n log indexDiff) | O(indexDiff) | Binary search operations |

### Why O(n) Time?

- **Each element visited once:** Single pass through array
- **Constant bucket operations:** Hash map insert/delete/lookup all O(1)
- **Limited bucket checks:** At most 3 buckets checked per element
- **Bounded space:** At most `indexDiff + 1` elements in buckets at any time

---

## 💡 Pro Tips & Tricks

### 💡 Pattern Recognition
- **"Close indices + close values"** → Consider bucket pattern
- **Small value differences** → Bucket pattern is optimal
- **Large arrays with proximity constraints** → O(n) matters over O(n log k)

### 💡 Implementation Tips
- **Bucket size = valueDiff + 1:** Ensures same-bucket elements satisfy constraint
- **Check 3 buckets max:** Current bucket + two adjacent buckets
- **Sliding window maintenance:** Remove element at `i - indexDiff` when `i >= indexDiff`
- **Distance check:** Use `< w` instead of `≤ valueDiff` for adjacent buckets

### 💡 Why `< w` Works
```python
# For adjacent bucket elements:
# Max difference = w - 1 = (valueDiff + 1) - 1 = valueDiff
# So checking `< w` is equivalent to checking `≤ valueDiff`
abs(num - bucket[adjacent]) < w  # Correct!
```

---

## 🧪 Additional Examples & Edge Cases

### Example 1: Negative Numbers
```python
Input: nums = [-1, 0, 1], indexDiff = 1, valueDiff = 1
```

**Trace:**
```
w = 2, indexDiff = 1

i=0, num=-1: bucket = -1//2 = -1, buckets = {-1: -1}
i=1, num=0:  bucket = 0//2 = 0
  Check bucket 0: Not found
  Check bucket -1: Found -1, abs(0-(-1)) = 1 < 2 ✅
  MATCH found!
```

### Example 2: Large Value Differences  
```python
Input: nums = [1, 10, 20], indexDiff = 2, valueDiff = 5
```

**Analysis:** All elements in different buckets, differences > 5, returns False

### Example 3: Exact Matches (valueDiff = 0)
```python
Input: nums = [1, 2, 1], indexDiff = 2, valueDiff = 0
```

**Bucket size = 1:** Each value gets its own bucket, only same bucket matches count

---

## 🔧 Optimization Techniques

### When to Use Bucket Pattern

✅ **Best for:**
- Small to medium `valueDiff` (≤ 1000)
- Large arrays where O(n) vs O(n log k) matters
- Problems requiring proximity constraints

❌ **Consider alternatives when:**
- Very large `valueDiff` relative to value range
- Need to find all pairs (not just existence)
- Memory is extremely constrained

### Hybrid Approach
```python
def chooseBestApproach(nums, indexDiff, valueDiff):
    if valueDiff <= 1000 and len(nums) > 1000:
        return "bucket"  # O(n) worth the complexity
    else:
        return "sortedset"  # Simpler implementation
```

---

## 🎓 Related Problems & Variations

### Similar Bucket Pattern Problems
- **Contains Duplicate I & II:** Simpler versions without value constraints
- **Group Anagrams:** Bucketing strings by character frequency
- **Top K Frequent Elements:** Bucket sort by frequency

### Pattern Extensions
- **2D Proximity:** Extend bucketing to coordinate pairs
- **Multiple Constraints:** Additional filtering within buckets  
- **Streaming Data:** Maintain buckets with timestamps
- **Range Queries:** Count elements within range instead of existence

---

## 📝 Interview Preparation Checklist

- [ ] Can explain bucket size calculation (`valueDiff + 1`)
- [ ] Can trace through examples with positive and negative numbers
- [ ] Understand why checking 3 buckets maximum is sufficient
- [ ] Can implement sliding window maintenance correctly
- [ ] Know when to choose bucket pattern over alternatives
- [ ] Can handle edge cases (empty array, valueDiff = 0)

---

## 🚀 Final Code Implementation

```python
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        Bucket pattern solution for Contains Duplicate III.
        
        Time: O(n), Space: O(min(n, indexDiff))
        
        Args:
            nums: List[int] - Array of integers
            indexDiff: int - Maximum index distance
            valueDiff: int - Maximum value distance
            
        Returns:
            bool - True if valid pair exists
        """
        if valueDiff < 0:
            return False
        
        bucket = {}
        w = valueDiff + 1  # Bucket size
        
        for i, num in enumerate(nums):
            m = num // w  # Bucket ID
            
            # Same bucket = guaranteed match
            if m in bucket:
                return True
            
            # Check adjacent buckets
            if m - 1 in bucket and abs(num - bucket[m - 1]) < w:
                return True
            if m + 1 in bucket and abs(num - bucket[m + 1]) < w:
                return True
            
            # Add to bucket and maintain sliding window
            bucket[m] = num
            if i >= indexDiff:
                del bucket[nums[i - indexDiff] // w]
        
        return False
```

---

## 🎯 When to Use This Pattern

### Perfect Scenarios
```
✅ Proximity problems with dual constraints
✅ Small value differences (efficient bucketing)
✅ Large datasets where O(n) vs O(n log k) matters
✅ Problems asking for existence (not enumeration)
```

### Consider Alternatives
```
❌ Very large value differences
❌ Need to find all valid pairs
❌ Complex distance metrics
❌ Multi-dimensional proximity
```

---

## 🏆 Mastery Summary

> *"The bucket pattern transforms proximity problems from O(n²) brute force to O(n) elegance by leveraging the mathematical property that nearby values cluster in predictable ranges."*

### 🎯 Key Mastery Points

**✅ Core Concept:** Bucket size = constraint + 1 ensures same-bucket validity  
**✅ Efficiency:** O(n) time through constant bucket operations  
**✅ Space Management:** Sliding window keeps memory bounded  
**✅ Edge Handling:** Works with negatives, zeros, and boundary cases  
**✅ Pattern Recognition:** Identify when bucketing applies vs alternatives

The bucket pattern is your **O(n) superpower** for proximity-based problems. Master it, and you'll elegantly solve an entire class of algorithmic challenges that stump others with inefficient approaches!

🎯 **Master the pattern, ace the interview!** 🚀
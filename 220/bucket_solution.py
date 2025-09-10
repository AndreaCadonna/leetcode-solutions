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
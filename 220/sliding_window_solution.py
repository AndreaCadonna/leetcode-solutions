class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        Find if there exists a pair (i,j) with close indices and close values.
        
        Args:
            nums: List[int] - Array of integers
            indexDiff: int - Maximum allowed index difference
            valueDiff: int - Maximum allowed value difference
            
        Returns:
            bool - True if such pair exists, False otherwise
        """
        # Guard clause: need at least 2 elements
        if len(nums) < 2:
            return False
            
        from sortedcontainers import SortedSet
        
        # Sliding window to maintain elements within indexDiff range
        window = SortedSet()
        
        for i, num in enumerate(nums):
            # Remove elements that are too far (outside window)
            if i > indexDiff:
                window.remove(nums[i - indexDiff - 1])
            
            # Check if current number has a "close enough" neighbor in window
            # We need to find any x in window such that abs(num - x) <= valueDiff
            # This means x should be in range [num - valueDiff, num + valueDiff]
            
            # Find the smallest element >= (num - valueDiff)
            pos = window.bisect_left(num - valueDiff)
            
            # Check if this element exists and is within valueDiff
            if pos < len(window) and window[pos] <= num + valueDiff:
                return True
            
            # Add current number to window for future iterations
            window.add(num)
        
        return False

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        Find the minimal length of subarray whose sum is >= target.
        
        Args:
            target (int): Target sum value
            nums (List[int]): Array of positive integers
            
        Returns:
            int: Minimal length of valid subarray, or 0 if none exists
        """
        # Guard clause: edge case handling
        if not nums:
            return 0
            
        n = len(nums)
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        # Sliding window: expand with right, shrink with left
        for right in range(n):
            # Expand: add current element to window
            current_sum += nums[right]
            
            # Shrink: while constraint satisfied, try to minimize length
            while current_sum >= target:
                # Record current window length
                window_length = right - left + 1
                min_length = min(min_length, window_length)
                
                # Shrink window from left
                current_sum -= nums[left]
                left += 1
        
        # Return result: 0 if no valid subarray found
        return min_length if min_length != float('inf') else 0
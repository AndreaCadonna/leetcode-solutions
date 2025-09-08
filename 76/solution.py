class Solution(object):
    def minWindow(self, s, t):
        """
        Find minimum window substring containing all characters of t.
        
        Args:
            s (str): Source string to search in
            t (str): Target string with required characters
            
        Returns:
            str: Minimum window substring or empty string if none exists
        """
        if not s or not t or len(s) < len(t):
            return ""
        
        # Build frequency map for target string t
        target_freq = {}
        for char in t:
            target_freq[char] = target_freq.get(char, 0) + 1
        
        # Sliding window variables
        left = 0
        min_window_start = 0
        min_window_len = float('inf')
        
        # Track how many unique characters we've satisfied
        required_chars = len(target_freq)
        satisfied_chars = 0
        
        # Current window frequency map
        window_freq = {}
        
        # Expand window with right pointer
        for right in range(len(s)):
            char = s[right]
            
            # Add character to window
            window_freq[char] = window_freq.get(char, 0) + 1
            
            # Check if this character's frequency requirement is now satisfied
            if char in target_freq and window_freq[char] == target_freq[char]:
                satisfied_chars += 1
            
            # Try to shrink window while it remains valid
            while satisfied_chars == required_chars:
                # Update minimum window if current is smaller
                if right - left + 1 < min_window_len:
                    min_window_len = right - left + 1
                    min_window_start = left
                
                # Remove leftmost character from window
                left_char = s[left]
                window_freq[left_char] -= 1
                
                # Check if removing this character breaks a requirement
                if left_char in target_freq and window_freq[left_char] < target_freq[left_char]:
                    satisfied_chars -= 1
                
                left += 1
        
        # Return minimum window or empty string if none found
        return "" if min_window_len == float('inf') else s[min_window_start:min_window_start + min_window_len]
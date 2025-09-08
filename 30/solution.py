class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # 1) Guard clauses
        if not s or not words or not words[0]:
            return []
        
        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words
        
        if len(s) < total_len:
            return []
        
        # 2) Core DS - word frequency map
        from collections import defaultdict
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        
        result = []
        
        # 3) Main logic - sliding window for each starting offset
        # We need to check each possible starting offset (0 to word_len-1)
        for offset in range(word_len):
            left = offset
            seen_words = defaultdict(int)
            matched_words = 0
            
            # Slide window in word_len chunks
            for right in range(offset, len(s) - word_len + 1, word_len):
                # Extract word at right position
                word = s[right:right + word_len]
                
                if word in word_count:
                    seen_words[word] += 1
                    
                    # If we've seen this word the correct number of times or less
                    if seen_words[word] <= word_count[word]:
                        matched_words += 1
                    else:
                        # We've seen this word too many times, shrink window from left
                        while seen_words[word] > word_count[word]:
                            left_word = s[left:left + word_len]
                            seen_words[left_word] -= 1
                            if seen_words[left_word] < word_count[left_word]:
                                matched_words -= 1
                            left += word_len
                    
                    # Check if we have a valid window with all words matched
                    if matched_words == total_words:
                        result.append(left)
                        # Move left pointer to start looking for next match
                        left_word = s[left:left + word_len]
                        seen_words[left_word] -= 1
                        matched_words -= 1
                        left += word_len
                else:
                    # Word not in our dictionary, reset the window
                    seen_words.clear()
                    matched_words = 0
                    left = right + word_len
        
        return result
        
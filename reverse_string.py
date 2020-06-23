    def reverseString(s):
        """
        Do not return anything, modify s in-place instead.
        """
        # 2 pointer approach 
        first = 0
        last = len(s) - 1
        
        while first < last:
            s[first], s[last] = s[last], s[first]
            first, last = first + 1, last - 1
            
        
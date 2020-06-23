"""
"What is the best profit we can get from selling the wines with prices stored in the array p, 
when the current year is year and the interval of unsold wines spans through [be, en], inclusive?
"""

# Backtrack solution to the problem with O(2^N) complexity
def profit(year, be, en):
    if be > en:
        return 0  
    return max(
        profit(year+1, be+1, en) + year*store[be],
        profit(year+1, be, en-1) + year*store[en] 
        )

def profit_memo(be, en):
    if be > en:
        return 0
    year = len(store)-(en-be+1)+1
    
    if price_cache[be][en] != -1:
        return price_cache[be][en]
    
    price_cache[be][en] = max(
        profit_memo( be+1, en) + year*store[be],
        profit_memo( be, en-1) + year*store[en] 
        )    
    return price_cache[be][en]

if __name__ == "__main__":
    store = [1, 4, 6, 2, 1, 4]
    print(profit(1, 0, len(store)-1))
    print(profit_memo(0, len(store)-1))
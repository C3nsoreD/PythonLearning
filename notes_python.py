'''
Does python call by reference or call by value?
'''
name = 'text'

def add_chars(str1):
    print( id(str1) ) #=> 4353702856
    print( id(name) ) #=> 4353702856
    
    # new name, same object
    str2 = str1
    
    # creates a new name (with same name as the first) AND object
    str1 += 's' 
    print( id(str1) ) #=> 4387143328
    
    # still the original object
    print( id(str2) ) #=> 4353702856
    
    
# add_chars(name)
# print(name) #=>text

'''
What is the difference between a shallow and a deep copy?
'''
# pointing by reference
li1 = [['a'],['b'],['c']]
li2 = li1
li1.append(['d'])
print(li2)  #=> [['a'], ['b'], ['c'], ['d']]


# shallow copy
li3 = [['a'],['b'],['c']]
li4 = li3.copy()
li3.append([4])
print(li4)  #=> [['a'], ['b'], ['c']]

li3[0][0] = ['X']
print(li4)  #=> [[['X']], ['b'], ['c']]


# deep copy
import copy

li5 = [['a'],['b'],['c']]
li6 = copy.deepcopy(li5)

li5.append([4])
li5[0][0] = ['X']
print(li6)  #=> [['a'], ['b'], ['c']]

'''
How to combine two lists into a list of tuples?
'''
a = ['a','b','c']
b = [1,2,3]
[(k,v) for k,v in zip(a,b)] #=> [('a', 1), ('b', 2), ('c', 3)]
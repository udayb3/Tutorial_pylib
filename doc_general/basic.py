# Result of a division is always in decimals
print( 4/3 )
# True and False are actually 0 and 1 but in form of keywords
print( True+1 )
# None, 0 and empty string/sets/list/dict/tuple give false, all others give true
print(bool(None), bool(set()))

# is checks if two variables refer to the same object and == checks if they are equal in value, use is to compare to None
a:list= [1,2]; b=a; c=[1,2]
print(c is a, b is a)

# strings can be concatenated without using +
ch1= "See" " this"
print(ch1)

# Assigning previously unassigned variables causes exception, no declaration possible
# Ternary operator ? can be used as below
ch2= 2 if None is 7 else 4
print(ch2)

# Using lists:      
#   METHODS: append, pop(from back), remove, insert, index, extend
#   SLICING: list[ start: end: step ]
#   Using del to remove any arbitary index, + to add two list, * to unpack values from the list
l1:list= []; l2= [1,2]
l2.append(3);   l2.append(4);   l2.pop(); l2.remove(1); 
del l2[0]; l2.insert(0,-1)
print(l2)
print(*l2)

# Using tuples(list like but immutable)

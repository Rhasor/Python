# Tuples need a comma to be defined
# A tuple is an immutable ordered collection of items
# They are defined by enclosing items in parentheses ()
# but the parentheses are optional unless needed for clarity or to avoid ambiguity
x1 = (40, 2)
x2 = 40, 2
print(type(x1)) # <class 'tuple'>
print(type(x2)) # <class 'tuple'>

rax = 3*(40 + 2,)
print(rax) # A tuple with one element needs a trailing comma
print(type(rax)) # <class 'tuple'>

x = (1, 2, 3)
print(type(x[0:2])) # <class 'tuple'>



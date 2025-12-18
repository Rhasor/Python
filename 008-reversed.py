# x = [1,2,3,4,5]
# print(tuple(reversed(x)))
# print('---with list()---')
# print(list(reversed(x)))
print('---with sort()---')
x = ['apple', 'banana', 'pear', 'grape', 'kiwi', 'fig', 'pineapple']
# x.sort(key=len)
x.sort(reverse=True)

print(x)
adding=[1, 2, 3] + [4, 5, 6]
print(adding)

print('--1--')
repeating = ['Hello'] * 5
print(repeating)
repeating1 = ('Hello' * 5)
print(repeating1)

print('--2--')
mixed = [1, 2, 3] * 3 + ['Hello'] * 2
print(mixed)

print('--error example--')
mixed1 = [1, 2, 3] + 'Hello' * 2
print(mixed1)

mixed2 = '1, 2, 3' + 'Hello' * 2
print(mixed2)
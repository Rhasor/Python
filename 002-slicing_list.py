numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[7:10])#first index is inclusive, second is exclusive
print(numbers[7:11])
print(numbers[7:9])
print(numbers[3:6])
print('--1--')
print(numbers[-3:-1])
print(numbers[-3:0])
print(numbers[-3:])
print('--2--')
print(numbers[:3])
print(numbers[:])
print(numbers[3:])  
print(numbers[:-3])

# longer slices with step values
print('--3--')
print(numbers[1:7:2])# Every second number
print(numbers[1:7:1])
print(numbers[1:7:3])# Every third number
print(numbers[1:7:4])
print(numbers[1:7:5])
print('--4--')
print(numbers[::2])
print(numbers[1::2])
print(numbers[::3])
print(numbers[::-1]) # Reverse the list
print(numbers[-1::-1])
print('--5--')
print(numbers[-3::-1])# Every element from -3 to the beginning
print(numbers[-3:1:-1])
print(numbers[-3:0:-1])
print(numbers[-3:1:-2])
print(numbers[-3::-2])
print('--6--')
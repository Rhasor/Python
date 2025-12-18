# check a user name and PIN code
print('---User PIN code check---')

datebase =[
    ['alice', '1234'],
    ['bob', '5678'],
    ['carol', 'abcd']
]
username = input('Enter your username: ')
pin = input('Enter your PIN code: ')

if[username, pin] in datebase:
    print('Access granted')
else:
    print('Access denied')
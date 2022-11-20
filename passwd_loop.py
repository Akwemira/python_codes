# This code verifies the username and password of a user 5 times
# After the 5th attempt, display Account Locked. 
username = ''
password = ''
attempts = 0

while attempts < 5:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == 'mimi' and password == 'java':
        print('You have Access')
        break
    else:
        print('Incorrect credentials, try again.')
        attempts += 1
        
if attempts == 5:
    print("Account Locked")
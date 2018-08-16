"""Steven Howlett"""
MIN_LENGTH=3
password=input("password:")
while len(password) < MIN_LENGTH:
    password = input("enter password with a min of 3 characters")
print('*'*len(password))
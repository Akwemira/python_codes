# This code writes a program to display an account id from the arn below:

arn = "arn:aws:iam::123456789012:user/Development/product_1234/*"
print("") # creating 1 line spacing to make output more visible 
print(arn)
#display on the screen:the aws account id is: account_id
account_id = (arn.split(":")[4])
print("")
#display on the screen:the aws account id is: account_id
print(f'The AWS account id is: {account_id}')
print("")


#write a program to display account id from arn below:
arn = "arn:aws:iam::123456789012:user/Development/product_1234/*"
#display on the screen:the aws account id is: account_id
print(arn.split(":")[4])


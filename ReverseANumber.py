num=int(input("Enter a number:"))

#initiate value to null
test_num=0

while(num>0):
    remainder=num%10
    test_num=(test_num*10)+remainder
    num=num//10

print("The reverse number is:{}".format(test_num))

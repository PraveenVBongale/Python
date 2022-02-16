num=int(input("Enter a number:"))

if num<0:
    print("Enter a Positive Number")
else:
    sum=0

#USE WHILE LOOP TO ITERATE UNTILL ZERO

while(num>0):
    sum+=num
    num-=1
print("The sum is:",sum)

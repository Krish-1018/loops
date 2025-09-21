
# 1) Take an integer and print the multiplication table of the interger upto a factor of 10 in this form -> n x 1 = n

i = int(input("enter the number"))
for n in range(1,11):
        print(F"{i} X {n} = {i*n}")


# 2) Take an integer and return the factorial

a = int(input("enter the number"))
fact=1
for i in range(a,1,-1):
    fact = i*fact
print(fact) 


# 3) Take an integer and print "YES" if the integer is prime and "NO" if it is not

a = int(input("enter the number"))
for i in range(2,int(a**0.5)+1):
    if a%i==0:
        print("NO")
        break
else:
    print("YES")

#2nd method
a = int(input("enter the number"))
count = 0
for i in range(2,a):
    if a%i==0:
        count = 1
        break
if count==1:
    print("NO")
else:
    print("YES")


# 4) Take two numbers and find product of all numbers between them that satisfy following condition (inclusive range):
# -> Numbers should be even
# -> Second last digit of number is 4

a= int(input("enter first number"))
b = int(input("enter second number"))
count = 0
product =1 
for i in range(a,b+1):
  if i%2==0 and (i//10)%10==4:
    product *= i
    count =1
if count==1:
  print(product)
else:
  print(0)  

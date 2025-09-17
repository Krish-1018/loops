
#when break is encountered the control comes out of the loop and rest part of the loop doesn't execute
#break will end loop but not  the program


for i in range(1,6,1):
    if i == 4:
        break
    print(i) #1,2,3
print("I am outside")


for i in range(1,5):
    print(i) #1
    break


for i in range(1,6,1):
    if i==4:
        break
    print(i) #1,2,3

# continue stops only that particular iteration 


for i in range(1,6,1):
    if i == 4:
        continue
    print(i) #1,2,3,5
print("I am outside")


for i in range(1,5):
    print(i) #1,2,3,4
    continue


#In Python, the pass statement is a null operation or a placeholder.
#  It is used when you need to have a statement syntactically but don’t want to execute any code. 
# Essentially, it allows you to leave blocks of code empty without causing an error.


for i in 'Python Training Session':
    if i=="p":
        pass
    elif i=="y":
        continue
    elif i=="g":
        break
    else:
        print(i)

# some basic questions

for i in range(1,5,2): # i-start =1, i-end = 4, step 2
    print(i)



for i in range(10,50,12): # i-start =10, i-end = 49, step 12
    print(i) #10, 22, 34,46



for i in range(0,10,10): # i-start: 0 , i-end: 9 , step :10
    print(i) #0


for i in range(5):  # i = 0 , end =4 , step = 1
    print(i)


for i in range(0):  # i = 0 , end = -1 , step = 1 (+ve dire)
    print(i) # this gives nothing


for i in range (5,1,-1): # s = 5, e = 2, step = -1
    print(i)


for i in range(2, -3, -1): # s = 2 , end = -2 , step = -1
    print(i)


for i in range(2, -3, 1): # s = 2 , end = -2 , step = 1
    print(i)  # this gives nothing


#1-5 print
for i in range(1,6):
    print(i)

#5-1 print
for i in range(5,0,-1):
    print(i)

#print , count and sum all even number from 1-100


# for i in range(1,101,1):
#     if i%2==0:
#         print(i)

# for i in range(2,101,2):
#     print(i)

# for i in range(1,101,1):
#     i%2==0 and print(i) #short circuit

count = 0
sum = 0
for i in range(1,101):
    if i%2==0 :
        print(i)
        count += 1
        sum += i
print(count) 
print(sum)  



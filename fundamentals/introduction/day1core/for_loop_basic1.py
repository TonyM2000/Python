for i in range (0,151,1):
    print (i)
for i in range (5,1001,5):
    print (i)
for i in range (1,101,1):
    if i%10 ==0:
        print("CODING DOJO")
    elif i%5 ==0:
        print("CODING")
    else:
        print(i)
print("-------")
x=0
for i in range (0,500001):
    if i%2 == 0:
        x +=i
    if i >= 500000:
        print(x)
print("-------")
for i in range(2018,-1,-4):
    if i > 0:
        print(i)
print("-------")
lownum = 0
highnum = 25
mult = 3
for i in range(lownum, highnum+1):
    if (i % mult == 0):
        print(i)
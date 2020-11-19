b=18 
for i in range(1,10):
    for l in range(1,b):
        print (end=' ')
    b=b-1   
    for m in range(1,i):
        print("*", end="")
    print("")    
b=9 
for i in range(10,1,-1):
    for l in range(1,b):
        print (end=' ')
    b=b+1   
    for m in range(1,i):
        print("*", end="")
    print("")    

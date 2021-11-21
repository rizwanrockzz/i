def prime(num):
    flag = True
    for i in range(2, num):
        if (num % i) == 0:
            flag = False
            break
    return flag
    
for i in range(2,100):
    if prime(i):
        print(i)

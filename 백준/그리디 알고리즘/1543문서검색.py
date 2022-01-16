a = input()
b = input()

count = 0
i=0
while(True):
    if(i+len(b)>len(a)):
        break
    x = a[i:len(b)+i]
    if(x==b):
        count += 1
        i += len(b)
    else:
        i += 1
print(count)

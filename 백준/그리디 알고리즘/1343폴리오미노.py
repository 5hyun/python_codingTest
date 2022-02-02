x = input()
count = 0
for i in range(len(x)):
    if(x[i]=='X'):
        count += 1
    
    if(count == 4 or (x[i]=='.' and count == 4)):
        x = x.replace('X', 'A', 4)
        count = 0
    elif((count == 2 and i == len(x)-1) or (x[i]=='.' and count == 2)):
        x = x.replace('X', 'B', 2)
        count = 0
    elif((x[i]=='.' and count % 2 == 1) or (count % 2 == 1 and i == len(x)-1)):
        count = -1
        break
print(x if (count != -1) else -1)
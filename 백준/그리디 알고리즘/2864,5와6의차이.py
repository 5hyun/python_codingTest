a, b = input().split()
len1 = len(a)
len2 = len(b)
La = list(a)
Lb = list(b)

for i in range(len1):
    if(La[i]=='5'):
        La[i] = '6'
for i in range(len2):
    if(Lb[i]=='5'):
        Lb[i] = '6'
int_a = 0
for i in range(len1):
    int_a += int(La[i]) * 10 ** (len1-i-1)
int_b = 0
for i in range(len2):
    int_b += int(Lb[i]) * 10 ** (len2-i-1)
max = int_a + int_b

La2 = list(a)
Lb2 = list(b)
for i in range(len1):
    if(La2[i]=='6'):
        La2[i] = '5'
for i in range(len2):
    if(Lb2[i]=='6'):
        Lb2[i] = '5'
int_a2 = 0
for i in range(len1):
    int_a2 += int(La2[i]) * 10 ** (len1-i-1)
int_b2 = 0
for i in range(len2):
    int_b2 += int(Lb2[i]) * 10 ** (len2-i-1)
min = int_a2 + int_b2

print(min, max, end = ' ')
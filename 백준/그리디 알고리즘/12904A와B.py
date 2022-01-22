s = input()
t = input()
l = len(t) - len(s)
for i in range(l):
    if(t[len(t)-1]=='A'):
        t = t[0:len(t)-1]
    elif(t[len(t)-1]=='B'):
        t = t[0:len(t)-1]
        t = t[::-1]
    if(t == s):
        print(1)
        break
else:
    print(0)
        
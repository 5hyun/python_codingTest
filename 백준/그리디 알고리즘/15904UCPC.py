x = input()
ary = ['U','C','P','C']
for i in range(len(x)):
    if x[i] == ary[0]:
        del ary[0]
    if len(ary) == 0:
        print("I love UCPC")
        break
else:
    print("I hate UCPC")
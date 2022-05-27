# 내 풀이
# n = int(input())

# def setting(data):
#   return data[1]

# ary = []

# for i in range(n):
#   x = input().split()
#   ary.append((x[0], int(x[1])))

# ary.sort(key=setting)

# for i in ary:
#   print(i[0], end=" ")

#교재 풀이
n = int(input())

ary = []

for i in range(n):
  x = input().split()
  ary.append((x[0], int(x[1])))

ary = sorted(ary, key=lambda student: student[1])

for student in ary:
  print(student[0], end=" ")
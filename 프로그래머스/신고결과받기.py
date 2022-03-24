def solution(id_list, report, k):
    answer = []
    name_dic = {}
    for i in id_list:
        name_dic[i] = 0
        
    dic = {}
    for i in range(len(report)):
        t = report[i].split()
        if t[1] in dic:
            if t[0] in dic[t[1]]:
                continue
            else:
                dic[t[1]][0] += 1
                dic[t[1]].append(t[0])
        else:
            dic[t[1]] = [1, t[0]]
    for i in dic:
        if dic[i][0] >= k:
            for j in range(1, len(dic[i])):
                a = dic[i][j]
                name_dic[a] += 1
    for i in name_dic:
        answer.append(name_dic[i])
    return answer
'''import sys

def solution(id_list, report, k):
    answer = []
    name_dic = {}
    for i in id_list:
        name_dic[i] = 0
        
    dic = {}
    for i in range(len(report)):
        t = report[i].split()
        if t[1] in dic:
            if t[0] in dic[t[1]]:
                continue
            else:
                dic[t[1]][0] += 1
                dic[t[1]].append(t[0])
        else:
            dic[t[1]] = [1, t[0]]
    for i in dic:
        if dic[i][0] >= k:
            for j in range(1, len(dic[i])):
                a = dic[i][j]
                name_dic[a] += 1
    for i in name_dic:
        answer.append(name_dic[i])
    return answer

name = sys.stdin.readline()
name = name.replace(" ", "")
name = name.strip("[""]")
name = name.replace("\"", "").strip()
name = name.split(',')
singo = sys.stdin.readline()
singo = singo.strip("[""]")
singo = singo.replace("\"", "").strip()
singo = singo.split(',')
n = int(input())
print(solution(name, singo, n))
'''
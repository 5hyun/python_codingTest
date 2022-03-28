def solution(record):
    answer = []
    dic = {}
    for i in record:
        t = i.split()
        if t[0] == 'Enter' or t[0] == 'Change':
            dic[t[1]] = t[2]
    
    for i in record:
        t = i.split()
        char = ''
        if t[0] == 'Enter':
            char += dic[t[1]] + "님이 들어왔습니다."
            answer.append(char)
        elif t[0] == 'Leave':
            char += dic[t[1]] + "님이 나갔습니다."
            answer.append(char)
    
    #return dic
    return answer

a = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(a))
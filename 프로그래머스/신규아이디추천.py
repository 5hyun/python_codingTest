def solution(new_id):
    from collections import deque
    answer = ''
    new_id = list(new_id.lower())
    rst = deque()
    i = 0
    count = 0
    for i in range(len(new_id)):
        if (97 <= ord(new_id[i]) <= 122) or (48 <= ord(new_id[i]) <= 57)or new_id[i] == '-' or new_id[i] == '_':
            rst.append(new_id[i])
            count = 0
        elif new_id[i] == '.':
            count += 1
            if count > 1:
                count -= 0
                continue
            else:
                rst.append(new_id[i])
    if rst: 
        while len(rst) > 0:
            if rst[0] == '.':
                rst.popleft()
            elif rst[-1] == '.':
                rst.pop()
            else:
                break
    if len(rst) > 15:
        for i in range(15):
            if i == 14 and rst[i] == '.':
                break
            answer += rst[i]
    elif len(rst) <= 2:
        if rst:
            t = rst[-1]
        else:
            t = 'a'
        for i in rst:
            answer += i
        while len(answer) < 3:
            answer += t
    else:
        for i in rst:
            answer += i
    return answer
def solution(lottos, win_nums):
    answer = []
    chk = []
    count = 0
    for i in lottos:
        if i == 0:
            count += 1
        if i in win_nums:
            chk.append(i)
            
    for i in chk:
        del lottos[lottos.index(i)]
        del win_nums[win_nums.index(i)]
    
    t = len(chk) #이게 최소 값
    if t+count == 6:
            answer.append(1)
    elif t+count == 5:
        answer.append(2)
    elif t+count == 4:
        answer.append(3)
    elif t+count == 3:
        answer.append(4)
    elif t+count == 2:
        answer.append(5)
    else:
        answer.append(6)
   
    if t == 6:
        answer.append(1)
    elif t == 5:
        answer.append(2)
    elif t == 4:
        answer.append(3)
    elif t == 3:
        answer.append(4)
    elif t == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    return answer
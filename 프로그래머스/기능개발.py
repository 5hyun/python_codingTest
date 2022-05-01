def solution(progresses, speeds):
    answer = []
    while progresses:
        count = 0
        for i in range(len(progresses)):
            if progresses[i] >= 100:
                continue
            progresses[i] += speeds[i]
        while progresses:
            if progresses[0] >= 100:
                count += 1
                del progresses[0]
                del speeds[0]
                if not progresses and count:
                    answer.append(count)
            else:
                if count > 0:
                    answer.append(count)
                break
            
    return answer
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if i > len(completion) - 1:
            answer = participant[i]
            break
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer

a = ["leo", "kiki", "eden"]
b = ["eden", "kiki"]
print(solution(a,b))
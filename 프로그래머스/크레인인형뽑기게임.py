def solution(board, moves):
    answer = 0
    rst = []#오른쪽 바구니
    game = []
    
    for i in range(len(board)):
        game.append([])
        for j in range(len(board)):
            game[i].append(board[len(board)-1-j][i])
    
    remove_set = {0}
    for i in range(len(game)):
        game[i] = [i for i in game[i] if i not in remove_set]
    for i in moves:
        if game[i-1]:
            t = game[i-1].pop()
            if rst and rst[-1] == t:
                rst.pop()
                answer += 2
            else:
                rst.append(t)
    return answer

a = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
k = [1,5,3,5,1,2,1,4]
print(solution(a, k))
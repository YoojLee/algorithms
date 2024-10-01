def solution(mat, x, y, start_dir):

    # 현재 위치 방문 처리
    mat[y][x] = -1
    answer = 1

    # 왼쪽 방향 정의
    next_dir = {
        0: 3, # 북 -> 서 
        1: 0, # 동 -> 북
        2: 1, # 남 -> 동
        3: 2 # 서 -> 남
    }
    move = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    # 처음에는 무조건 왼쪽으로 회전
    d = next_dir[start_dir]
    while True:
        for _ in range(4): # 상하좌우 탐색
            new_x, new_y = x+move[d][1], y+move[d][0]
        
            if mat[new_y][new_x]==1 or mat[new_y][new_x]==-1: # 바다이거나 (1) 이미 방문했거나 (-1)
                d = next_dir[d] # d를 업데이트해서 방향을 바꾼다
            
            else: # 전진 가능 -> 현재 위치에서의 탐색 마침
                answer += 1
                x, y = new_x, new_y
                mat[y][x] = -1 # 방문 표시
                break
                
        else: # 상하좌우 탐색에 실패할 경우 -> 뒤로 후진 (나머지 연산으로 구현)
            new_x, new_y = x+move[4%(d+1)][1], y+move[4%(d+1)][0]

            if mat[new_y][new_x]==1: # 바다이면
                break

    return answer
            
    

if __name__ == "__main__":
    n, m = 4, 4
    start_x, start_y, start_dir = 1, 1, 0

    mat = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
    answer = solution(mat, start_x, start_y, start_dir)

    print(answer)


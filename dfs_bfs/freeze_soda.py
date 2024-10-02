from collections import deque
def solution(mat, n, m):
    answer = 0

    # 방향 정의
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우

    visited = [[False]*m]*n
    queue = deque()

    for i in range(n):
        for j in range(m):
            # 탐색 시작
            if visited[i][j]:
                continue
            else:
                visited[i][j] = True # 방문처리
                queue.append((i,j))
                while queue:
                    y,x = queue.pop()
                    for d in dir:
                        new_y, new_x = y+d[0], x+d[1]
                        
                        if (0 <= new_y < n) and (0 <= new_x < m):
                            if visited[new_y][new_x]:
                                continue

                            if (mat[new_y][new_x] == 0): # valid 좌표
                                visited[new_y][new_x] = True
                                queue.append([new_y, new_x])                
                answer += 1

    return answer

if __name__ == "__main__":
    n, m = 4,5
    mat = [
        [0,0,1,1,0],
        [0,0,0,1,1],
        [1,1,1,1,1],
        [0,0,0,0,0]
    ]
    answer = solution(mat, n, m)
    print(answer)
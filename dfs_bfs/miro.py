from collections import deque
def solution(mat, n, m):
    answer = 1 # 첫번째 칸 방문
    dir = [[-1,0], [1,0], [0,-1], [0,1]] # 상하좌우
    queue = deque()

    visited = [[False for _ in range(m)] for _ in range(n)] # 그냥 곱해서 만들면 메모리 할당 방식이 다른 듯..
    queue.append((0,0))

    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            while queue:
                y, x = queue.pop()
                visited[y][x] = True # 방문 처리
                for d in dir:
                    new_y, new_x = y+d[0], x+d[1]
                    if not ((0 <= new_y < n) and (0 <= new_x < m)):
                        continue
                    if visited[new_y][new_x] or mat[new_y][new_x] == 0:
                        continue
                    else:
                        queue.append((new_y, new_x))
            answer += 1    

    return answer

if __name__ == "__main__":
    n, m = 5,6
    mat = [
        [1,0,1,0,1,0],
        [1,1,1,1,1,1],
        [0,0,0,0,0,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1]
    ]
    answer = solution(mat, n, m)
    print(answer)
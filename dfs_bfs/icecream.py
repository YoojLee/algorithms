from collections import deque

def is_valid(vy, vx):	
	if 0 <= vy < N and 0 <= vx < M:
		return True
	else:
		return False

def main(N, M, board):
    queue = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    move = [(0, -1), (0, 1), (-1,0), (1,0)] # 방향 정의
    answer = 0
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == '0' and not visited[i][j]:
                visited[i][j] = True
                queue.append((i,j))
                answer += 1
                
            while queue:
                vy, vx = queue.popleft()
                
                # 탐색 방향은 상하좌우
                for mv in move:
                    new_y, new_x = vy+mv[0], vx+mv[1]
                    if is_valid(new_y, new_x) and not visited[new_y][new_x]:
                        visited[new_y][new_x] = True
                        if board[new_y][new_x] == '0':
                                queue.append((new_y, new_x)) # 근데 여기서 바로 append를 하면 안됨

    return answer


if __name__ == "__main__":
    board = """
    00000
    """
    board = [list(row.strip()) for row in board.strip().split("\n")]
    print(board)
    N, M = len(board), len(board[0])
    answer = main(N, M, board)

    print(answer)
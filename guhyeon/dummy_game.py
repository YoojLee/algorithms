# from collections import deque

# def solution():
#     pass

# if __name__ == "__main__":
#     answer = solution()
#     N = int(input())

#     mat = [[0 for _ in range(N)] for _ in range(N)]

#     # 사과 위치 심기
#     K = int(input())
#     for _ in range(K):
#         r, c = map(lambda x: int(x)-1, input().split())

#         mat[r][c] = 100


#     n_traj = int(input())
#     traj = []
#     for _ in range(n_traj):
#         x,c = input().split()
#         traj.append([x,c])

#     traj = deque(traj)

#     print(mat)
#     r, c = 0, 0
#     tail_r, tail_c = 0,0
#     mat[r][c] = 1 # 뱀이 있다
#     d = [[0,1],[1,0],[0,-1],[-1,0]] # 우, 하, 좌, 상
#     cur_d = 0
#     count = 1
#     l = 0
#     print(traj)
#     # 뱀의 운행 시작 -> for loop으로 구현하게 되면 방향 전환을 반영 못함
#     while True:
        
#         print(count, int(traj[0][0]))
#         if count == int(traj[0][0]):
#             new_dir = traj.popleft()[1]
            
#             if new_dir == 'D': # 우측으로 90도 회전
#                 cur_d = (cur_d + 1) % 4
#             else: # 좌측으로 90도 회전
#                 cur_d = (cur_d - 1) % 4
#         # 이동
#         new_r, new_c = r+d[cur_d][0], c+d[cur_d][1]
        
#         if new_r >= N or new_c >= N:
#             break

#         if mat[new_r][new_c] == 100:
#             mat[new_r][new_c] = 1
#             l += 1
#         else:
#             mat[new_r][new_c] = 1
#             mat[new_r-l][new_c-l] = 0 # 아 이걸 2차원으로 길이를 구현하는 게 어렵구나 -> 이렇게 말고 tail을 지정하는 형태는 어떨라나? 약간 2차원 배열 투포인터 형태로
        


#         # 머리만 바꿈
#         r, c = new_r, new_c
#         count += 1


#     print(count)

n = int(input())
k = int(input())
data = [[0] * (n+1) for _ in range(n+1)] # 맵 정보
info = [] # 회전 정보

for _ in range(k):
    a,b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction, C):
    if C == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

    return direction

def simulate():
    x, y = 1, 1 # 처음 위치
    data[x][y] = 2 # 뱀이 있는 곳은 표시함
    direction = 0
    time = 0
    index = 0
    q = [(x,y)] # 현재 위치 -> 위치를 queue로 가져가면 되는 거구나

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2: # 뱀이 있는 곳을 표시해야 자기 자신에 부딪힌 것을 알 수 있음
            if data[nx][ny] == 0: # 사과가 없다면
                data[nx][ny] = 2 # 일단 방문 처리
                q.append((nx, ny)) # 방문한 곳 넣어주기 (이게 어차피 꺾이는 거니까 좌표를 다 넣어주는 게 유리한 것 같다) => 요걸 이렇게 관리하는 게 중요할 듯
                px, py = q.pop(0) # 기존의 tail
                data[px][py] = 0 # 한 칸 움직이기 -> tail이 길어지지 않고 이걸 그냥 움직이는 형태

            if data[nx][ny] == 1: # 사과가 있다면 -> 길이만 늘림
                data[nx][ny] = 2 # 일단 방문 처리
                q.append((nx, ny)) # 방문한 곳 넣어주기 -> 대신 tail을 움직이진 않음
        else:
            time += 1
            break

        x, y = nx, ny
        time += 1
        if index <l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1 # 이걸로 약간 queue 같은 역할을 했다고 봄 -> 얘도 queue로 구현할 수 있지 않을까 싶음
    return time

print(simulate())
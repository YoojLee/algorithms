import heapq

def solution(food_times, k):
    # 음식의 총 시간이 k보다 작거나 같으면 더 섭취할 음식이 없으므로 -1 반환
    if sum(food_times) <= k:
        return -1
    
    # 우선순위 큐에 (음식을 먹는 데 걸리는 시간, 음식 번호) 삽입
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))  # (시간, 음식 번호)
    
    total_time = 0  # 현재까지 음식을 먹는 데 소요된 총 시간
    previous = 0    # 직전 음식이 걸린 시간
    
    length = len(food_times)  # 현재 남은 음식의 개수
    
    # 시간이 가장 적게 걸리는 음식을 하나씩 처리
    while total_time + (q[0][0] - previous) * length <= k:
        now = heapq.heappop(q)[0]  # 시간이 가장 적게 걸리는 음식
        total_time += (now - previous) * length  # 지금까지 걸린 시간 반영
        length -= 1  # 하나의 음식을 다 먹었으므로 남은 음식의 개수 감소
        previous = now  # 직전에 먹은 음식 시간 업데이트
    
    # 남은 음식들 중에서 k - total_time 만큼 남은 시간을 처리
    result = sorted(q, key=lambda x: x[1])  # 음식 번호 기준으로 정렬
    return result[(k - total_time) % length][1]

            

if __name__ == "__main__":
    food_times = [1,1,1]
    k = 3
    print(solution(food_times, k))
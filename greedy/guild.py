# 모험가 길드 -> 공포도가 적은 사람이 많을 수록 유리함. -> 적은 사람부터 그룹을 형성하면 됨.
from collections import Counter
def solution(arr):
    answer = 0
    arr.sort()
    count = 0
    for i in range(len(arr)):
        count += 1
        if count == arr[i]:
            answer += 1
            count = 0
        else:
            continue

    return answer

if __name__ == "__main__":
    arr = [2,3,1,2,2]
    answer = solution(arr)

    print(answer)
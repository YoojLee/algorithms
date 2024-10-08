# 곱하기와 더하기
def solution(ip):
    # 0, 1이 나오면 더한다
    answer = int(ip[0])
    for i in range(1, len(ip)):
        if int(ip[i-1]) in [0, 1]:
            answer += int(ip[i])
        else:
            answer *= int(ip[i])

    return answer

if __name__ == "__main__":
    ip = list(input())
    answer = solution(ip)
    print(answer)
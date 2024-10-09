# 만들 수 없는 금액 -> N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램
def solution(n, coins):
    coins.sort()
    if coins[0] > 1:
        return 1
    else:
        answer = 2
        for i in range(1, n):
            if coins[i] <= answer:
                answer += coins[i]
            else:
                break

    return answer

if __name__ == "__main__":
    n = int(input())
    coins = [int(i) for i in input().split()]

    print(solution(n, coins))
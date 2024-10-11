from itertools import combinations

def solution(weights):
    combs=combinations(weights, 2)
    answer = 0

    for c in combs:
        if c[0] != c[1]:
            answer += 1
    

    return answer

if __name__ == "__main__":
    n,m = input().split()
    weights = list(map(int, input().split()))
    print(solution(weights))
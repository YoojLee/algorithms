def solution(N):
    mid = len(N) // 2
    left = sum(int(c) for c in N[:mid])
    right = sum(int(c) for c in N[mid:])

    if left == right:
        return "LUCKY"

    else:
        return "READY"


if __name__ == "__main__":
    N = input()
    print(solution(N))
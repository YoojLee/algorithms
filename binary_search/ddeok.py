from bisect import bisect_left


def solution(N, M, arr):
    answer = 0

    end = max(arr)
    start = end - M
    # start = 0

    sub_arr = [sum(max(i-j, 0) for i in arr) for j in range(end, start, -1)]
    answer = bisect_left(sub_arr, M)

    return end-answer

if __name__ == "__main__":
    N = 4
    M = 6
    arr=[19, 15, 10, 17]

    answer = solution(N, M, arr)
    print(answer)

def solution(arr):
    answer = [0, 0]

    for i in range(1, len(arr)):
        if (arr[i-1] != arr[i]):
            answer[int(arr[i-1])] += 1
    answer[int(arr[len(arr)-1])] += 1
    return min(answer)

if __name__ == "__main__":
    arr = input()
    arr = list(arr)
    print(solution(arr))

def solution(food_times, k):
    n = len(food_times)
    for i in range(k):
        if food_times[i%n] == 0:
            continue
        food_times[i%n] -= 1

    if sum(food_times) == 0:
        return -1
    else:
        return i%n


if __name__ == "__main__":
    food_times = [3,1,2]
    k = 5
    print(solution(food_times, k))
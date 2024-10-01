def solution(mat):
    min_mat = [min(row) for row in mat]
    return max(min_mat)

if __name__ == "__main__":
    n, m = 2, 4
    mat = [[7,3,1,8], [3,3,3,4]]
    answer = solution(mat)

    print(answer)


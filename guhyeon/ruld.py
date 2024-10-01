def solution(n, traj):
    x, y = 1, 1
    dir = {
        "R": [0, 1],
        "L": [0, -1],
        "U": [-1, 0],
        "D": [1, 0]
    }

    for d in traj:
        dy, dx = dir[d]
        new_x, new_y = x + dx, y + dy

        if (0 < new_x <= n) and (0 < new_y <= n):
            x, y = new_x, new_y

    return y, x


if __name__ == "__main__":
    n = 5
    traj = "R R R U D D".split()
    answer = solution(n, traj)

    print(answer)


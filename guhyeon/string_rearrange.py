def solution(N):
    N = sorted(N)
    alpha = ""
    numeric = 0
    for c in N:
        if c.isalpha():
            alpha += c
        else: # number
            numeric += int(c)
    
    return alpha+str(numeric)


if __name__ == "__main__":
    N = input()
    print(solution(N))
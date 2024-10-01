def check_three(s):
    s = str(s)
    return "3" in s

def solution(N):
    counter = 0
    for h in range(N+1):
        if check_three(h):
            counter += 60*60
            continue
        for m in range(60):
            if check_three(m):
                counter += 60
                continue
            for s in range(60):
                if check_three(s):
                    counter += 1
    
    return counter

"""
# 보다 단순한 버전 -> 휴리스틱 없이 바로 완탐하는 형태
def solution(N):
    counter = 0
    for h in range(N+1):
        for m in range(60):
            for j in range(60):
                if '3' in str(h) + str(j) + str(k):
                    counter += 1
    
    return counter
"""
    

if __name__ == "__main__":
    n = 5
    answer = solution(n)

    print(answer)


def solution(s):
    answer = len(s)
    n = len(s)
    for i in range(1,n//2+1): # 가장 큰 압축률은 반으로 쪼개질 때 성립함
        # loop over string
        compressed=""
        cp = s[:i]
        counter = 1
        for j in range(i, n-i+1, i):
            # print(i, j, cp, s[j:i+j])
            if cp == s[j:i+j]:
                counter += 1
            else:
                if counter == 1:
                    compressed += cp
                else:
                    compressed += f"{counter}{cp}"
                counter = 1
                cp = s[j:i+j]

        if counter == 1:
            compressed += cp
        else:
            compressed += f"{counter}{cp}"
        
        if j+i < n:
            compressed += s[j+i:]

        if len(compressed) < answer:
            answer = len(compressed)
            
    return answer
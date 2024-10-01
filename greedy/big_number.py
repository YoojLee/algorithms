def solution(arr, m, k):
    arr_sort = sorted(arr, reverse=True)
    sub_arr = [arr_sort[0]]*k + [arr_sort[1]]
    return sum(sub_arr) * (m//(k+1)) + sum(sub_arr[:m%(k+1)]) # 인덱싱으로 하는 버전
    
    ## 반복문 사용
    # count, k_count = 0, 0
    # answer = 0
    # while count < m:
    #     count += 1
    #     if k_count < k:
    #         answer += largest
    #         k_count += 1
    #     else:
    #         k_count = 0
    #         answer += s_largest

    #     print(count, answer)
        
    # return answer

if __name__ == "__main__":
    answer = solution([2,4,5,4,6], m=8, k=3)
    print(answer)


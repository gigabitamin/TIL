def can_merge_strings(N, A):
    # 끈을 길이 순으로 정렬
    A.sort()
    
    while len(A) > 1:
        # 가장 짧은 두 개의 끈을 선택
        a = A.pop(0)
        b = A.pop(0)
        
        # 두 끈의 합
        W = a + b
        
        # ⌊W/2⌋와 ⌈W/2⌉가 각각 a, b인지 확인
        if a != W // 2 or b != (W + 1) // 2:
            return "FALSE"
        
        # 두 끈을 이어붙인 결과를 다시 리스트에 넣고 정렬
        A.append(W)
        A.sort()
    
    return "TRUE"

# 예시 테스트 실행
print(can_merge_strings(5, [4, 16, 4, 5, 4]))  # "TRUE"
print(can_merge_strings(2, [1, 5]))            # "FALSE"

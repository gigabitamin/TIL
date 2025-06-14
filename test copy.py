def solution(Frame):
    answer = []
    
    # 1~9번째 프레임 처리
    for i in range(9):
        frame = Frame[i].split()
        
        if len(frame) == 1:  # STRIKE 처리
            answer.append("X")
        else:
            first = frame[0]
            second = frame[1]
            
            # 첫 번째 투구 처리 (0일 때는 "-"로)
            if first == "0":
                first = "-"
            
            # 두 번째 투구 처리 (0일 때는 "-"로)
            if second == "0":
                second = "-"
            
            # SPARE 처리
            if first != "-" and second != "-" and int(first) + int(second) == 10:
                second = "/"
            
            answer.append(f"{first} {second}")
    
    # 10번째 프레임 처리
    last_frame = Frame[9].split()
    result = []
    
    # 첫 번째 투구 처리
    if last_frame[0] == "10":
        result.append("X")
    else:
        result.append(last_frame[0] if last_frame[0] != "0" else "-")
    
    # 두 번째 투구 처리
    if len(last_frame) > 1:
        if last_frame[1] == "10":
            result.append("X")
        else:
            result.append(last_frame[1] if last_frame[1] != "0" else "-")
    
    # SPARE 처리
    if len(last_frame) > 1 and int(last_frame[0]) + int(last_frame[1]) == 10:
        result[1] = "/"
    
    # 세 번째 투구 (보너스 투구)
    if len(last_frame) == 3:
        if last_frame[2] == "10":
            result.append("X")
        else:
            result.append(last_frame[2] if last_frame[2] != "0" else "-")
    
    answer.append(" ".join(result))
    
    return answer

# 입력 예시
Frame = ["8 1", "10", "7 0", "6 4", "0 8", "8 2", "10", "9 0", "0 10", "8 2 5"]

# 함수 호출 및 결과 출력
result = solution(Frame)
print(result)

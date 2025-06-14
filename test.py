def count_hatched_chicks(N, E, D):
    count = 0
    for ei in E:
        # 남은 부화일이 14 - ei일이므로, D일 후에 부화하는지 확인
        if 14 - ei <= D:
            count += 1
    return count

# 예시 테스트 실행
print(count_hatched_chicks(5, [1, 4, 10, 13, 6], 4))  # 2

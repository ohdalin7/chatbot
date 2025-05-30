# Levenshtein_Distance.py

# 문자열 두 개의 레벤슈타인 거리 계산 함수
def calc_distance(a, b):
    ''' 두 문자열 a와 b 사이의 레벤슈타인 거리 계산 '''
    if a == b: return 0  # 문자열이 같으면 거리 = 0
    a_len = len(a)
    b_len = len(b)
    if a == "": return b_len  # a가 비어있으면 b의 길이만큼 삽입 필요
    if b == "": return a_len  # b가 비어있으면 a의 길이만큼 삭제 필요

    # 2차원 배열 생성: (a_len+1) x (b_len+1)
    matrix = [[0] * (b_len + 1) for _ in range(a_len + 1)]

    # 첫 행/열 초기화 (공백 문자와의 거리)
    for i in range(a_len + 1):
        matrix[i][0] = i
    for j in range(b_len + 1):
        matrix[0][j] = j

    # 거리 계산: 삽입, 삭제, 교체 중 최솟값 선택
    for i in range(1, a_len + 1):
        for j in range(1, b_len + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1  # 문자가 다르면 cost = 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,      # 삭제
                matrix[i][j - 1] + 1,      # 삽입
                matrix[i - 1][j - 1] + cost  # 교체
            )
    return matrix[a_len][b_len]  # 최종 거리 반환

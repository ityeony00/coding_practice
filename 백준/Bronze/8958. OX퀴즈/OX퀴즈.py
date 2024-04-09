for _ in range(int(input())):
    # 변수 초기화
    con = 0  # 연속수
    total = 0  # 전체점수
    # Get records
    ox_record = input().strip()
    # ox_record for문으로 돌기
    for ox in ox_record:
        # O일때
        if ox == "O":
            con += 1
        # X일때
        else:
            con = 0
        total += con
    print(total)

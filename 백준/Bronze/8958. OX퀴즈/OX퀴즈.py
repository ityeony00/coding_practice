point = 0
con = 0
sum = 0
for _ in range(int(input())):
    # Get records
    ox_record = input().strip()
    for i in range(len(ox_record)):
        if ox_record[i] == "O":
            point += 1
            con += 1
        else:
            point = 0
        sum = sum + point
    print(sum)
    point = 0
    con = 0
    sum = 0

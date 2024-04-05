# 첫 번째 줄 입력 받기
N, X = map(int, input().split())
# 두 번째 줄 입력 받기
A = list(map(int, input().split()))

#for문으로 X보다 작은 값 출력
for i in A:
    if i < X:
        print(i, end=" ")

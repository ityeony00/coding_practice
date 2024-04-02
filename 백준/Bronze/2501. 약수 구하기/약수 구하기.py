# input, map 사용하여 N, K 할당
N, K = map(int, input().split())

# 리스트 생성
yaksu_list = []
# for문을 통해 1부터 N까지 약수 찾아서 빈 yaksu 리스트에 append로 추가
for i in range(1, N + 1):
    # N 을 i로 나눴을 때 0일 때:
    if N % i == 0:
        # yaksu리스트에 i를 append
        yaksu_list.append(i)

# yaksu_list 원소의 개수가 K보다 크거나 같을 때
if len(yaksu_list) >= K:
    # yaksu_list의 k번째 작은 수 출력
    print(yaksu_list[K - 1])
else:
    # 0출력
    print(0)

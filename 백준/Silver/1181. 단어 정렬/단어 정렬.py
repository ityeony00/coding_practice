import sys

# 입력 받기
list_word = [sys.stdin.readline().strip() for _ in range(int(input()))]
list_word = list(set(list_word))
# sort_list
list_word.sort(key=lambda x: (len(x), x))
# print(sort_list)

for word in list_word:
    print(word)
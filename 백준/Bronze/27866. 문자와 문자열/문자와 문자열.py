import sys

# 입력 받기
word = sys.stdin.readline().strip()
idx = int(sys.stdin.readline())
print(word[idx - 1])
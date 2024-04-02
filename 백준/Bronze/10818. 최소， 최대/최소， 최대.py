import sys

input = sys.stdin.readline
num_ints = int(input())
numbers = list(map(int, input().split()))

print(min(numbers), max(numbers))

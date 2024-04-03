
five_numbers = list(map(int, input().split()))
jegob = []
for num in five_numbers:
    jegob.append(num**2)

print(sum(jegob) % 10)

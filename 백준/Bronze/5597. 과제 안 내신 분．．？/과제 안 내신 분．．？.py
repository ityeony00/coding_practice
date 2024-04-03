hw_students = set()
# 28명의 학생 번호를 입력 받음
for i in range(28):
    number = int(input())
    hw_students.add(number)

all_students = set()
for i in range(1, 31):
    # set에서는 append가 아닌 add를 씀
    all_students.add(i)

# all_students set에 담기 <-이 방법이 더 간단함
all_students = set(range(1, 31))

no_hw_students = all_students - hw_students

# print(no_hw_students)

for i in sorted(no_hw_students):
    print(i)

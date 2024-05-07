def solution(s):
    str = s.lower()
    print(str)
    if str.count('p') == str.count('y'):
        return True
    else:
        return False
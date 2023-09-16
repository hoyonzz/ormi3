"""
문자열 관련 함수
문자열 자료형은 자체적으로 함수를 가지고 있다. 이들 함수를 다른 말로 문자열 내장 함수라 한다.
이 내장 함수를 사용하려면 문자열 변수 이름 뒤에 '.'를 붙인 다음에 한수 이름을 써주면 된다.
"""

# 문자 개수 세기 (count)
a = 'hobby'
print(a.count('b'))

# 위치 알려주기 1(find)
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))
# 문자열 중 문자 b가 처음으로 나온 위치를 반환한다. 만약 찾는 문자나 문자열이 존재하지 않는다면
# -1을 반환한다.
print(a.find('z'))

# 위치 알려주기 2(index)
a = "Life is too short"
print(a.index('t'))
# print(a.index('k'))
# 앞의 find함수와 다른 점은 문자열 안에 존재하지 않는 문자를 찾으면 오류가 발생한다는 점이다.

# 문자열 삽입(join)
print(','.join('abcd'))
print(','.join(['a', 'b', 'c', 'd']))

# 소문자를 대문자로 바꾸기(upper)
a = 'hi'
print(a.upper())

# 대문자를 소문자로 바꾸기(lower)
a = "HI"
print(a.lower())

# 왼쪽 공백 지우기(lstrip)
a = "   hi"
print(a.lstrip())

# 오른쪽 공백 지우기(rstrip)
a = "hi     "
print(a.rstrip())

# 양쪽 공백 지우기(strip)
a = "   hi   "
print(a.strip())

# 문자열 바꾸기(replace)
a = "Life is too short"
print(a)
print(a.replace("Life", "Your leg"))
print(a)
# a변수를 변경하는 것은 아님!

# 문자열 나누기(split)
a = "Life is too short"
print(a.split())
print(a)
b = "a:b:c:d"
print(b)
print(b.split(':'))
# split함수는 아무 값도 넣어 주지 않으면 공백을 기준으로 문자열을 나누어준다.

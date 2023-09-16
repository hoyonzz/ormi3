# # 방금 배운 연산자를 사용해서 숫자 14를 3으로 나누었을 때, 몫과 나머지를 확인해보자.
# print(14//3, 14%3)

# # 줄을 바꾸는 이스케이프 코드 '\n'삽입하기
# multiline = "Life is too short\nYou need python"
# line = "Life is too short You need python"
# print(multiline)
# print(line)

# # 이스케이프 코드: 문자열 예제에서 여러 줄의 문장을 처리할 때, 백슬래시 문자와 소문자 n을 조합한 '\n' 이스케이프 코드를 사용했다.
# # 이스케이프 코드란 프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 '문자 조합'이다. 주로 출력물을 보기 좋게 정렬하는 용도로 사용한다.
# print('\\n : 문자열 안에서 줄을 바꿀 때 사용')
# print('\\t : 문자열 안에서 탭 간격을 줄 때 사용')
# print('\\ : 문자 \를 그대로 표현할 때 사용')
# print("\\' : 작은따옴표(')를 그대로 표현할 때 사용")
# print('\\" : 큰따옴표(")를 그대로 표현할 때 사용')

# 문자열 더해서 연결하기(Concatenation)
# head = "python"
# tail = " is fun!"
# print(head+tail)

# # 문자열 곱하기
# a = "python"
# print(a * 2)

# # 문자열 곱하기 응용
# print('=' * 50)
# print("my Program")
# print('=' * 50)

# # 문자열 길이 구하기
# a = "Life is too short"
# print(len(a))

"""
문자열 인덱싱과 슬라이싱
indexing이란 무엇인가를 '가리킨다'는 의미이고, slicing은 무엇인가를 '잘라낸다'는 의미이다.
"""

# # 문자열 인덱싱
# a = "Life is too short, You need Python"
# print(a[3])
# # 파이썬은 0부터 숫자를 센다.
# print(a[-1])
# print(a[-0])

# b = a[0] + a[1] + a[2] + a[3]
# print(b)
# b1 = a[0:4]
# print(b1)
# print(a[19:])
# print(a[:])

# 슬라이싱으로 문자열 나누기
# a = "20010331Rainy"
# date = a[:8]
# weather = a[8:]
# print(date)
# print(weather)

# a = "20010331Rainy"
# year = a[:4]
# print(year)
# day = a[4:8]
# print(day)
# weather = a[8:]
# print(weather)

# # f문자열 포매팅
# name = '홍길동'
# age = 30
# print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
# print(f'나는 내년이면 {age+1}살이 된다.')

# # 왼쪽 정렬
# print(f'{"hi":<10}')
# # 오른쪽 정렬
# print(f'{"hi":>10}')
# # 가운데 정렬
# print(f'{"hi":^10}')

# # 공백 채우기
# print(f'{"hi":=^10}')
# print(f'{"hi":!<10}')

# 소수점 표현
# y = 3.42134234
# print(f'{y:0.4f}')
# # 소수점 4자리까지 표현하고 자릿수를 10으로 맞춤
# print(f'{y:10.4f}')

# 연습문제: format 함수 또는 f 문자열 포매팅을 사용해 '!!!python!!!' 문자열을 출력해 보자.
print(f'{"python":!^12}')
# 리스트 관련 함수

# 리스트에 요소 추가(append)
a = [1,2,3]
print('a =', a)
a.append(4)
print(a)

a.append([5,6])
print(a)

# 리스트 정렬(sort)
a = [4,2,1,2,3]
print(a)
a.sort()
print(a)
a = ['a', 'c', 'b']
print(a)
a.sort()
print(a)

# 리스트 뒤집기(reverse)
a = ['a', 'c', 'b']
print(a)
a.reverse()
print(a)

# 위치반환(index)
a = [1,2,3]
print(a.index(3))
print(a.index(1))
# 존재하지 않는 값을 넣을 경우 오류 발생

# 리스트에 요소 삽입(insert)
a = [1,2,3]
print(a)
a.insert(0, 4)
print(a)
a.insert(3, 5)
print(a)

# 리스트 요소 제거(remove)
a = [1,2,3,1,2,3]
print(a)
a.remove(3)
print(a)

# 리스트 요소 끄집어내기(pop)
a = [1,2,3]
print(a.pop())
print(a)

a = [1,2,3]
a.pop(1)

# 리스트에 포함된 요소 X의 개수 세기(COUNT)
a = [1,2,3,1]
a.count(1)

# 리스트 확장(extend)
a = [1,2,3]
a.extend([4,5])
print(a)
# a.extend(4,5)
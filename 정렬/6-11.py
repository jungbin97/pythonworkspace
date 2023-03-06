# -------------------------------------------
#  [이코테]성적이 낮은 순서로 학생 출력하기
# -------------------------------------------

# 리스트에서 성적 값 반환 함수
# def setting(student):
#     return student[1]

# # 학생 수 입력받기
# count = int(input())

# student = [input().split() for _ in range(count)]


# result = sorted(student, key=setting)

# 정렬이 수행된 리스트 출력
# for i in range(count):
#     print(result[i][0], end=" ")

# for student in result:
#     print(student[0], end =" ")
# -------------------------------------------
#  교재 풀이
# -------------------------------------------

count = int(input())

# 학생정보를 입력받아 리스트에 저장
arr = []
for i in range(count):
    input_data = input().split()
    #이름은 그대로, 점수는 int 형으로 변환
    arr.append((input_data[0], int(input_data[1])))
    
# 키(key)를 이용하여, 점수를 기준으로 정렬
arr = sorted(arr, key=lambda student: student[1])

# 정렬이 수행된 결과 출력
for student in arr:
    print(student[0], end=" ")
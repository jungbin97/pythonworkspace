def solution(n, m, section):
    count = 1
    start = section[0]

    for i in range(1, len(section)):
        if start + m - 1 < section[i]:
            count += 1
            start = section[i]
    
    return count

print(solution(8, 4, [2,3,6]))
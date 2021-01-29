def rotate(matrix):
    tr = 0
    tc = 0
    dr = len(matrix)-1
    dc = len(matrix)-1
    while tr<dr:
        while tc < dc:
            for i in range(dc-tc):
                tmp = matrix[tr][tc+i]
                matrix[tr][tc+i] = matrix[dr-i][tc]
                matrix[dr-i][tc] = matrix[dr][dc-i]
                matrix[dr][dc-i] = matrix[tr+i][dc]
                matrix[tr+i][dc] = tmp
            tr += 1
            tc += 1
            dr -= 1
            dc -= 1
    return matrix


if __name__ == '__main__':
    a = [
        [1, 2, 3,1],
        [4, 5, 6,1],
        [7, 8, 9,1],
        [7, 8, 10,1]
        ]
    print(rotate(a))
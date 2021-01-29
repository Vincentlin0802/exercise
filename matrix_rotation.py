def rotate(matrix):     #顺时针旋转90度
    #找到整个矩阵的左上角和右下角的两个数
    tr = 0
    tc = 0
    dr = len(matrix)-1
    dc = len(matrix)-1
    while tr<dr:
        while tc < dc: #这个循环用来判断有几圈需要转（先转外圈在继续转里面的内圈，一圈一圈转）
            for i in range(dc-tc): #抓取每一圈的四个边角，然后依次找到位置进行换位
                tmp = matrix[tr][tc+i]
                matrix[tr][tc+i] = matrix[dr-i][tc]
                matrix[dr-i][tc] = matrix[dr][dc-i]
                matrix[dr][dc-i] = matrix[tr+i][dc]
                matrix[tr+i][dc] = tmp
            #外圈转完了之后 到了内圈 要把坐标改变一下
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
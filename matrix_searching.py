def searching(matrix, num):
    #从整个矩阵的右上角开始遍历到左下角
    tr = 0
    dc = len(matrix) - 1
    while(dc >0 and tr<len(matrix)): #边界
        pivot = matrix[tr][dc] #矩阵右上角的数字
        if(num>pivot):   #将要找的数字和右上角的数字进行比较
            tr += 1
        elif(num<pivot):
            dc -= 1
        elif(num==pivot):
            print("True")
            break
    if(dc<0 or tr>len(matrix)-1): #如果越界了，就代表不在矩阵中
        print("False")


if __name__ == '__main__':
    a = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
        ]

    searching(a,3)
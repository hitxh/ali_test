
import numpy as np
import string
'''
m = int(input("请输入矩阵的行数m:  "))
n = int(input("请输入矩阵的列数n:  "))

# A = np.zeros((m, n), dtype=int)    # 不使用这个方法

A = [[0]*m] * n     # 使用这个方法创建数组  因为我要用index方法  当然还有别的解决途径
print("输入0-1矩阵")                        
for i in range(m):                       # 使用这个方法赋初值
    A[i] = input().split(' ')
print(A)
'''
A  =  [[1, 1, 0,1, 1, 0, 0],\
        [1, 0, 1, 1, 0, 0, 1],\
        [1, 1, 1,1, 1, 1, 1],\
        [0, 1, 0,1, 0, 1, 1],\
        [1, 0, 1,1, 1, 1, 0],\
        [1, 1, 0,1, 1, 0, 1]]
# A = np.array(A)    np没有index  但是np也有好多操作
# [x[y] for x in A]  读取A的第y列
# [x[y] for x in A][m1:m2]  读取A的第y列  m1到m2行  不包括第m2行
print(np.array(A))       # 以矩阵形式打印在屏幕上
m = len(A)
n = len(A[0])
A_num = np.zeros((m, n))
max_num = 0
print("行数  ", m)
print("列数  ", n)
for i in range(m):
    for j in range(n):
        if A[i][j]!=0:
            try:
                A_right = A[i][j:].index(0)                     # 取四个方向
            except:
                A_right = len(A[i][j:])
            try:
                A_left  = A[i][j::-1].index(0)
            except:
                A_left = len(A[i][j::-1])
            try:
                A_up    = [x[j] for x in A][i::-1].index(0)
            except:
                A_up = len([x[j] for x in A][i::-1])
            try:
                A_down  = [x[j] for x in A][i:].index(0)
            except:
                A_down = len([x[j] for x in A][i:])
            A_num[i][j] = A_right + A_left + A_up + A_down - 3


max_num = np.max(np.max(A_num))     # 因为A_num是numpy类型

c = np.where(A_num == max_num)

c = c + np.ones((len(c), len(c[0])))
print("目标点位置  \n", c)
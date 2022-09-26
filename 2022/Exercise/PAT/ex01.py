"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/12
Description: 螺旋矩阵
思路：
计算m*n的矩阵，然后排列顺序并填充，
思路一：按一层一层来写，先上右下左
思路二：逐个元素填充，遇到边界转换方向
疑问：不知道为什么按口字型填充老是失败
"""


def factorization(N):
    iter = int(N**0.5)
    for i in range(iter, 0, -1):
        if N % i == 0:
            return N // i, i


def main():
    N = int(input())
    input_list = list(map(int, input().split()))
    input_list.sort(reverse=True)
    m, n = factorization(N)
    top, right, bottom, left = 0, n - 1, m - 1, 0
    result_list = [[0 for i in range(n)] for i in range(m)]
    for i in range(N):
        
    for t in range(m):
        print(' '.join(list(map(str, result_list[t]))))


main()
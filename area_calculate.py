#coding=utf-8
# 计算图像文件 '正方形面积占比计算.JPG'中粉红色区域占总正方形面积的比例

# 思路：蒙特卡洛算方法：
# 假设正方形边长为1
# 以正方形的左下角定点为直角坐标系圆点，记圆点为A（0，0）
# 正方形右下角的点为B（1，0）
# 正方形左上角的点为C（0，1）
# 正方形上面的那条边的中点为D（0.5,1）
# 记AD与BC两线的交点，即为粉红色三角形的定点为P
# 直线AD的方程式为 y = 2*x
# 直线BC的方程为   y = 1-x
# 粉红的区域的可行域为满足 y < 2*x 且 y < 1-x 且 y >0，其中x的范围为 0～1
# 正方形区域的可行域为 0<x<1;0<y<1

import numpy as np
import matplotlib.pyplot as plt

def meng_num(n):
    col_X=[]; col_y=[]
    z=np.zeros(n)
    sum=0                       # 程序刚开始的时候，没有点落入粉红色区域的可行域
    for i in range(n):
        x=np.random.rand()      # 随机生成一个值为0～1的数即记为x坐标
        y=np.random.rand()      # 随机生成一个值为0～1的数即记为y坐标
        col_X.append(x)         # 收集生成的x，留着作图用
        col_y.append(y)         # 收集生成的y，留着作图用
        if y<2*x and y < 1-x:   # 若坐标（x，y）落入粉红区域,则进行计数
            sum +=1
            z[i]=1
    area_rate=sum/len(range(n+1))   # 则粉红色区域所占正方形的概率为落入粉红色区域的点数除以总生成的随机数n
    print('当随机生成 %i 个点的时候，面积占比为： %f ' %(n,area_rate))

    #以下是可视化输出，只是把生成的点投影到区域中
    x1 = np.linspace(0, 1 / 3, 1000)
    x2 = np.linspace(1 / 3, 1, 1000)
    x3 = np.linspace(0, 1, 1000)
    y1 = 2 * x1
    y2 = 1 - x2
    y3 = 0 * x1
    plt.plot(x1, y1, x2, y2, x3, y3)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.scatter(col_X,col_y,c=z,cmap='rainbow')
    plt.title('when create %i random point' %n)
    plt.show()


for n in list([10,100,1000,10000,100000]):
    meng_num(n)

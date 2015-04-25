#encoding=utf-8

import sys
 
f = open('trainingset.txt','r')
list = f.readlines()
m = len(list)
x1 = []
x2 = []
y = []
for i in range(m):
    list[i] = list[i].strip().split(",")
    x1.append(int(list[i][0]))
    x2.append(int(list[i][1]))
    y.append(int(list[i][2]))
 
epsilon = 0.0001
#learning rate

alpha = input('Please input an alpha(0.0000003049~0.00000030491,the best tested alpha:0.0000003049024): ')

diff = [0,0]
max_itor = 1000
error1 = 0
error0 = 0
cnt = 0
 
#把参数初始化
theta0 = 0
theta1 = 0
theta2 = 0
 
while True:
     
    cnt = cnt + 1
 
    #计算参数
    for i in range(m):
 
        diff[0] = y[i] - (theta0 + theta1 * x1[i] + theta2 * x2[i])
         
        theta0 = theta0 + alpha * diff[0] * 1
        theta1 = theta1 + alpha * diff[0] * x1[i]
        theta2 = theta2 + alpha * diff[0] * x2[i]
 
    #计算cost function
    error1 = 0
    for lp in range(m):
        error1 += (y[i] - (theta0 + theta1 * x1[i] + theta2 * x2[i]))**2 / 2
     
    if abs(error1-error0) < epsilon:
        break
    else:
        error0 = error1
 
    print 'theta0 : %f, theta1 : %f, theta2 : %f, error1 : %f' % (theta0, theta1, theta2, error1)
 
print 'Done: theta0 : %f, theta1 : %f, theta2 : %f' % (theta0, theta1, theta2)

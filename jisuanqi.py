'''
Author: 榜哥
Date: 2022-12-09 22:21:55
LastEditors: Please set LastEditors
LastEditTime: 2022-12-17 15:32:21
FilePath: \vs\py\a.py
Description: QQ:2104864320 
Copyright (c) 2022 by 榜哥 email: Zzb090317@outlook.com , All Rights Reserved.
'''
import math
def sswr(num):  # sourcery skip: extract-duplicate-method, hoist-similar-statement-from-if, hoist-statement-from-if, remove-pass-body-from-if, remove-pass-body
    yw  = int(input('精度'))#精确到10的n次方
    b = 10**yw
    if b > num:
        print('叫神仙来')  #委婉出错
    else:      
        c = 1/ b#向左移x位
        num *= c
        a = num - math.trunc(num)#看后面小数
        if a <0.5: #小5省略
            num = math.trunc(num)
            print(num*b)#还原
            v= str(num)
            r = list(v)#有效数字
            s = len(r)
            print('有效数字共有%d个'%s)
        else:
            num +=1 #大五进一
            num = math.trunc(num)
            print(num*b)  # 还原
            v = str(num)
            r = list(v)  # 有效数字
            s = len(r)
            print('有效数字共有%d个'% s)


def equ(a, b, n):  
    if n == 1:
        print(a+b)
    elif n == 2:
        print(a-b)
    elif n == 3:
        print(a*b)
    elif n == 4:
        print(a/b)
    elif n == 5:
        print(a**b)
    elif n == 6:
        print(a//b)
    elif n == 7:
        print(a % b)
    elif n == 8:
        g = int(a)
        h = int(b)
        e = math.factorial(g)
        f = math.factorial(h)
        print(e, f)
    elif n == 9:
        e = math.fabs(a)
        f = math.fabs(b)
        print(e, f)
    elif n == 10:
        e = math.trunc(a)
        f = math.trunc(b)
        print(e, f)
    elif n == 11:
        sswr(a)
        sswr(b)


# sourcery skip: merge-comparisons
f = ['1加', '2减', '3乘', '4除', '5n次方', '6整除','7取余', '8阶乘(两个数单独计算)', '9绝对值(两个数单独计算)','10简单粗暴删除小数','11四舍五入']
while True:
    c = input('按回车键继续,打出q退出(值太大会崩溃)')
    if c == 'q' or c == 'Q':
        exit()
    elif c == '':
        a = float(input('a = '))
        b = float(input('b = '))
        print('请选择运算,如:')
        for i in f:
            print(i)
        n = int(input())
        equ(a, b, n)
    else:
        print('这个BUG被简单粗暴地修复了(狗头)')#作者患了脑血栓,搞出了沙雕设计
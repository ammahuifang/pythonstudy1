#作业1：编写一个函数，用递归的方法输出斐波那契额(Fibonacci sequence)数列list
'''
递归函数
在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
举个例子，我们来计算阶乘 n! = 1 * 2 * 3 * ... * n，用函数 fact(n)表示，可以看出：
fact(n) = n! = 1 * 2 * 3 * ... * (n-1) * n = (n-1)! * n = fact(n-1) * n
所以，fact(n)可以表示为 n * fact(n-1)，只有n=1时需要特殊处理。
于是，fact(n)用递归的方式写出来就是：


def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
'''

x=int(input("输入一个数："))
def fib(n):   
    if n==0:
        return 0
    if n==1:
        return 1    
    return fib(n-1)+fib(n-2)
for i in range(1,x+1):
    print(fib(i))


'''
输入一个数：6
1
1
2
3
5
8
'''

#作业3：用埃拉托色尼筛输出0-n的质数的list
'''
埃拉托色尼筛选法(the Sieve of Eratosthenes)简称埃氏筛法，
是古希腊数学家埃拉托色尼(Eratosthenes 274B.C.～194B.C.)提出的一种筛选法。
是针对自然数列中的自然数而实施的，用于求一定范围内的质数，它的容斥原理之完备性条件是p=H~。
'''

def _int_iter():
    n=1
    while True:
        n=n+1
        yield n
def _not_divisible(n):
    return lambda x:x%n>0

def primes():
    it=_int_iter()
    while True:
    

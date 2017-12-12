#洗衣程序
print('lever :h,l')
lever = input()
if lever == 'h':
    print('注水50L')
    print('搅拌60min')
    print('放水')
elif lever == 'l':
     print('注水20L')
     print('搅拌30min')
     print('放水')
#甩干程序
print('输入甩干次数')
times = int(input())
for i in range(times):
    print('注水20L')
    print('搅拌20min')
    print('放水')

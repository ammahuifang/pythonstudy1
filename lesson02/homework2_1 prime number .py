# find the prime number from 1 to 100


num=1
p_num=1 
while num<100:
    div_num=2
    num+=1
    while div_num<num:
        if num%div_num==0:
            break
        div_num+=1
    else:
        p_num+=1
        print(p_num,num)
        

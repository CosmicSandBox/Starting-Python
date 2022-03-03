##브라질학과/201901032/김재우

import random

a=0
e=''
while a<5:
    import random
    numbers=[]
    for num in range(0,2,1):
        numbers.append(random.randrange(0,100,1))

    print(str(numbers[0])+'+'+str(numbers[1])+'=', end='')
    q=int(input())
    print(q)

    if q==numbers[0]+numbers[1]:
        print('정답입니다.')
        e+='ㅇ'
    else:
        print('오답입니다.')

    a+=1

print('5문제 중'+str(e.count('ㅇ'))+'문제를 맞췄습니다.')
print('당신의 점수는'+str(20*e.count('ㅇ'))+'점입니다.')

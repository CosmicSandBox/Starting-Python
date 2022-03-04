#브라질학과/201901032/김재우

hap=0


for i in range(105,151,7):
    if i%7==0:
        hap=hap+i
        print('%d  '%i, end='  ')


print('\n100부터 150까지의 정수 중에서 7의 배수들의 합계:%d' %hap)

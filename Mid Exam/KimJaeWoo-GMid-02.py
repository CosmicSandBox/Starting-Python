#브라질학과/201901032/김재우

a=float(input('실수1 입력:'))
b=float(input('실수2 입력:'))

plus=a+b
minus=a-b
times=a*b
divide=a/b


print('{0:5.2f} + {1:5.2f} ={2:9.2f}'.format(a, b, plus))
print('{0:5.2f} - {1:5.2f} ={2:9.2f}'.format(a, b, minus))
print('{0:5.2f} * {1:5.2f} ={2:9.2f}'.format(a, b, times))
print('{0:5.2f} / {1:5.2f} ={2:9.2f}'.format(a, b, divide))

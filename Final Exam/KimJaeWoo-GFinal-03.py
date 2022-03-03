##브라질학과/201901032/김재우

a=int(input('1차 점수 입력:'))
b=int(input('2차 점수 입력:'))
c=int(input('3차 점수 입력:'))
d=int(input('4차 점수 입력:'))

print('1차 점수:'+str(a))
print('2차 점수:'+str(b))
print('3차 점수:'+str(c))
print('4차 점수:'+str(d))
print('------------------')
print('총점 :'+str(a+b+c+d))
q=(a*1/10+b*2/10+c*3/10+d*4/10)
print('평균 : %d'%q)

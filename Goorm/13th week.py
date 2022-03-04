a=int(input('투자 액수를 입력하세요: '))
b=int(input('투자한 날짜 수를 입력하세요: '))

total=10000
total=a

if a>=100 and a<=10000 and b>=1 and b<=10:
   for i in range(1,b+1):
      change= int(input('%d일차 변동 데이터를 입력하세요:' %i ))
      for j in range(i,i+1):
         total+=total*(change/100)

ben= total - a
print("%d" %ben)

if ben > 0:
   print('이득입니다.')
elif ben==0:
   print('본전입니다.')
elif ben<0:
   print('손해입니다.')
##브라질학과/201901032/김재우

#함수선언부분
def scorealpha(a):
    if a>=90:
        print('당신의 점수:%d'%a)
        print('당신의 학점:A')
    elif a>=80:
        print('당신의 정수:%d'%a)
        print('당신의 학점:B')
    elif a>=70:
        print('당신의 점수:%d'%a)
        print('당신의 학점:C')
    elif a>=60:
        print('당신의 점수:%d'%a)
        print('당신의 학점:D')
    else:
        print('당신의 점수:%d'%a)
        print('당신의 학점:F')
#메인코드부분
while True:
    n=int(input('점수 입력:'))
    scorealpha(n)
    print('')


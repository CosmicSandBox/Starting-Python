##브라질학과/201901032/김재우##

dic={'B4':'Before','TX':'Thanks','BBL':'Be Back Later', 'BCNU':'Be Seeing You', 'HAND':'Have A Nice Day'}

for i in range(0,5,1):
    a=input('번역할 문장을 입력하시오:')
    if a=='B4':
        print(dic.get('B4'))
    elif a=='TX':
        print(dic.get('TX'))
    elif a=='BBL':
        print(dic.get('BBL'))
    elif a=='BCNU':
        print(dic.get('BCNU'))
    elif a=='HAND':
        print(dic.get('HAND'))

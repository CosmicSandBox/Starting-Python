##브라질학과/201901032/김재우

s1='Kang Young Min'
s2='Kang Young-Min'
s3='Park Dong Min'
s4='Park Dong=Yun'

#s1
a=s1
b=''
for i in range(0, len(a)):
    if a[i]!=' 'and a[i]!='-'and a[i]!='=':
        b+=a[i]
print(a+'(은)는'+b.upper()+'(으)로 수정됨')
e=b.upper()
#s2
a=s2
b=''
for i in range(0, len(a)):
    if a[i]!=' 'and a[i]!='-'and a[i]!='=':
        b+=a[i]
print(a+'(은)는'+b.upper()+'(으)로 수정됨')
f=b.upper()
#s3
a=s3
b=''
for i in range(0, len(a)):
    if a[i]!=' 'and a[i]!='-'and a[i]!='=':
        b+=a[i]
print(a+'(은)는'+b.upper()+'(으)로 수정됨')
g=b.upper()
#s4
a=s4
b=''
for i in range(0, len(a)):
    if a[i]!=' 'and a[i]!='-'and a[i]!='=':
        b+=a[i]
print(a+'(은)는'+b.upper()+'(으)로 수정됨')
h=b.upper()
#N의 갯수
print(e+' : '+str(e.count('N'))+'개의 N이 나타남')
print(f+' : '+str(f.count('N'))+'개의 N이 나타남')
print(g+' : '+str(g.count('N'))+'개의 N이 나타남')
print(h+' : '+str(h.count('N'))+'개의 N이 나타남')

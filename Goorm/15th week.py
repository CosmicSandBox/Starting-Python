def del_sign(origin):
   data = origin.replace('.',' ')
   data = data.replace(',',' ')
   data = data.replace('-',' ')
   data = data.replace('"',' ')
   data = data.replace("'",' ')
   data = data.replace('\ufeff',' ')
   data = data.replace('\n',' ')
   ver1 = data.split(' ')
   return ver1

def find_standard(origin):
   set_temp= set(origin)
   set_temp.remove('')
   standard= list(set_temp)
   print('사용된 단어 개수는 총 %d개입니다.' %len(standard))
   return standard

def analysis(origin,standard):
   for i in standard:
      count=0
      for j in origin:
         if i==j:
            count +=1
      print('%15s=%5d번' %(i, count))

f=open('data/Rapunzel.txt', 'r')
all= f.read()
f.close()

rapunzel =del_sign(all)
new_standard=find_standard(rapunzel)
result =analysis(rapunzel, new_standard)

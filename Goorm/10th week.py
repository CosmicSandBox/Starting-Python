answer = str(input())

total = 0
current = 1

for i in answer :
   if i=='O':
      total+=current
      current+=1
      
   elif i=='X':
      current=1
         
   
print(total)
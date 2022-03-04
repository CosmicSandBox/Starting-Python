start_day = 2  # Tuesday
last_day = 31

print('\tS\tM\tT\tW\tT\tF\tS')
for i in range(2) :
   print('\t', end='')
for i in range(1,32) :
   if i%7!=5 :
      print('\t%d' %i, end='')
   elif i%7==5:
      print('\t%d\n' %i)
	
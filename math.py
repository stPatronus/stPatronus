num = 1
while num * 2 != int(str(num)[-1:] + str(num)[:len(str(num))-1]):
  print(str(num) + " " + str(num*2))


    
  num += 1

#105263157892736742#

print(str(num) +" is the lowest number." )
input()

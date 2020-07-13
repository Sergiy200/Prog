#Task1
v_array = [3, 6, 10, 15, 18, 20, 22, 27, 31, 34, 36, 40, 45, 47, 44, 41, 49, 50]



sum = 0
for element in v_array:
 if element % 2 == 0:
  sum+=element
print(sum)

#Task2
import random
M = 10
N = 5
a = []
elm = 0
max_element = 0
for i in range(N):
    b = []
    for j in range(M):
        elm = random.randint(1,100)
        b.append(elm)
        print("%3d" % b[j], end='')
        if max_element < elm:
             max_element = elm  
    a.append(b)
    print() 
print (max_element)

col = 0
for i in range(M):
    s = 0
    for j in range(N):
                  if max_element == a[j][i]:
                           col = i
print (col)
array_help = []
if col != M-1:
 for j in range(0,N): 
   array_help.append(a[j][col])
   a[j][col] = a[j][M-1]
   a[j][M-1] = array_help[j]
for i in range(N): 
 for j in range(M):
  print("%3d" % a[i][j], end='')
 print()

 

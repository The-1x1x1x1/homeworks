import random

p=[0,0,0,0,0,0,0,0]
for x in range(8):
    p[x]=random.randint(48,122) 
    p[x]=chr(p[x])
print(str(p))
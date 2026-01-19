squa=[]
odd=[]
even=[]
for x in range(10):
    sq=x*x
    squa.append(sq)
    if sq%2==0:
        even.append(sq)
    else:
        odd.append(sq)

print(squa)
print(odd)
print(even)
l1=[1,2,3,4,5,6,7,8,9,10]
even=[x for x in l1 if x%2==0]
odd=[x for x in l1 if x%2==1]
print("even nums in list: ",even)
print("odd nums in list: ",odd)

di={1,2,3,4,5}
sq={x*x for x in di}
print(sq)

d={str(x): x**2 for x in [1,2,3,4,5,6]}
print(d)
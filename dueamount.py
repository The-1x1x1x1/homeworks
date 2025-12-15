def dues(b,p):
    due=b-p
    return max(due,0)

bill=int(input("enter bill: "))
pay=int(input("enter pay: "))
a=dues(bill,pay)
print("dues: ",a)
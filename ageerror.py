try:
    age=int(input("enter age: "))
    if age<0:
        raise ValueError("Age.cannot.be.negative.")
    if age%2==0:
        print("age is even")
    else:
        print("age is odd")
except ValueError as ex:
    print("invalid age: ", ex )
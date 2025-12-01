def squa(l):
    area=l*l
    peri=l*4
    return area, peri

def rect(l,w):
    area=l*w
    peri=2*(l+w)
    return area, peri

def circ(r):
    area=3.14*(r**2)
    peri=2*3.14*r
    return area, peri

choice=input("a. square or b. rectangle or c. circle (a/b/c): ")

if choice=="a":
    n=int(input("enter length: "))
    print("area and perimeter= " ,squa(n))
elif choice=="b":
    n1=int(input("enter length: "))
    n2=int(input("enter width: "))
    print("area and perimeter= ", rect(n1,n2))
elif choice=="c":
    n=int(input("enter radius: "))
    print("area and circumference= ", circ(n))
dec = int(input("enter number to convert: "))
bina = ""

if dec == 0:
    bina = "0"
else:
    while dec > 0:
        remain = dec % 2 
        bina = str(remain) + bina  
        dec = dec // 2  
print(bina)
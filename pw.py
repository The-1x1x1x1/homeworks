import string
import random

l=int(input("enter password length: "))
cha=string.ascii_letters+string.digits

pw=''
for i in range(l):
    pw+=random.choice(cha)

pw2=list(pw)
random.shuffle(pw2)
pw=''.join(pw2)

print("generated password: ",pw)
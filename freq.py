thing={'1x1x1x1':1,'is':2,'the':1,"best":1,"hacker!":4}
K=1
res=0

for key in thing:
    if thing[key]==K:
        res+=1

print("freq. of K: ",res)
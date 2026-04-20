class Reverse:
    def __init__(self):
        self.str=input()
    def Rev(self):
        return self.str[::-1]
    
obj=Reverse()
print("reversed: ", obj.Rev())
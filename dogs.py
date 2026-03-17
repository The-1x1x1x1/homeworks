class dog:
    def __init__(self,breed,colour):
        self.breed=breed
        self.colour=colour
    
princess=dog("pitbull","mixed")
terminator=dog("golden labrador","yellow")
print("princess is a ",format(princess.colour),format(princess.breed))
print("TERMINATOR is a ",format(terminator.colour),format(terminator.breed))
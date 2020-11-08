class atom(object):
    def __init__(self,atno,x,y,z):
        self.atno = atno
        self.position = (x,y,z)
        # this is constructor
    def symbol(self): # a class method
        return atno__to__Symbol[atno]
    def __repr__(self): # a class method
        return '%d %10.4f %10.4f %10.4f%'
        (self.atno, self.position[0], self.position[1],
        self.position[2])
        # toString
        

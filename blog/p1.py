class myClass:
    def __init__(self,name,family):
        self.name=name
        self.family=family
    
    def __repr__(self):
        return f'name={self.name}'
    
    def __str__(self):
        return f'family={self.family}'
    
mc1=myClass('ali','mohammadi')

print(mc1)
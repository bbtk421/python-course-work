class robot:
    def __init__(self,make,model,name):
        self.make = make
        self.model = model
        self.name = name

class robotDoctor(robot):
    bedside = "Irreverant"
    instrument = "scalpel"
    

class robotConstruction(robot):
    personality = "I'm walkin here"
    tool = "drill"
  
        

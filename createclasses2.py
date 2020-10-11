class robot:
      name = ""
      make = ""
      model = ""

      def info(self):
            msg = "\nName: {}\nMake: {}\nModel: {}".format(self.name,self.make,self.model)
            return msg

class robotDoctor(robot):
      name = "D.O.C."
      make = "Mom's Friendly Robot Company"
      model = "Hawkeye"
      bedside_manner = "Irreverant"
      instrument = "scalpel"

      def docinfo(self):
            msg = "\nBedside Manner: {}\nInstrument: {}".format(self.bedside_manner,self.instrument)
            return msg

class robotConstruction(robot):
      name = "Jim"
      make = "Wernstrom Inc."
      model = "Goomba"
      personality = "I'm walkin' here"
      tool = "drill"

      def coninfo(self):
            msg = "\nPersonality: {}\nTool: {}".format(self.personality,self.tool)
            return msg
  
        
if __name__ == "__main__":
      doc = robotDoctor()
      print(doc.info())
      print(doc.docinfo())

      con = robotConstruction()
      print(con.info())
      print(con.coninfo())
      
      

class Private:
    def __init__(self):
        self.__privateVar = 20

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private 
        
obj = Private()
obj.getPrivate()
obj.setPrivate(21)
obj.getPrivate()
        
class Protecc:
    def __init__(self):
        self._protectedVar = 0
        
    def getProtecc(self):
        print(self._protectedVar)
        
    def setProtecc(self, protecc):
        self.__protectedVar = protecc
        

obj = Protecc()
obj.getProtecc()
obj.setProtecc(2)
obj.getProtecc()

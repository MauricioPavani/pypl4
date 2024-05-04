class PL4:
    def __init__(self, miscData, dfHEAD, data):
        self.miscData = miscData
        self.dfHEAD = dfHEAD
        self.data = data

    def getFromNode(self):
        from_node = [x for x in self.dfHEAD['FROM'] if not (x == '')]
        return from_node

    def getToNode(self):
        to_node = [x for x in self.dfHEAD['TO'] if not (x == '')]
        return to_node

    def getTypeSinal(self):
        type_signal = [x for x in self.dfHEAD['TYPE'] if not (x == '')]
        return type_signal

    def getDeltaTfromSimulation(self):
        ...

    def getDeltaTfromPlot(self):
        ...

    def getSteps(self):
        ...

    def getTmax(self):
        ...

    def _convertType(self):
        ...

    def getVarData(self):
        ...

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
        return self.miscData['deltat']

    def getDeltaTfromPlot(self):
        return self.data[:, 0][-1] / (
            self.miscData['steps'] - self.miscData['steps'] % 2
        )

    def getSteps(self):
        return self.miscData['steps']

    def getTmax(self):
        return self.data[:, 0][-1]

    def _convertType(self):
        ...

    def getVarData(self):
        ...

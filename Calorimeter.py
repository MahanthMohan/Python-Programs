class Calorimeter:

    def qsur(self,qrxn):
        self.qrxn = qrxn
        qsur = str(-1 * (self.qrxn)) + " kJ"
        return qsur

    def qrxn(self,ΔH):
        self.ΔH = ΔH
        qrxn = str(self.ΔH) + " kJ"
        return qrxn

    def enthalpy(self,m,c,θF,θI):
        self.m = m 
        self.c = c 
        self.θF = θF
        self.θI = θI
        θR = self.θF - self.θI
        enthalpy = self.m * self.c * θR
        return enthalpy

    def classifyrxn(self, enthalpy):
        self.enthalpy = enthalpy
        if(self.enthalpy > 0):
            return "Endothermic Reaction"
        else:
            return "Exothermic Reaction"

cal = Calorimeter()
command = str(input("Enter what you want to do (qsur, qrxn, enthalpy, classify reaction): "))
if(command == "qsur"):
    print(cal.qsur(qrxn = input("Enter the qrxn: ")))

elif(command == "qrxn"):
    print(cal.qrxn(ΔH = input("Enter the qrxn: ")))

elif(command == "enthalpy"):
    print(cal.enthalpy(m = input("Enter the mass of the sample(s): "), c = input("Enter the specific heat: "), θF = input("Enter the final temperature: "), θI = input("Enter the intial temperature: ")))

elif(command == "classify reaction"):
    print(cal.classifyrxn(enthalpy = input("Enter the enthalpy change: ")))
    

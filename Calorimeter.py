class Calorimeter:

    def enthalpy(self, products, reactants):
        self.products = products
        self.reactants = reactants
        enthalpy = "The enthalpy is " + str(products - reactants) + " kJ"
        return enthalpy

    def qsur(self,qrxn):
        self.qrxn = qrxn
        if(qrxn > 0):
            qsur = str(-1 * (qrxn)) + " kJ"
            return qsur
        else:
            qsur = str(-1 * qrxn) + " kJ"
            return qsur
        
    def qrxn(self,qsur):
        self.qsur = qsur
        if(qsur > 0):
            qrxn = str(-1.0 * qsur) + " kJ"
            return qrxn
        else:
            qrxn = str(-1.0 * qsur) + " kJ"
            return qrxn

    def HeatAbsorbed(self,m,c,θF,θI):
        self.m = m
        self.c = c
        self.θF = θF
        self.θI = θI
        θR = θF - θI
        enthalpy = str(m * c * θR) + " J"
        return enthalpy

    def classifyrxn(self, enthalpy):
        self.enthalpy = enthalpy
        if(enthalpy > 0):
            return "Endothermic Reaction"
        else:
            return "Exothermic Reaction"

    def net_enthalpy(self, r1, r2):
        self.r1 = r1
        self.r2 = r2
        enthalpy = "The net enthalpy is " + str(r1 + r2) + " kJ"
        return enthalpy


cal = Calorimeter()
command = str(input("Enter what you want to do (enthalpy, qsur, qrxn, heat absorbed, classify reaction, net enthalpy): "))
if(command == "enthalpy"):
    print(cal.enthalpy(products = float(input("Energy of the products: ")), reactants = float(input("Energy of the reactants: "))))

if(command == "qsur"):
    print(cal.qsur(qrxn =float(input("Enter the qrxn: "))))

elif(command == "qrxn"):
    print(cal.qrxn(qsur = float(input("Enter the qsur: "))))

elif(command == "heat absorbed"):
    print(cal.enthalpy(m = float(input("Enter the mass of the sample in g: ")), c = float(input("Enter the specific heat in J: ")), θF = float(input("Enter the final temperature: ")), θI = float(input("Enter the intial temperature: "))))

elif(command == "classify reaction"):
    print(cal.classifyrxn(enthalpy = float(input("Enter the enthalpy change: "))))

elif(command == "net enthalpy"):
    print(cal.net_enthalpy(r1 = float(input("Enthalpy change of reaction 1: ")), r2 = float(input("Enthalpy change of reaction 2: "))))

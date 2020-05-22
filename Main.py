
class Main:

    def getInput(self):
        lower_limit = int(input("Enter the lower value: "))
        upper_limit = int(input("Enter the upper value: "))
        array = [lower_limit,upper_limit]
        #print(array)
        return array

    def doThing(self,a,b):
        print (a,b)

Main = Main()

array = Main.getInput()
Main.doThing(array[0],array[1])



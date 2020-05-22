class WesternShowdown:

  def showdown(self, p1, p2):
    self.p1 = p1
    self.p2 = p2
    if p1.find("Bang!") < p2.find("Bang!"):
      print("p1 is the winner!")
    elif p1.find("Bang!") > p2.find("Bang!"):
      print("p2 is the winner!")
    else:
      print("tie")

p1 = str(input("Enter Bang! to shoot for player 1: "))
p2 = str(input("Enter Bang! to shoot for player 2: "))

showdown = WesternShowdown()

print("'" + p1 + "'")
print("'" + p2 + "'")
showdown.showdown(p1,p2)

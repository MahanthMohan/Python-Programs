def showdown(p1, p2):
 if p1.find("Bang!") < p2.find("Bang!"):
  print("p1")
 elif p1.find("Bang!") > p2.find("Bang!"):
  print("p2")
 else:
  print("tie")

p1 = str(input("Enter Bang! to shoot for player 1: "))
p2 = str(input("Enter Bang! to shoot for player 2: "))
showdown(p1,p2)
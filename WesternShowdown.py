def showdown(p1, p2):
 if p1.find("Bang!") < p2.find("Bang!"):
  print("→ p1")
  print("p1 draws his gun sooner than p2")
 elif p1.find("Bang!") > p2.find("Bang!"):
  print("→ p2")
  print("p2 draws his gun sooner than p1")
 elif p1.find("Bang!") == p2.find("Bang!"):
  print("→ tie")
  print("tie")
		
pl = str(input("Enter the word Bang! for p1: "))
p2 = str(input("Enter the word Bang! for p2: "))
print("\n" + p1)
print("\n" + p2)
showdown(p1,p2)

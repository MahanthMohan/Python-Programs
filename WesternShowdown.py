def showdown(p1, p2):
 if p1.find("Bang!") < p2.find("Bang!"):
  return("→ p1")
  return("p1 draws his gun sooner than p2")
 elif p1.find("Bang!") > p2.find("Bang!"):
  return("→ p2")
  return("p2 draws his gun sooner than p1")
 elif p1.find("Bang!") == p2.find("Bang!"):
  return("→ tie")
  return("tie")
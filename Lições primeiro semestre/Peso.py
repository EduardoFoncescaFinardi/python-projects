a = input("weight: ")
b = input("(K)g or (L)bs: ")
while str(b)!="K" and str(b)!="L":
  print("Error, type K ou L")
  b = input("(K)g or (L)bs: ")
if str(b) == "K":
  print("Your weight in Lbs is: ", float(a) * 2.2)
if str(b) == "L":
  print("Your weight in Kg is: ", float(a) / 2.2)
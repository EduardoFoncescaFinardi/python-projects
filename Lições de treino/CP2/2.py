n = int(input("N:"))
i = 1
soma = 0
soma2 = 0
while i <= n:
  print(f"loop {i}: soma {soma}")
  soma += i
  i += 1
  
print(soma)

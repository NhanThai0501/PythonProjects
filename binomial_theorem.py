def gt(n):
  if n < 2:
    return 1
  return n * gt(n - 1)

def C(n, k):
  return int(gt(n)/(gt(k) * gt(n - k)))

to_hop = lambda a: "" if a == 1 else str(a)

def pt(a, m):
  if m == 0:
    s = ""
  elif m == 1:
    s = a
  else:
    s = a + '^' + str(m)
    
  return s

def binomial_theorem_newton(a, b, n):
  s = []
  for k in range (n + 1):
    s.append(to_hop(C(n, k)) + pt(a, n - k) + pt(b, k))
  s1 = f"{a} + {b})^{n} = {' + '.join(s)}"
  return s1

number = int(input("Enter the binomial number that you want: "))
print(binomial_theorem_newton('a', 'b', number)) 
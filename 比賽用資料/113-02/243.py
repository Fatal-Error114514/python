eq = input()
eq1 = eq.replace("=","-(") + ")"
c = eval(eq1, {'X': 1j})
print(int(-c.real/c.imag))
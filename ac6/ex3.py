A ,B, C = input() .split()
D, E, F = input() .split()

A = int(A)
B = int(B)
C = float(C)
D = int(D)
E = int(E)
F = float(F)

valor_a_pagar = (A * C) + (D * F)

print("VALOR A PAGAR: R$ {:.2f}. format(valor_a_pagar)")
# 5. Avaliar as seguintes espresións, tendo en conta que as variables  teñen os valores:

# a)
i, j, k = 1, 0, 1
print("a)", i + k <= j - k * 3 and k >= 2)   # False

# b)
i, j, k = 3, 2, -1
print("b)", i == 3 or j <= 2 and k > 0)      # True

# c)
tipo, rede = 10, 7.5
print("c)", tipo < rede + 1.5)               # False

# d)
ano = 1993
print("d)", ano % 400 == 0)                  # False

# e)
print("e)", 3 == 2 or 5 > 1 + 1)             # True

# f)
print("f)", 5 - 2 > 4 and not(0.5 == 1 / 5)) # False

# g)
a, b, c, d = 2, 5, 6, 10
print("g)", a >= b or a >= c and a < d)      # False

# h)
a, b, c, d = 2, 5, 6, 10
print("h)", a + b < c and a + c < d or 2 * a < a + b) # True

# i) en Python usamos "not" en lugar de "!"
a, b, c, d = 2, 5, 6, 10
print("i)", (not(a * b < d)) and (not(a * b < c)) or b + c <= d) # True
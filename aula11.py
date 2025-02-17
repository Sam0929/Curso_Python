# Precedência de operadores

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -


conta_1 = 1 + 2 ** 3 + 5  # 14
conta_2 = 1 + 2 ** (3 + 5)  # 2^8 + 1 = 257
conta_3 = (1 + 2) ** (3 + 5)  # 3^8 = 6561

print(conta_1)
print(conta_2)
print(conta_3)

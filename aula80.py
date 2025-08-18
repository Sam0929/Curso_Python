
# Métodos úteis:
# add, update, clear, discard

s1= set()

s1.add(1)
s1.add("Sam")
s1.update(("1233", 123123))
# s1.clear()
s1.discard('1233')
print(s1)

# Operadores úteis:
# união | união (union) - Une

s1 = {1, 2, 3}
print(s1)
s2 = {3, 2, 2, 2, 4, 5, 6}

s3 = s1 | s2
print("união", s3)

s3 = s1 & s2
print("inter", s3)

s3 = s1 - s2

print("differ", s3)

s3 = s2 - s1
 
print("differ", s3)

s3 = s1 ^ s2

print("symmetric difference", s3 )








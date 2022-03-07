# list all natural numbers 0-sum
# naturals = []
# for i in range(35):
#     naturals.append(i)

# combos = []
# for num in naturals:
#     a = num
#     for i in range(34 - num):
#         b = i
#         c = 34 - b - a
#         combo = []
#         combo.append(a)
#         combo.append(b)
#         combo.append(c)
#         combos.append(combo)

            
# def check(a, b, c) -> bool:
#     if (a + b > c) and (a + c > b) and (b + c > a):
#         return True
#     else:
#         return False


# triangles = []
# for combo in combos:
#     if check(combo[0], combo[1], combo[2]):
#         triangles.append(combo)

# isosceles = []
# for triangle in triangles:
#     if triangle[0] == triangle[1] or triangle[0] == triangle[2] or triangle[1] == triangle[2]:
#         isosceles.append(triangle)

# print(len(isosceles))
# print(len(triangles))


# X is number of tests in a group, n is group sizes
n = 8
g = 1000 / n
eX = 1 * (.95**n) + (n + 1) * (1 - (.95**n))
eY = g * eX
print(eX)
print(eY)
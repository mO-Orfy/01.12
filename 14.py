def SOK(x, y):
    while y:
        x, y = y, x % y
    return x

def PRO(x, y):
    return x * y // SOK(x, y)

def fra(A, B, C, D):
    den1 = PRO(B, D)
    sum = A * (den1 // B) - C * (den1 // D)
    div1 = SOK(sum, den1)
    num1 = sum // div1
    num2 = den1 // div1
    return num1, num2
A = int(input("Введите числитель первой дроби (A):"))
B = int(input("Введите знаменатель первой дроби (B): "))
C = int(input("Введите числитель второй дроби (C): "))
D = int(input("Введите знаменатель второй дроби (D): "))
num1, num2 = fra(A, B, C, D)
print(f"Произведение дробей: {num1}/{num2}")

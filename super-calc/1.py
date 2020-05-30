print("Введите первое число: ")
a = float(input())
print("Введите второе число: ")
b = float(input())
print("Введите операцию, которую Вы хотите совершить: ")
oper = input()
if oper == "+":
    res = a + b
elif oper == "-":
    res = a - b
elif oper == "*":
    res = a * b
elif oper == "/":
    res = a / b
elif oper == "$":
    res = (a + b) ** 2
str = str(a) + " " + oper + " " + str(b) + " = " + str(res)
print(str)

# функция сложения
def add(x, y):
    return x + y

# функция вычитания
def subtract(x, y):
    return x - y

# функция умножения
def multiply(x, y):
    return x * y

# функция деления
def divide(x, y):
    return x / y

print("Выберите операцию.")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

# запрашиваем ввод пользователя
choice = input("Введите номер операции (1/2/3/4): ")

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Некорректный ввод")
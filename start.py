print("Hello World")

#Variavel
variavel_name = "Erickson"
variavel_last = "Martinez"
print(variavel_name+ " "+variavel_last)

# String
nome = "string"
numero = 1
print('String')
print("String")
print(str(numero))
print(nome)

# numbers
number_int = 1
number_float = 3.14
number_int_string = '1'
number_float_string = '3.14'
print(number_int)
print(number_float)
print(int(number_int_string))
print(float(number_float_string))

#Input
name = input("Enter your name: ")
print("Welcome " + name)

#Calc
num1 =input(name +' enter first number: ')
num2 = input(name +' enter second number: ')
operation = input('Enter which operation you want to do, sum, subtract, multiply, divide or average: ')
match operation:
    case 'sum':
        result = float (num1) + float (num2)
    case 'subtract':
        result = float (num1) - float (num2)
    case 'multiply':
        result = float (num1) * float (num2)
    case 'divide':
        result = float (num1) / float (num2)
    case 'average':
        result = (float (num1) + float (num2)) / 2

print('Result of the '+ operation +' '+ str(result))
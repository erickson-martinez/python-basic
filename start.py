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
age = input("Enter your age: ")
print("Welcome " + name)

#if statements
if float(age) >= 18:
    print("You of legal age.")
else:
    print("You are underage.")

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

#List in array
friends = ['jaq', 'ppu', 'GG', 'Jaque', 'Rhay']
numbers = [133,55,2,77,99,2,3,4,5,6,7,8,9,1,2,3,5,9,10,8,5,7,11,55,99,55]

print(friends[1:3]) # index start 1 to less than 3
print(friends[2:]) #index start 2 to end
friends[1] = name #alter index 1
print(friends)

#join array
friends.extend(numbers)
print(friends)

#insert in array
friends.insert(3, 'Hiago')
print(friends)

#remove in array
friends.remove('Jaque')
print(friends)

#remove in array by index
friends.pop(1)
print(friends)

#finds element by index
friends.index('Rhay')
print(friends)

#count element in array
print(friends.index(1))

#order
separate_numbers = [item for item in friends if isinstance(item, (int, float))]
separate_friends = [item for item in friends if isinstance(item, str)]

separate_numbers.sort()
separate_friends.sort()
print(separate_numbers)
print(separate_friends)




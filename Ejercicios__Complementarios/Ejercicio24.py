#Mostrar series de Fibonacci hasta 10 términos
num1 = 0
num2 = 1
print(num1)
print(num2)
for i in range(0,12-1):
  fib=num1+num2
  num1 = num2
  num2 = fib
  print(fib)



# 1. Escreva um programa que leia dois números inteiros e exiba a soma deles.
ex1N1 = int(input("Insert number 1: "))
ex1N2 = int(input("Insert number 2: "))
ex1Sum = ex1N1+ex1N2
print(f"Sum: {ex1Sum}")

# 2. Escreva um programa que receba um número e verifique se ele é par ou ímpar.
ex2Num = int(input("Insert a number: "))
if ex2Num % 2 == 0:
    print(f"{ex2Num} is even. ")
else:
    print(f"{ex2Num} is odd. ")

# 3. Escreva um programa que calcule o fatorial de um número.
n=int(input("Insert the number: "))
total=0
antecessor=n-1
fatorial = n

while antecessor > 0:
    fatorial *= antecessor 
    
    antecessor-=1
   
print(f"{n}! = {fatorial}")

# 4. Escreva um programa que exiba os primeiros "n" termos da sequência de 
# Fibonacci. Sendo "n" o numero que o usuário digitar.
# 1, 1, 2, 3, 5, 8, 13

n=int(input("Fibonacci, até o termo de nº:  "))
n1=1
n2=1
n3=n1+n2
fiboLista=[n1,1]

for i in range(n-2):
    
    mainNumero = fiboLista[-2]
    ultimoNumero = fiboLista[-1]    

    nAdd = mainNumero+ultimoNumero #nAdd = 1 + 1 => nAdd = 2

    fiboLista.append(nAdd) #fiboLista=[1, 2]

print(fiboLista)

    








    





    
    

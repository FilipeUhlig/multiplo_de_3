"""
Programa: multiplo_de_3
Descrição: Este programa verifica se um número digitado é múltiplo de 3 ou não, em caso de número real, ele retorna que é não inteiro.
Autor: F
Data : 23/06/2023
Versão: 0.0.1
"""

#Atribuição de variáveis



x = 0

#Entrada de dados

x = float(input("Qual o número desejado? "))


#Processamento de dados

if (x % 3) == 0 and int(x) == x:
    print(f"O número {x} é múltiplo de 3.")
    
elif (x % 3) != 0 and int(x) == x:
    print(f"O número {x} não é múltiplo de 3.")

else:
    print("O número é não inteiro.")



#Saida de dadaos
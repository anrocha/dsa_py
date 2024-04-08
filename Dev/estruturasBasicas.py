
#Versão Python
from platform import python_version
print('Versão Python: ', python_version())

#Verificar tipo do dado
print('Tipo do dado:', type('a'))

#Divisão com ' / ' é float mas com ' // ' é inteiro

#Conversões de float e int
float(9)
int(6.0)

#Converter número para Binário e Hex
print(bin(540))
print(hex(540))

#Funções built-in

## Retornar o número absoluto
abs(-9)
abs(9)

## Arredondamento
round(9.22,2) 

## Potência
pow(5,4)
print(5**4)

# Variáveis

## Atribuindo valor a variáveis
var_teste = 1


## Declaração Múltipla

var1, var2, var3 = "andre", "andre2", "andre3"

var1 = var2 = var3 = "andre"


## Buscar dado apenas de um pedaço da string
### Aplicar slicing

stringtextoa = 'andre'

stringtextoa[0]
stringtextoa[1]

stringtextoa[0:] #tudo após o 0

stringtextoa[2:3] #tudo entre 2 e 3

stringtextoa[:2] #tudo até 2

stringtextoa[-1] #último caracter de trás para frente

stringtextoa[::-1] #Traz tudo de trás para frente

stringtextoa[::2] #Um carácter sim, um não.







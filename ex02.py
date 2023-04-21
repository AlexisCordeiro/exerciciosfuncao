#Escreva uma função que receba Nome e Idade. Retorne valores que contêm a chave "idade" e cujo valor é maior que 18.
def funcao():
    dicionario = {}
    while True:
        chave = str(input('Digite os nomes da sua lista(caso queira para digite "."): '))
        if chave == ".":
            break
        
        valor = int(input('Digite a idade: '))
    
        if valor > 18:
            dicionario[chave] = valor
            
    return print('Os maiores de idade são: ', dicionario)

print(funcao())
        
        
#Escreva uma função que receba um dicionário como entrada e retorna uma nova lista com as chaves ordenadas em ordem alfabética.
# Escreva uma função que receba um dicionário como entrada e retorna uma nova lista contendo apenas as chaves
def funcao():
    dicionario = {}
    n = int(input('Digite o números de vezes que deseja adicionar chave valor: '))
    for i in range(n):
        chave = str(input('Adicione palavras para ser sua chave no dicionario: '))
        valor = int(input('Adicione valor(números) para suas chaves: '))
        if chave not in dicionario and valor not in dicionario:
            dicionario[chave] = valor
        else:
            print('O item já está adicionado no dicionario')
        
    dicionario_ordenado = {chave: dicionario[chave] for chave in sorted(dicionario, key=lambda x: x[0])}
    return(print(dicionario_ordenado))
funcao()
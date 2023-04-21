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
    
    lista2 = []
    for chave, valor in dicionario.items():
        lista2.append(chave)
    
            
    return(print('Este é o seu dicionário: ', dicionario, '. Esses são as chaves: ', lista2))
    
funcao()
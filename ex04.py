#Escreva uma função que receba um dicionário como entrada e retorna duas listas. Uma com chave e outra com valor.
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
    
    lista = []      
    lista2 = []
    for chave, valor in dicionario.items():
        lista.append(chave)
        lista2.append(valor)
    
            
    return(print('Este é o seu dicionário: ', dicionario, 
    '. Essas são a chave: ', lista, '. Essa são o valor: ', lista2))
    
funcao()
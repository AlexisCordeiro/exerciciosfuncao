#Escreva uma função que receba duas listas de mesmo comprimento, uma contendo chaves 
# e outra contendo valores, e retorna um dicionário criado a partir dessas listas.
lista = []
lista2 = []
def funcao():
    dicionario = {}
    n = int(input('Digite o números de vezes que deseja adicionar chave valor: '))
    for i in range(n):
        chave = input('Adicione chaves em sua lista: ')
        if chave not in lista:
            lista.append(chave)
        valor = input("Digite o valor: ")
        if valor not in lista2:
            lista2.append(valor)
    
    def criar_dicionario(lista, lista2):
        return dict(zip(lista, lista2))
    
    dicionario = criar_dicionario(lista, lista2)
    return print('As chaves está aqui: ', lista, '. Os valores estão aqui: ', lista2, '. As duas em forma de dicionário: ', dicionario)
funcao()




        
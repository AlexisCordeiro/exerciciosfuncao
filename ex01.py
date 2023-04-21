#Escreva uma função que receba itens (números) em um dicionário como entrada e retorne a chave com o maior valor.

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
            
    print(dicionario)
    
    
    def chave_maior_valor(dicionario):
        chave_maior = None
        maior_valor = float('-inf')
        for chave, valor in dicionario.items():
            if valor > maior_valor:
                chave_maior = chave
                maior_valor = valor
        return print('A chave com maior valor é: ', chave_maior)
        
    chave_maior_valor(dicionario)    
    
print(funcao())


    




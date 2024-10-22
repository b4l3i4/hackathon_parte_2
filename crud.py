# Sistema de CRUD simples com dicionário CORRIGIDO
def mostrar_menu(): #':'
    print("Menu:")
    print("1. Adicionar Usuário")
    print("2. Listar Usuários")
    print("3. Editar Usuário")
    print("4. Remover Usuário")
    print("5. Sair")

def adicionar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    if nome in usuarios:  #'not'
        print("Usuário já existe. Tente outro nome.")
        return
    idade = input("Digite a idade do usuário: ")
    if not idade.isdigit():  
        print("Idade deve ser um número.")
        return
    usuarios[nome] = idade 
    print("Usuário adicionado com sucesso!") #erro de escrita

def listar_usuarios(usuarios):
    if not usuarios: 
        print("Nenhum usuário cadastrado.")
        return
    for nome, idade in usuarios.items(): #não estava puxando nome e idade 
        print('nome: ', nome)
        print('idade: ', idade)


def editar_usuario(usuarios):
    nome = input("Digite o nome do usuário que deseja editar: ")
    if nome not in usuarios: 
        print("Usuário não encontrado!")
        return
    nova_idade = input("Digite a nova idade: ")
    if not nova_idade.isdigit():  
        print("Idade deve ser um número.")
        return
    usuarios[nome] = nova_idade 
    print("Usuário atualizado com sucesso!")

def remover_usuario(usuarios):
    nome = input("Digite o nome do usuário que deseja remover: ")
    if nome in usuarios: # 'not' 
        usuarios.pop(nome)
        print('Usuário removido com sucesso!')   #adicionar o print

        return True 
    else:
        print("Usuário não encontrado!")

def main():
    while True: #  Laço de repetição
        usuarios = {} # trocou cochete por chaves
    
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        if not opcao.isdigit():  
            print("Opção inválida! Por favor, digite um número.")
            return #tinha "continue" no lugar q deveria ser return
        opcao = int(opcao)  
        if opcao == 5: # tava escrito opção '0'e era pra ser 5 
            print("Saindo do sistema...")
            break
        elif opcao == 1:
            adicionar_usuario(usuarios)
        elif opcao == 2:
            listar_usuarios(usuarios)
        elif opcao == 3:
            editar_usuario(usuarios)
        elif opcao == 4:
            remover_usuario(usuarios)
        else:
            print("Opção inválida!")
if __name__  ==  '__main__':  #  faltou o  main
    main()


# Liste os erros encontrados
# Quantidade de erros encontrados: 11
# Tempo gasto: 1h
# O codigo funciona perfeitamente? Simm
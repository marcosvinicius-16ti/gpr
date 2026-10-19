def criar_heroi():
    print ("BEM VINDO AO MEU PEQUENO JOGO")
    nome = input("Digite o nome do seu heroi: ")

    # aqui irei definir os stats iniciais do heroi
    return {
        "nome": nome,
        "vida_max": 100,
        "vida_atual": 10,
        "ataque": 2
    }

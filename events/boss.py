def iniciar_boss():
    """Retorna os textos de introdução da Boss Fight."""
    textos = [
        "\n UMA FIGURA MACABRA APARECE NA SUA FRENTE... ela parece querer dizer algo",
        "\n ???: responda minhas perguntas e ira sair vivo",
        "\n --- PRIMEIRA PERGUNTA ---",
        "encontrei 10 aventureiros antes, 4 foram decaptados, quantos restaram?",
        "1) 6 aventureiros",
        "2) eu poupei a vida deles",
        "3) 2 aventureiros",
        "\n Qual sua resposta? 1, 2 ou 3?",
    ]
    return textos


def processar_resposta_boss(resposta, jogador):
    """Processa a resposta do jogador para a pergunta do Boss."""
    resposta = resposta.strip()

    if resposta == "1":
        mensagem = "\n vc se salvou dessa vez, mas nao se preocupe eu voltarei..."
        acertou = True
    else:
        mensagem = "\n que pena, esperava mais de voce\n a figura lentamente se aproxima com um sorriso agoniante, e o fim..."
        jogador["vida_atual"] = 0
        acertou = False

    return jogador, mensagem, acertou

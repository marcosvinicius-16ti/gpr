def enfrentar_boss(jogador):
    print("\n UMA FIGURA MACABRA APARECE NA SUA FRENTE... ela parece\nquerer dizer algo")
    print("\n ???: responda minhas perguntas e ira sair vivo")
    
    acertos = 0
    
    # pergunta 1
    
    print("\n PRIMEIRA PERGUNTA")
    print("\n encontrei 10 aventureiros antes, 4 foram decaptados,quantos restaram?")
    print ("1)6 aventureiros")
    print("2) eu poupei a vida deles")
    print ("3) 2 aventureiros")
    
    resposta1 = input("\n Qual sua resposta? 1,2 ou 3?").strip()
    
    if resposta1 =="2":
        print("\n vc se salvou dessa vez,mas nao se preocupe eu voltarei...")
        acertos =+1
    else:
        print("\n que pena, esperava mais de voce\n a figura lentamente se aproxima, e o fim...")
    return jogador
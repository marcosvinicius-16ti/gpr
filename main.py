from character.hero import criar_heroi

if __name__ == "__main__":
    jogador = criar_heroi()

    print ("\n-----STATS DO JOGADOR-----")
    print (f"Nome: {jogador['nome']}")
    print (f"Vida Máxima: {jogador['vida_max']}")
    print (f"Vida Atual: {jogador['vida_atual']}")
    print (f"Ataque: {jogador['ataque']}")

    # pergunta se o jogador deseja continuar ou sair do jogo

    resposta = input("\nDeseja continuar pro dia 1? (s/n): ").lower().strip()

    if resposta in ["s", "sim"]:
        print("\nContinuando para o dia 1...")
    else:
        print("\nSaindo do jogo...")
from character.hero import criar_heroi
from events.daily import executar_evento_diario
from events.boss import enfrentar_boss

if __name__ == "__main__":
    jogador = criar_heroi()

    print("\n-----STATS DO JOGADOR-----")
    print(f"Nome: {jogador['nome']}")
    print(f"Vida Máxima: {jogador['vida_max']}")
    print(f"Vida Atual: {jogador['vida_atual']}")
    print(f"Ataque: {jogador['ataque']}")

    dia = 1
    jogo_ativo = True

    while jogo_ativo:
        # Verificação se o jogador esta vivo ou morto
        if jogador["vida_atual"] <= 0:
            print("\n infelizmente voce morreu...")
            jogo_ativo = False
            break

        # mostra o dia q o player esta
        print(f"\n================ DIA {dia} ================")

        # quando for dia 5 (boss)
        if dia == 5:
            print("alguma coisa apareceu no seu caminho, ele nao parece ser humano...")
            jogador = enfrentar_boss(jogador)
        else:
            jogador = executar_evento_diario(jogador)

        print("\n--- STATS DO JOGADOR APOS O EVENTO ---")
        print(f"Nome: {jogador['nome']}")
        print(f"Vida Atual: {jogador['vida_atual']}/{jogador['vida_max']}")
        print(f"Ataque: {jogador['ataque']}")

        # se morreu no evento
        if jogador["vida_atual"] <= 0:
            print("\n infelizmente voce morreu...")
            jogo_ativo = False
            break

        # MENSAGEM DIA 3
        if dia == 3:
            print(
                "\n voce sente um calafrio no coracao, algo se aproxima rapidamente e estara aqui daqui a 2 dias..."
            )

        # pergunta se quer continuar para o proximo dia
        resposta = (
            input(f"\nDeseja continuar para o próximo dia? (s/n): ").lower().strip()
        )

        if resposta in ["s", "sim"]:
            dia += 1
        else:
            print("\n voce desistiu da sua jornada...")
            jogo_ativo = False

    print("\nObrigado por jogar!")

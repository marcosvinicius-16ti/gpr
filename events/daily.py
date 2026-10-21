import random


def executar_evento_diario(jogador):
    events = [
        {
            "descricao": "voce encontrou um manto magico de cura e recuperou um pouco de vida.",
            "efeito": "vida_atual",
            "valor": 5,
        },
        {
            "descricao": "voce encontrou um encantamento pra sua espada e aumentou seu ataque.",
            "efeito": "ataque",
            "valor": 3,
        },
        {
            "descricao": "voce caiu enquanto corria da chuva e machucou seu joelho, perdendo um pouco de vida.",
            "efeito": "vida_atual",
            "valor": -5,
        },
    ]

    evento_escolhido = random.choice(events)

    efeito_evento = evento_escolhido["efeito"]
    valor_mudanca = evento_escolhido["valor"]

    texto_efeito = ""

    if efeito_evento == "vida_atual":
        jogador["vida_atual"] += valor_mudanca
        if jogador["vida_atual"] > jogador["vida_max"]:
            jogador["vida_atual"] = jogador["vida_max"]
        elif jogador["vida_atual"] < 0:
            jogador["vida_atual"] = 0

        texto_efeito = (
            f"efeito: {valor_mudanca:+d} de vida (vida atual: {jogador['vida_atual']})"
        )
    elif efeito_evento == "ataque":
        jogador["ataque"] += valor_mudanca
        texto_efeito = f"efeito: {valor_mudanca:+d} de ataque (novo ataque atual: {jogador['ataque']})"

    # Criamos o texto formatado para ser lido pela janela
    mensagem_evento = f"\nalgo aconteceu em sua jornada: {evento_escolhido['descricao']}\n{texto_efeito}"

    return jogador, mensagem_evento


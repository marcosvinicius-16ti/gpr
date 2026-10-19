import random 
def executar_evento_diario(jogador):
    events = [
        {
            "descricao": "voce encontrou um manto magico de cura e recuperou um pouco de vida.",
            "efeito": "vida_atual",
            "valor": 5
        },
        {
            "descricao": "voce encontrou um encantamento pra sua espada e aumentou seu ataque.",
            "efeito": "ataque",
            "valor": 3
        },
        {
            "descricao": "voce caiu enquanto corria da chuva e machucou seu joelho, perdendo um pouco de vida.",
            "efeito": "vida_atual",
            "valor": -5
        }

    ]
    # vai selecionar um evento

    evento_escolhido = random.choice(events)

    print(f"\nalgo aconteceu em sua jornada: {evento_escolhido['descricao']}")

    # aplica o efeito do evento no jogador

    efeito_evento = evento_escolhido["efeito"]
    valor_mudanca = evento_escolhido["valor"]

    if efeito_evento == "vida_atual":
        jogador["vida_atual"] += valor_mudanca
        if jogador["vida_atual"] > jogador["vida_max"]:
            jogador["vida_atual"] = jogador["vida_max"]
        elif jogador["vida_atual"] < 0:
            jogador["vida_atual"] = 0

        print(f"efeito: {valor_mudanca:+d} de vida (vida atual: {jogador['vida_atual']})")
    elif efeito_evento == "ataque":
        jogador["ataque"] += valor_mudanca
        print(f"efeito: {valor_mudanca:+d} de ataque (novo ataque atual: {jogador['ataque']})")
    
    return jogador
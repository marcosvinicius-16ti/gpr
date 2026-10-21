from character.hero import criar_heroi
from events.daily import executar_evento_diario
from events.boss import iniciar_boss
from layout.window import JogoJanela
from events.boss import processar_resposta_boss


class GerenciadorJogo:
    def __init__(self):
        self.janela = JogoJanela()
        self.jogador = None
        self.dia = 1
        self.estado = "PEDIR_NOME"

        self.janela.ao_enviar_resposta = self.processar_entrada

        self.janela.escrever("Digite o nome do seu heroi: ")


    def exibir_stats(self):
        self.janela.escrever("\n----- STATS DO JOGADOR -----")
        self.janela.escrever(f"Nome: {self.jogador['nome']}")
        self.janela.escrever(
            f"Vida Atual: {self.jogador['vida_atual']}/{self.jogador['vida_max']}"
        )
        self.janela.escrever(f"Ataque: {self.jogador['ataque']}\n")

    def iniciar_jogo(self):
        self.exibir_stats()
        self.executar_dia()

    def executar_dia(self):
        if self.jogador["vida_atual"] <= 0:
            self.janela.escrever("\n infelizmente sua aventura terminou cedo demais...")
            self.estado = "FIM"
            return

        self.janela.escrever(f"================ DIA {self.dia} ================")


        #logica boss dia 5
        if self.dia == 5:
            textos_boss = iniciar_boss()
            for texto in textos_boss:
                self.janela.escrever(texto)
            self.estado = "PERGUNTA_BOSS_1"
        else:
            # Dias normais
            self.jogador, mensagem_evento = executar_evento_diario(self.jogador)
            self.janela.escrever(mensagem_evento)
            self.exibir_stats()

            if self.jogador["vida_atual"] <= 0:
                self.janela.escrever("\n infelizmente sua aventura terminou cedo demais...")
                self.estado = "FIM"
                return

            if self.dia == 3:
                self.janela.escrever(
                    "voce derrepente sente um medo agoniante, algo esta chegando em 2 dias...\n"
                )

            self.janela.escrever("Deseja continuar para o próximo dia? (s/n)")
            self.estado = "PERGUNTA_CONTINUAR"

    def processar_entrada(self, resposta: str):
        resposta = resposta.lower().strip()
        if self.estado == "PEDIR_NOME":
            nome_heroi = resposta if resposta else "Aventureiro"
            self.jogador = criar_heroi(nome_heroi)
            self.janela.escrever(f"\nBem-vindo, {self.jogador['nome']}! Sua aventura começa agora.\n")
            self.estado = "INICIO"
            self.iniciar_jogo()
            return
        
        if self.estado == "PERGUNTA_CONTINUAR":
            if resposta in ["s", "sim"]:
                self.dia += 1
                self.executar_dia()
            else:
                self.janela.escrever(
                    "\nvoce nao quis continuar nesse mundo"
                )
                self.estado = "FIM"

        elif self.estado == "PERGUNTA_BOSS_1":
            self.jogador, mensagem, acertou = processar_resposta_boss(resposta, self.jogador)
            self.janela.escrever(mensagem)
            self.exibir_stats()

            self.estado = "FIM"

    def rodar(self):
        self.janela.janela.after(10, self.iniciar_jogo)
        self.janela.iniciar()


if __name__ == "__main__":
    jogo = GerenciadorJogo()
    jogo.rodar()

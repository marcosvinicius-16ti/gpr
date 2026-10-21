import tkinter as tk


class JogoJanela:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Nada e oque parece ser...")
        self.janela.geometry("800x600")
        self.janela.configure(bg="#0a0a0a")

        # Callback pela entrada do heroi
        self.ao_enviar_resposta = None

        # texto
        self.texto_area = tk.Text(
            self.janela,
            bg="#0a0a0a",
            fg="#00ff66",  # Verde terminal macabro
            font=("Consolas", 12),
            wrap=tk.WORD,
            padx=15,
            pady=15,
            insertbackground="white",
        )
        self.texto_area.pack(expand=True, fill="both", padx=15, pady=15)
        self.texto_area.bind("<Key>", lambda e: "break")

        # entrada do botao
        frame_input = tk.Frame(self.janela, bg="#0a0a0a")
        frame_input.pack(fill="x", padx=15, pady=(0, 15))

        self.entrada_var = tk.StringVar()
        self.entrada = tk.Entry(
            frame_input,
            textvariable=self.entrada_var,
            bg="#1a1a1a",
            fg="white",
            font=("Consolas", 12),
            insertbackground="white",
            relief=tk.FLAT,
        )
        self.entrada.pack(side=tk.LEFT, expand=True, fill="x", padx=(0, 10))
        self.entrada.bind("<Return>", self._tratar_enter)
        self.entrada.focus()

        btn_enviar = tk.Button(
            frame_input,
            text="Enviar",
            command=self._tratar_click,
            bg="#050505",
            fg="white",
            font=("Consolas", 10, "bold"),
            relief=tk.FLAT,
            padx=15,
        )
        btn_enviar.pack(side=tk.RIGHT)

    def escrever(self, mensagem: str):
        """Imprime mensagens na janela do jogo."""
        self.texto_area.config(state=tk.NORMAL)
        self.texto_area.insert(tk.END, mensagem + "\n")
        self.texto_area.see(tk.END)
        self.texto_area.config(state=tk.DISABLED)
        self.janela.update_idletasks()  

    def _tratar_enter(self, event):
        self._tratar_click()

    def _tratar_click(self):
        texto = self.entrada_var.get().strip()
        if texto and self.ao_enviar_resposta:
            self.escrever(f"> {texto}\n")
            self.entrada_var.set("")
            self.ao_enviar_resposta(texto)

    def iniciar(self):
        """Inicia o loop da janela."""
        self.janela.mainloop()


from tela_nivel_2 import *

from funçoes import *
root = Tk()


class tela_1 ():
    def tela_inicial(self):
        self.root.title("CenTEC")
        self.root.config(background="#006669")
        self.root.geometry("900x650")
        self.root.resizable(True, True)
        self.root.maxsize(width=1000, height=700)
        self.root.minsize(width=100, height=70)

# criação dos frames
        self.frame_1 = Frame(bd=2, bg="#006675", highlightbackground="#006670", highlightthickness=4)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.48)
        self.frame_2 = Frame(bd=2, bg="#006670", highlightbackground="#006670", highlightthickness=4)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.48)


# criação do botao chek_box

        self.motorola = StringVar()
        self.samsung = str(2)
        self.bot_chek = atk.Button3d(self.frame_1, bg="#1EAAF1", text="chek box",command=self.situacao)
        self.bot_chek.place(relx=0.70, rely=0.55, relwidth=0.10, relheight=0.15)

        self.chek = Checkbutton(self.frame_1, text="esperando", variable=self.motorola,onvalue=1,offvalue=0)
        self.chek.place(relx=0.01, rely=0.80, relwidth=0.11, relheight=0.05)

        self.chek = Checkbutton(self.frame_1, state="active", text="pronto", variable=self.samsung,
                                command=self.chek_box_s)
        self.chek.place(relx=0.01, rely=0.90, relwidth=0.11, relheight=0.05)



#criaçao dos botoes
        self.bot_limpar = atk.Button3d(self.frame_1, bg="#1EAAF1", text="limpar", command=self.limpa_tela)
        self.bot_limpar.place(relx=0.15, rely=0.8, relwidth=0.10, relheight=0.15)



# ADD CLIENTE
        self.bot_add = atk.Button3d(self.frame_1 ,text="ADD Cliente", command=self.adicione_cliente,bg="#1EAAF1")
        self.bot_add.place(relx=0.41, rely=0.0655, relwidth=0.15, relheight=0.15)
# CONSULTAR CLIENTE
        self.bot_consultar_clientes = atk.Button3d(self.frame_1, bg="#1EAAF1", text="CONSULTAR CLIENTES", command=self.tela_consultar_db)
        self.bot_consultar_clientes.place(relx=0.65, rely=0.01, relwidth=0.195, relheight=0.15)
#GARANTIA
        self.bot_garantia = atk.Button3d(self.frame_1, bg="#1EAAF1", text="GARANTIA", command=self.tela_garantia)
        self.bot_garantia.place(relx=0.85, rely=0.01, relwidth=0.15, relheight=0.15)
#ENTRADA DE AAPARELHO
        self.bot_entrada_aparelhos = atk.Button3d(self.frame_1, bg="#1EAAF1", text="ADD APARELHO",command=self.adiciona_smart)
        self.bot_entrada_aparelhos.place(relx=0.35, rely=0.8, relwidth=0.15, relheight=0.15)
# APARELHOS QUE ESTAO NA LOJA
        self.bot_aparelhos = atk.Button3d(self.frame_1, bg="#1EAAF1", text="APARELHOS",
                                          command=self.tela_aparelhos)
        self.bot_aparelhos.place(relx=0.65, rely=0.20, relwidth=0.195, relheight=0.15)
# TELAS
        self.bot_telas = atk.Button3d(self.frame_1, bg="#1EAAF1", text="muda status",
                                          command=self.situacao)
        self.bot_telas.place(relx=0.85, rely=0.20, relwidth=0.15, relheight=0.15)

#LIMPAR BUSCA
        self.bot_limpar_BUSCA = atk.Button3d(self.frame_1, bg="#1EAAF1", text="limpar", command=self.limpa_tela_inicial)
        self.bot_limpar_BUSCA.place(relx=0.70, rely=0.83, relwidth=0.10, relheight=0.15)
# BOTAO BUSCAR
        self.bot_buscar = atk.Button3d(self.frame_1, bg="#1EAAF1", text="Buscar", fg="white", command=self.busca_clientes)
        self.bot_buscar.place(relx=0.90, rely=0.675, relwidth=0.10, relheight=0.15)
#BOTAO DAR BAIXA
        self.bot_saida = atk.Button3d(self.frame_1, text="dar baixa", command=self.dar_baixa, bg="#1EAAF1")
        self.bot_saida.place(relx=0.85, rely=0.425, relwidth=0.15, relheight=0.15)


#criaçao dos labels
        self.lb_id_smartphone = Label(self.frame_1, text="ID \nAparelho", fg="white", bg="#006675",
                                      font=("candara", "15", "bold italic"))
        self.lb_id_smartphone.place(relx=0.51, rely=0.45, relwidth=0.15, relheight=0.150)

        self.entrada_id_smartphone = Entry(self.frame_1)
        self.entrada_id_smartphone.place(relx=0.65, rely=0.45, relwidth=0.19, relheight=0.10)

# criaçao das label DO NOME
        self.lb_nome = Label(self.frame_1, text="Nome \ndo cliente", fg="white", bg="#006675",
                             font=("candara", "15", "bold italic"))
        self.lb_nome.place(relx=0.53, rely=0.65, relwidth=0.10, relheight=0.20)
# codigo de entrada DO NOME
        self.entrada_nome_i = Entry(self.frame_1)
        self.entrada_nome_i.place(relx=0.65, rely=0.70, relwidth=0.19, relheight=0.10)

# label nome entrada para cadastro de clientes
        self.lb_nome = Label(text="Nome", fg="white", bg="#006675",
                             font=("candara", "15", "bold italic"))
        self.lb_nome.place(relx=0.03, rely=0.02, relwidth=0.10, relheight=0.09)
# codigo de entrada nome
        self.entrada_nome = Entry(self.frame_1)
        self.entrada_nome.place(relx=0.15, rely=0.02, relwidth=0.25, relheight=0.10)

# label telefone
        self.lb_telefone = Label(text="Telefone", fg="white", bg="#006675",
                                 font=("candara", "15", "bold italic"))
        self.lb_telefone.place(relx=0.03, rely=0.10, relwidth=0.12, relheight=0.05)
# codigo de entrada telefone
        self.entrada_telefone = Entry(self.frame_1)
        self.entrada_telefone.place(relx=0.15, rely=0.15, relwidth=0.25, relheight=0.10)

#marca
        self.lb_marca = Label(self.frame_1,text="Marca", fg="white", bg="#006675",
                              font=("candara", "15", "bold italic"))
        self.lb_marca.place(relx=0.01, rely=0.43, relwidth=0.10, relheight=0.05)
        self.entrada_marca = Entry(self.frame_1)
        self.entrada_marca.place(relx=0.15, rely=0.41, relwidth=0.10, relheight=0.10)

#MODELO
        self.lb_model = Label(self.frame_1, text="Modelo", fg="white", bg="#006675",
                              font=("candara", "15", "bold italic"))
        self.lb_model.place(relx=0.25, rely=0.43, relwidth=0.10, relheight=0.05)

        self.entrada_model = Entry(self.frame_1)
        self.entrada_model.place(relx=0.35, rely=0.41, relwidth=0.15, relheight=0.10)


#ORÇAMENTO
        self.lb_orcamento = Label( self.frame_1,text="Orçamento", fg="white", bg="#006675",
                                  font=("candara", "15", "bold italic"))
        self.lb_orcamento.place(relx=0.01, rely=0.55, relwidth=0.13, relheight=0.1)
        self.entrada_orcamento = Entry(self.frame_1)
        self.entrada_orcamento.place(relx=0.15, rely=0.54, relwidth=0.35, relheight=0.10)

 # DESCRIÇÃO
        self.lb_descricao = Label(self.frame_1,text="Descrição", fg="white", bg="#006675",
                                  font=("candara", "15", "bold italic"))
        self.lb_descricao.place(relx=0.01, rely=0.7, relwidth=0.11, relheight=0.05)
        self.entrada_descricao = Entry(self.frame_1)
        self.entrada_descricao.place(relx=0.15, rely=0.67, relwidth=0.35, relheight=0.10)


# ID DO CLIENTE PARA ADICIONAR O APARELHO
        self.lb_id_cliente = Label(self.frame_1, text="id cliente", fg="white", bg="#006675",font=("candara", "15", "bold italic"))
        self.lb_id_cliente.place(relx=0.13, rely=0.28, relwidth=0.12, relheight=0.10)
        self.entrada_id_cliente = Entry(self.frame_1)
        self.entrada_id_cliente.place(relx=0.25, rely=0.28, relwidth=0.15, relheight=0.1)

        self.novo_id_smartphone = Entry(self.frame_1)
        self.novo_id_smartphone.place(relx=0.26, rely=0.82, relwidth=0.08, relheight=0.10)

        # criaçao da tabela
        self.tabela = ttk.Treeview(self.frame_2, height=4, columns=("coluna1", "coluna2", "coluna3", "coluna4", "coluna5"))

        self.tabela.heading("#1", text="id")
        self.tabela.heading("#2", text="nome")
        self.tabela.heading("#3", text="telefone")
        self.tabela.heading("#4", text="ID aparelho")
        self.tabela.heading("#5", text="status")

        self.tabela.column("#0", width=00, minwidth=50, stretch=NO)
        self.tabela.column("#1", width=80, minwidth=50, stretch=NO)
        self.tabela.column("#2", width=200, minwidth=50, stretch=NO)
        self.tabela.column("#3", width=150, minwidth=50, stretch=NO)
        self.tabela.column("#4", width=60, minwidth=50, stretch=NO)
        self.tabela.column("#5", width=150, minwidth=50, stretch=NO)

        self.tabela.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
        # barra de rolagem
        self.scrool = Scrollbar(self.frame_2, orient="vertical")
        self.tabela.configure(xscrollcommand=self.scrool.set)
        self.scrool.place(relx=0.96, rely=0.05, relwidth=0.02, relheight=0.89)


class aplicacao (funcs,nivel_2,tela_1):

    def __init__(self):
        self.root = root
        self.tela_inicial()
        self.select()
        root.mainloop()
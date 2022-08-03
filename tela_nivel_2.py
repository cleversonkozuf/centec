

from funçoes import *

class nivel_2():

    def tela_consultar_db(self):
        consultar = Toplevel()
        consultar.title("CenTEC")
        consultar.config(background="#006669")
        consultar.geometry("700x500")
        consultar.resizable(True, True)
        consultar.maxsize(width=1000, height=700)
        consultar.minsize(width=100, height=70)

# frame da tela 3
        self.frame_consultar = Frame(consultar,bd=2, bg='#006675', highlightbackground="#006670", highlightthickness=4)
        self.frame_consultar.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.25)
        self.frame_consultar2 = Frame(consultar,bd=2, bg="#006670", highlightbackground="#006670", highlightthickness=4)
        self.frame_consultar2.place(relx=0.01, rely=0.26, relwidth=0.98, relheight=0.5)

        self.frame_editar = Frame(consultar, bd=2, bg="#006670", highlightbackground="#006670", highlightthickness=4)
        self.frame_editar.place(relx=0.01, rely=0.75, relwidth=0.98, relheight=0.25)

# botoes da tela 3

        self.bot_dell = atk.Button3d(self.frame_consultar, bg="#1EAAF1", text="Editar Clientes",
                                     command=self.botoes_editar_cliente)
        self.bot_dell.place(relx=0.01, rely=0.20, relwidth=0.15, relheight=0.35)
        self.id_edita = Entry(self.frame_consultar)
        self.id_edita.place(relx=0.25, rely=0.25, relwidth=0.1, relheight=0.2)

        self.bot_voltar = atk.Button3d(self.frame_editar, bg="#1EAAF1", text="Voltar",
                                     command=consultar.destroy)
        self.bot_voltar.place(relx=0.85, rely=0.64, relwidth=0.15, relheight=0.35)




# tabela do banco de dados da tela
        self.tabela_bd = ttk.Treeview(self.frame_consultar2, height=4,
                                      columns=("coluna0", "coluna1", "coluna2", "coluna3", "coluna4"))
        self.tabela_bd.heading("#1", text="id")
        self.tabela_bd.heading("#2", text="nome")
        self.tabela_bd.heading("#3", text="telefone")
        self.tabela_bd.heading("#4", text="Data de registro")
        self.tabela_bd.column("#0", width=00, minwidth=50, stretch=NO)
        self.tabela_bd.column("#1", width=60, minwidth=50, stretch=NO)
        self.tabela_bd.column("#2", width=150, minwidth=50, stretch=NO)
        self.tabela_bd.column("#3", width=200, minwidth=50, stretch=NO)
        self.tabela_bd.column("#4", width=200, minwidth=50, stretch=NO)
        self.tabela_bd.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

        self.select_tela_consultar_clientes()

    def tela_garantia(self):
        tela4 = Toplevel()
        tela4.title("CenTEC")
        tela4.config(background="#006666")
        tela4.geometry("700x500")
        tela4.resizable(True, True)


        self.lb_descricao = Label(tela4, text="GARANTIA ATIVA", fg="white", bg="#006669",
                                  font=("candara", "20", "bold italic"))
        self.lb_descricao.place(relx=0.325, rely=0.02, relwidth=0.40, relheight=0.10)
#botao voltar
        self.botao_voltar=atk.Button3d(tela4, bg="#1EAAF1", text="Voltar",
                                          command=tela4.destroy)
        self.botao_voltar.place(relx=0.84, rely=0.91, relwidth=0.15, relheight=0.08)

        # tabela da garantia
        self.tabela_garantia = ttk.Treeview(tela4, height=4,
                                            columns=(
                                            "coluna0", "coluna1", "coluna2", "coluna3", "coluna4", "coluna5", "coluna6",
                                            "coluna7"))
        self.tabela_garantia.heading("#1", text="nome")
        self.tabela_garantia.heading("#2", text="telefone")
        self.tabela_garantia.heading("#3", text="marca")
        self.tabela_garantia.heading("#4", text="modelo")
        self.tabela_garantia.heading("#5", text="id_smart")
        self.tabela_garantia.heading("#6", text="data de saida")
        self.tabela_garantia.heading("#7", text="Descrição")
        self.tabela_garantia.column("#0", width=00, minwidth=50, stretch=NO)
        self.tabela_garantia.column("#1", width=100, minwidth=50, stretch=NO)
        self.tabela_garantia.column("#2", width=100, minwidth=50, stretch=NO)
        self.tabela_garantia.column("#3", width=80, minwidth=50, stretch=NO)
        self.tabela_garantia.column("#4", width=100, minwidth=50, stretch=NO)
        self.tabela_garantia.column("#5", width=80, minwidth=50, stretch=NO)
        self.tabela_garantia.column("#6", width=100, minwidth=50, stretch=NO)
        self.tabela_garantia.column("#7", width=100, minwidth=50, stretch=NO)
        self.tabela_garantia.place(relx=0.01, rely=0.10, relwidth=0.98, relheight=0.8)

        # select da tabela
        self.tabela_garantia.delete(*self.tabela_garantia.get_children())
        self.conecta_BD()
        lista = self.cursor.execute(""" SELECT NOME,telefone,Marca,modelo,id_smart,convert(char,data_sai,3),descricao FROM clientes 
        INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
        where data_sai >= dateadd(MONTH, -3, getdate())
        ORDER BY nome ASC; """)

        for (nome, telefone, marca, modelo, id_smart, data, descricao) in lista:
            self.tabela_garantia.insert("", "end", values=(nome, telefone, marca, modelo, id_smart, data, descricao))

    def tela_aparelhos(self):

        tela3 = Toplevel()
        tela3.title("CenTEC")
        tela3.config(background="#006669")
        tela3.geometry("800x500")
        tela3.resizable(True, True)
        tela3.maxsize(width=1000, height=700)
        tela3.minsize(width=100, height=70)

        # label
        self.lb_descricao = Label(tela3, text="APARELHOS", fg="white", bg="#006669",
                                  font=("candara", "20", "bold italic"))
        self.lb_descricao.place(relx=0.4, rely=0.02, relwidth=0.20, relheight=0.10)
#BOTOES
        self.bot_excluir = atk.Button3d(tela3, bg="#1EAAF1", text="EXCLUIR",
                                      command=self.delete_smart)
        self.bot_excluir.place(relx=0.03, rely=0.02, relwidth=0.10, relheight=0.08)

        self.entrada_id_delete = Entry(tela3)
        self.entrada_id_delete.place(relx=0.15, rely=0.03, relwidth=0.10, relheight=0.05)

        self.bot_voltar = atk.Button3d(tela3, bg="#1EAAF1", text="Voltar",
                                        command=tela3.destroy)
        self.bot_voltar.place(relx=0.87, rely=0.90, relwidth=0.1, relheight=0.08)

# frame da tela

        self.frame_aparelhos2 = Frame(tela3, bd=2, bg="#006675", highlightbackground="#006675",
                                      highlightthickness=4)
        self.frame_aparelhos2.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.80)

        #
        self.tabela_aparelhos = ttk.Treeview(self.frame_aparelhos2, height=4,
                                             columns=("coluna0", "coluna1", "coluna2", "coluna3", "colun4", "coluna5",
                                                      "coluna6", "coluna7", "coluna8"))
        self.tabela_aparelhos.heading("#1", text="NOME")
        self.tabela_aparelhos.heading("#2", text="TELEFONE")
        self.tabela_aparelhos.heading("#3", text="MARCA")
        self.tabela_aparelhos.heading("#4", text="MODELO")
        self.tabela_aparelhos.heading("#5", text="ID_SMART")
        self.tabela_aparelhos.heading("#6", text="ORÇAMENTO")
        self.tabela_aparelhos.heading("#7", text="DESCRIÇÃO")
        self.tabela_aparelhos.heading("#8", text="STATUS")
        self.tabela_aparelhos.column("#0", width=00, minwidth=80, stretch=NO)
        self.tabela_aparelhos.column("#1", width=100, minwidth=80, stretch=NO)
        self.tabela_aparelhos.column("#2", width=80, minwidth=80, stretch=NO)
        self.tabela_aparelhos.column("#3", width=70, minwidth=80, stretch=NO)
        self.tabela_aparelhos.column("#4", width=80, minwidth=80, stretch=NO)
        self.tabela_aparelhos.column("#5", width=80, minwidth=80, stretch=NO)
        self.tabela_aparelhos.column("#6", width=80, minwidth=80, stretch=NO)
        self.tabela_aparelhos.column("#7", width=150, minwidth=80, stretch=NO)
        self.tabela_aparelhos.column("#8", width=100, minwidth=80, stretch=NO)

        self.tabela_aparelhos.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
        self.select_aparelhos()

    def tela_orcamento(self):
        orcamento = Toplevel()
        orcamento.title("CenTEC")
        orcamento.config(background="#006669")
        orcamento.geometry("1000x500")
        orcamento.resizable(True, True)
        orcamento.maxsize(width=1000, height=700)
        orcamento.minsize(width=100, height=70)

        # label orçamento
        self.lb_descricao = Label(orcamento, text="ORÇAMENTO", fg="white", bg="#006669",
                                  font=("candara", "20", "bold italic"))
        self.lb_descricao.place(relx=0.4, rely=0.02, relwidth=0.20, relheight=0.10)

        # frame da tela

        self.frame_orcamento = Frame(orcamento, bd=2, bg="#006675", highlightbackground="#006675",
                                     highlightthickness=4)
        self.frame_orcamento.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.20)
        # botoes
        self.bot_atualiza = atk.Button3d(orcamento, text="atualizar orçamento", command=self.up_orcamento, bg="#1EAAF1")
        self.bot_atualiza.place(relx=0.84, rely=0.325, relwidth=0.132, relheight=0.10)

        self.bot_ok = atk.Button3d(orcamento, text="OK", command=self.faz_orcamento, bg="#1EAAF1")
        self.bot_ok.place(relx=0.37, rely=0.3, relwidth=0.05, relheight=0.05)

        self.bot_ok = atk.Button3d(orcamento, text="voltar", command=orcamento.destroy, bg="#1EAAF1")
        self.bot_ok.place(relx=0.85, rely=0.8, relwidth=0.1, relheight=0.1)


        # preço da peça
        self.lb_valor_peca = Label(orcamento, text="Valor da peça", fg="white", bg="#006675",
                                   font=("candara", "15", "bold italic"))
        self.lb_valor_peca.place(relx=0.01, rely=0.3, relwidth=0.25, relheight=0.05)
        self.entrada_valor_peca = Entry(orcamento)
        self.entrada_valor_peca.place(relx=0.25, rely=0.3, relwidth=0.12, relheight=0.05)
        # orçamento com garantia
        self.lb_cgarantia = Label(orcamento, text="com garantia", fg="white", bg="#006675",
                                  font=("candara", "15", "bold italic"))
        self.lb_cgarantia.place(relx=0.420, rely=0.3, relwidth=0.25, relheight=0.05)
        self.entrada_cgarantia = Entry(orcamento)
        self.entrada_cgarantia.place(relx=0.70, rely=0.3, relwidth=0.12, relheight=0.05)
        # sem garantia
        self.lb_sgarantia = Label(orcamento, text="sem garantia", fg="white", bg="#006675",
                                  font=("candara", "15", "bold italic"))
        self.lb_sgarantia.place(relx=0.415, rely=0.4, relwidth=0.25, relheight=0.05)
        self.entrada_sgarantia = Entry(orcamento)
        self.entrada_sgarantia.place(relx=0.70, rely=0.4, relwidth=0.12, relheight=0.05)

        self.tabela_aparelhos = ttk.Treeview(self.frame_orcamento, height=9,
                                             columns=("coluna0", "coluna1", "coluna2", "coluna3", "colun4", "coluna5",
                                                      "coluna6", "coluna7", "coluna8", "coluna9", "COLUNA10"))
        self.tabela_aparelhos.heading("#1", text="NOME")
        self.tabela_aparelhos.heading("#2", text="TELEFONE")
        self.tabela_aparelhos.heading("#3", text="MARCA")
        self.tabela_aparelhos.heading("#4", text="MODELO")
        self.tabela_aparelhos.heading("#5", text="ID_SMART")
        self.tabela_aparelhos.heading("#6", text="PROBLEMA")
        self.tabela_aparelhos.heading("#7", text="ORÇAMENTO COM\n GARANTIA")
        self.tabela_aparelhos.heading("#8", text="ORÇAMENTO SEM\n GARANTIA")
        self.tabela_aparelhos.heading("#9", text="DESCRIÇÃO")
        self.tabela_aparelhos.heading("#10", text="STATUS")

        self.tabela_aparelhos.column("#0", width=00, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#1", width=100, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#2", width=80, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#3", width=70, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#4", width=80, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#5", width=70, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#6", width=80, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#7", width=130, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#8", width=130, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#9", width=100, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#9", width=100, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#10", width=100, minwidth=100, stretch=NO)

        self.tabela_aparelhos.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
        self.passar_orcamento()

    def telas(self):
        telas = Toplevel()
        telas.title("CenTec")
        telas.config(background="#006666")
        telas.geometry("1200x600")
        telas.resizable(True, True)
        telas.maxsize(width=1000, height=700)
        telas.minsize(width=100, height=70)


# frames
        self.frame_telas = Frame(telas, bd=2, bg="#006670", highlightbackground="#006670", highlightthickness=4)
        self.frame_telas.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.50)

        self.frame_telas2 = Frame(telas, bd=2, bg="#006680", highlightbackground="#006670",
                                      highlightthickness=4)
        self.frame_telas2.place(relx=0.01, rely=0.51, relwidth=0.98, relheight=0.4)

        self.frame_telas3 = Frame(telas, bd=2, bg="#006670", highlightbackground="#006670", highlightthickness=4)
        self.frame_telas3.place(relx=0.01, rely=0.88, relwidth=0.98, relheight=0.1)

#labels
        self.marca = Label(self.frame_telas,text="Marca", fg="black", bg="#006675",
                             font=("candara", "15", "bold italic"))
        self.marca.place(relx=0.02, rely=0.035, relwidth=0.10, relheight=0.09)

        self.modelo = Label(self.frame_telas,text="Modelo", fg="black", bg="#006675",
                             font=("candara", "15", "bold italic"))
        self.modelo.place(relx=0.02, rely=0.40, relwidth=0.10, relheight=0.09)

        self.condicoes = Label(self.frame_telas,text="Condiçoes", fg="black", bg="#006675",
                             font=("candara", "15", "bold italic"))
        self.condicoes.place(relx=0.02, rely=0.25, relwidth=0.10, relheight=0.09)

        self.descricao = Label(self.frame_telas,text="Descrição", fg="black", bg="#006675",
                             font=("candara", "15", "bold italic"))
        self.descricao.place(relx=0.02, rely=0.55, relwidth=0.10, relheight=0.09)

        self.fornecedor = Label(self.frame_telas, text="Fornecedor", fg="black", bg="#006675",
                               font=("candara", "15", "bold italic"))
        self.fornecedor.place(relx=0.02, rely=0.7, relwidth=0.10, relheight=0.09)
#entrys
        self.entrada_modelo = Entry(self.frame_telas)
        self.entrada_modelo.place(relx=0.15, rely=0.40, relwidth=0.1, relheight=0.10)

        self.entrada_descricao = Entry(self.frame_telas)
        self.entrada_descricao.place(relx=0.15, rely=0.55, relwidth=0.1, relheight=0.10)

        self.entrada_fornecedor = Entry(self.frame_telas)
        self.entrada_fornecedor.place(relx=0.15, rely=0.7, relwidth=0.10, relheight=0.1)

        self.entrada_excluir_tela = Entry(self.frame_telas3)
        self.entrada_excluir_tela.place(relx=0.02, rely=0.2, relwidth=0.1, relheight=0.50)

# botao add fornecedore
        self.bot_add_forecedores = atk.Button3d(self.frame_telas, text="ADD fornecedor", command=self.bot_add_fornecedor, bg="#006675")
        self.bot_add_forecedores.place(relx=0.63, rely=0.02, relwidth=0.15, relheight=0.15)
# botao add tela
        self.bot_add_tela = atk.Button3d(self.frame_telas, text="ADD tela", command=self.adiciona_tela, bg="#006675")
        self.bot_add_tela.place(relx=0.3, rely=0.525, relwidth=0.15, relheight=0.15)
# botao excluir tela
        self.bot_excluir_tela = atk.Button3d(self.frame_telas3, text="excluir tela", command=self.exclui_tela, bg="#006675")
        self.bot_excluir_tela.place(relx=0.13, rely=0.1, relwidth=0.10, relheight=0.80)
# botao voltar
        self.bot_voltar = atk.Button3d(self.frame_telas, text="voltar",bg="#006690",command=telas.destroy)
        self.bot_voltar.place(relx=0.9, rely=0.02, relwidth=0.1, relheight=0.13)
# botoes de busca
        # botao samsung
        self.bot_busca_samsung = atk.Button3d(self.frame_telas, text="Samsung", bg="#006680", command=self.select_telas_samsung)
        self.bot_busca_samsung.place(relx=0.0, rely=0.88, relwidth=0.12, relheight=0.13)
        # botao xiaomi
        self.bot_busca_Xiaomi = atk.Button3d(self.frame_telas, text="Xiaomi", bg="#006680", command=self.select_telas_xiaomi)
        self.bot_busca_Xiaomi.place(relx=0.15, rely=0.88, relwidth=0.12, relheight=0.13)
        # botao motorola
        self.bot_busca_motorola = atk.Button3d(self.frame_telas, text="Motorola", bg="#006680", command=self.select_telas_motorola)
        self.bot_busca_motorola.place(relx=0.3, rely=0.88, relwidth=0.12, relheight=0.13)
        # botao Iphone
        self.bot_busca_iphone = atk.Button3d(self.frame_telas, text="Iphone", bg="#006680", command=self.select_telas_iphone)
        self.bot_busca_iphone.place(relx=0.45, rely=0.88, relwidth=0.12, relheight=0.13)
        # botao lg
        self.bot_busca_lg = atk.Button3d(self.frame_telas, text="LG", bg="#006680", command=self.select_telas_lg)
        self.bot_busca_lg.place(relx=0.60, rely=0.88, relwidth=0.12, relheight=0.13)
        # botao Asus
        self.bot_busca_asus = atk.Button3d(self.frame_telas, text="Asus", bg="#006680", command=self.select_telas_asus)
        self.bot_busca_asus.place(relx=0.75, rely=0.88, relwidth=0.12, relheight=0.13)
        # botao outros
        self.bot_busca_outros = atk.Button3d(self.frame_telas, text="Todos", bg="#006680", command=self.select_tabela_telas)
        self.bot_busca_outros.place(relx=0.90, rely=0.88, relwidth=0.1, relheight=0.13)

# chek box
        self.marca_tela = IntVar()

        self.condicao = IntVar()

        self.chec= Checkbutton(self.frame_telas, text="Motorola", fg="black", bg="#006675", onvalue=1, offvalue=0,
                                variable=self.marca_tela,
                                command=self.seleciona_marca_tela)
        self.chec.place(relx=0.15, rely=0.02, relwidth=0.125, relheight=0.05)

        self.chec = Checkbutton(self.frame_telas, text="Samsung", fg="black", bg="#006675", onvalue=2, offvalue=0,
                                variable=self.marca_tela,command=self.seleciona_marca_tela)
        self.chec.place(relx=0.15, rely=0.10, relwidth=0.125, relheight=0.05)

        self.chec = Checkbutton(self.frame_telas, text="Xiaomi", fg="black", bg="#006675", onvalue=3, offvalue=0,
                                variable=self.marca_tela,command=self.seleciona_marca_tela)
        self.chec.place(relx=0.30, rely=0.02, relwidth=0.125, relheight=0.05)
        self.chec = Checkbutton(self.frame_telas, text="LG", fg="black", bg="#006675", onvalue=4, offvalue=0,
                                variable=self.marca_tela,command=self.seleciona_marca_tela)
        self.chec.place(relx=0.288, rely=0.10, relwidth=0.125, relheight=0.05)
        self.chec = Checkbutton(self.frame_telas, text="Asus", fg="black", bg="#006675", onvalue=5, offvalue=0,
                                variable=self.marca_tela,command=self.seleciona_marca_tela)
        self.chec.place(relx=0.4, rely=0.02, relwidth=0.125, relheight=0.05)
        self.chec = Checkbutton(self.frame_telas, text="Iphone", fg="black", bg="#006675", onvalue=6, offvalue=0,
                                variable=self.marca_tela,command=self.seleciona_marca_tela)
        self.chec.place(relx=0.406, rely=0.10, relwidth=0.125, relheight=0.05)


        self.chec = Checkbutton(self.frame_telas, text="Nova", fg="black", bg="#006675", onvalue=1, offvalue=0,
                                variable=self.condicao,command=self.seleciona_marca_tela)
        self.chec.place(relx=0.139, rely=0.25, relwidth=0.125, relheight=0.05)
        self.chec = Checkbutton(self.frame_telas, text="Usada", fg="black", bg="#006675", onvalue=2, offvalue=0,
                                variable=self.condicao,command=self.seleciona_marca_tela)
        self.chec.place(relx=0.298, rely=0.25, relwidth=0.125, relheight=0.05)

        self.select_tabela_telas()

    def tela_informacoes (self):
        info = Toplevel()
        info.title("CenTEC")
        info.config(background="#006669")
        info.geometry("1400x300")
        info.resizable(True, True)


        # label orçamento
        self.lb_descricao = Label(info, text="INFORMAÇOES DO SMARTPHONE", fg="white", bg="#006669",
                                  font=("candara", "20", "bold italic"))
        self.lb_descricao.place(relx=0.32, rely=0.02, relwidth=0.30, relheight=0.10)

        # frame da tela

        self.frame_info = Frame(info, bd=2, bg="#006675", highlightbackground="#006675",
                                     highlightthickness=4)
        self.frame_info.place(relx=0.01, rely=0.2, relwidth=0.98, relheight=0.70)


        self.tabela_aparelhos = ttk.Treeview(self.frame_info, height=9,
                                             columns=("coluna0", "coluna1", "coluna2", "coluna3", "colun4", "coluna5",
                                                      "coluna6", "coluna7", "coluna8", "coluna9", "COLUNA10","COLUNA11","COLUNA12","COLUNA13","COLUNA14"))
        self.tabela_aparelhos.heading("#1", text="id_cliente")
        self.tabela_aparelhos.heading("#2", text="NOME")
        self.tabela_aparelhos.heading("#3", text="TELEFONE")
        self.tabela_aparelhos.heading("#4", text="MARCA")
        self.tabela_aparelhos.heading("#5", text="MODELO")
        self.tabela_aparelhos.heading("#6", text="ID_SMART")
        self.tabela_aparelhos.heading("#7", text="PROBLEMA")
        self.tabela_aparelhos.heading("#8", text="Orçamento com\ngarantia")
        self.tabela_aparelhos.heading("#9", text="Orçamento sem\ngarantia")
        self.tabela_aparelhos.heading("#10", text="DESCRIÇÃO")
        self.tabela_aparelhos.heading("#11", text="STATUS")
        self.tabela_aparelhos.heading("#12", text="data de entrada")
        self.tabela_aparelhos.heading("#13", text="data de saída")

        self.tabela_aparelhos.column("#0", width=0, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#1", width=70, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#2", width=90, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#3", width=80, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#4", width=80, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#5", width=70, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#6", width=80, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#7", width=130, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#8", width=130, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#9", width=100, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#10", width=130, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#11", width=100, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#12", width=120, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#13", width=120, minwidth=100, stretch=NO)
        self.tabela_aparelhos.column("#14", width=100, minwidth=100, stretch=NO)


        self.tabela_aparelhos.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
        self.select_informaçoes()




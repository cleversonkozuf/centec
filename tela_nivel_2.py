

from funçoes import *

class nivel_2():

    def tela_consultar_db(self):
        consultar = Tk()
        consultar.title("CenTEC")
        consultar.config(background="#006669")
        consultar.geometry("700x500")
        consultar.resizable(True, True)
        consultar.maxsize(width=1000, height=700)
        consultar.minsize(width=100, height=70)

        # frame da tela 3
        self.frame_consultar = Frame(consultar,bd=2, bg='#006675', highlightbackground="#006670", highlightthickness=4)
        self.frame_consultar.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.2)
        self.frame_consultar2 = Frame(consultar,bd=2, bg="#006670", highlightbackground="#006670", highlightthickness=4)
        self.frame_consultar2.place(relx=0.01, rely=0.21, relwidth=0.98, relheight=0.78)

        # botoes da tela 3
        self.bot_excluir = atk.Button3d(self.frame_consultar, bg="#1EAAF1", text="excluir", fg="white",
                                        command=self.tela_inicial)
        self.bot_excluir.place(relx=0.02, rely=0.20, relwidth=0.30, relheight=0.60)

        self.bot_dell = atk.Button3d(self.frame_consultar, bg="#1EAAF1", text="editar clientes",
                                     command=self.tela_editar_clientes)
        self.bot_dell.place(relx=0.35, rely=0.20, relwidth=0.30, relheight=0.60)



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
        # barra de rolagem
        self.scrool = Scrollbar(self.frame_consultar2, orient="vertical")
        self.tabela_bd.configure(xscrollcommand=self.scrool.set)
        self.scrool.place(relx=0.96, rely=0.05, relwidth=0.02, relheight=0.89)
        # select da tabela
        self.tabela_bd.delete(*self.tabela_bd.get_children())
        self.conecta_BD()
        lista = self.cursor.execute(""" SELECT id_cliente, nome, telefone, convert(char,data_registro,3)  FROM clientes
        ORDER BY nome ASC; """)
        for (id, nome, telefone, data) in lista:
            self.tabela_bd.insert("", "end", values=(id, nome, telefone, data))

    def tela_garantia(self):
        tela4 = Tk()
        tela4.title("CenTEC")
        tela4.config(background="#006666")
        tela4.geometry("700x500")
        tela4.resizable(True, True)
        tela4.maxsize(width=1000, height=700)
        tela4.minsize(width=100, height=70)

        self.lb_descricao = Label(tela4, text="GARANTIA ATIVA", fg="white", bg="#006669",
                                  font=("candara", "20", "bold italic"))
        self.lb_descricao.place(relx=0.325, rely=0.02, relwidth=0.40, relheight=0.10)

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
        self.tabela_garantia.place(relx=0.01, rely=0.10, relwidth=0.98, relheight=0.98)
        # barra de rolagem
        self.scrool = Scrollbar(self.tabela_garantia, orient="vertical")
        self.tabela_garantia.configure(xscrollcommand=self.scrool.set)
        self.scrool.place(relx=0.96, rely=0.05, relwidth=0.02, relheight=0.89)
        # select da tabela
        self.tabela_garantia.delete(*self.tabela_garantia.get_children())
        self.conecta_BD()
        # lista = self.cursor.execute(""" SELECT id_cliente, nome, telefone, convert(char,data_registro,3)  FROM clientes
        # ORDER BY nome ASC; """)
        lista = self.cursor.execute(""" SELECT NOME,telefone,Marca,modelo,id_smart,convert(char,data_sai,3),descricao FROM clientes 
        INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
        where data_sai >= dateadd(MONTH, -3, getdate())
        ORDER BY nome ASC; """)

        for (nome, telefone, marca, modelo, id_smart, data, descricao) in lista:
            self.tabela_garantia.insert("", "end", values=(nome, telefone, marca, modelo, id_smart, data, descricao))

    def tela_aparelhos(self):

        tela3 = Tk()
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

        # frame da tela

        self.frame_aparelhos2 = Frame(tela3, bd=2, bg="#006675", highlightbackground="#006675",
                                      highlightthickness=4)
        self.frame_aparelhos2.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.88)

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
        self.tabela_aparelhos.column("#5", width=60, minwidth=80, stretch=NO)
        self.tabela_aparelhos.column("#6", width=80, minwidth=80, stretch=NO)
        self.tabela_aparelhos.column("#7", width=150, minwidth=80, stretch=NO)
        self.tabela_aparelhos.column("#8", width=80, minwidth=80, stretch=NO)

        self.tabela_aparelhos.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
        # barra de rolagem
        self.scrool = Scrollbar(self.frame_aparelhos2, orient="vertical")
        self.tabela_aparelhos.configure(xscrollcommand=self.scrool.set)
        self.scrool.place(relx=0.96, rely=0.05, relwidth=0.02, relheight=0.89)
        # select da tabela
        self.tabela_aparelhos.delete(*self.tabela_aparelhos.get_children())
        self.conecta_BD()
        lista = self.cursor.execute("""SELECT NOME,telefone,Marca,modelo,id_smart,orcamento,descricao,situacao AS Status FROM clientes 
            INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
            ORDER BY nome ASC;""")

        for (id, cod, marca, modelo, orcamento, data, descricao, status) in lista:
            self.tabela_aparelhos.insert("", "end", values=(id, cod, marca, modelo, orcamento, data, descricao, status))

    def tela_editar_clientes(self):
        tela4 = Tk()
        tela4.title("CenTE")
        tela4.config(background="#006666")
        tela4.geometry("700x500")
        tela4.resizable(True, True)
        tela4.maxsize(width=1000, height=700)
        tela4.minsize(width=100, height=70)


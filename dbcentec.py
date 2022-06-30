import pyodbc
from tkinter import *
from tkinter import ttk
import awesometkinter as atk



root = Tk()
#conecta bd
class funcs():
    def limpa_tela(self):
        self.entrada_cpf.delete(0,END)
        self.entrada_nome.delete(0, END)
        self.entrada_telefone.delete(0,END)
    def limpa_tela_inicial(self):
        self.entrada_nome_i.delete(0, END)
    def conecta_BD(self):
        conn = pyodbc.connect(DRIVER="SQL Server",
                                 Server='CLEVERSON\DB_CENTRAL',
                                 database='bd_central')
        print("conexao feita")
        self.cursor = conn.cursor()
    def desconecta_bd(self):
        self.cursor.close();print("Desconectando ao banco de dados BD_Central_tec")
#tela 2
class tela_nivel_2():
    def tela_add_clientes(self):
        #formaçao da tela
        tela2=Tk()
        tela2.title("CenTEC")
        tela2.config(background="#006669")
        tela2.geometry("700x500")
        tela2.resizable(True,True)
        tela2.maxsize(width=1000,height=700)
        tela2.minsize(width=100,height=70)

        self.frame_add_clientes = Frame(bd=0.02, bg='#006675', highlightbackground="#006670", highlightthickness=0.04)
        self.frame_add_clientes.place(relx=0.015, rely=0.02, relwidth=0.97, relheight=0.96)

        #BOTOES
        self.bot_add = atk.Button3d(self.frame_add_clientes, text="ADD Cliente",command = self.adicione_cliente, bg="#1EAAF1")
        self.bot_add.place(relx=0.45, rely=0.70, relwidth=0.20, relheight=0.10)
        self.bot_add = atk.Button3d(self.frame_add_clientes, text="LIMPAR", command=self.limpa_tela,bg="#1EAAF1")
        self.bot_add.place(relx=0.80, rely=0.3, relwidth=0.15, relheight=0.10)
        self.bot_add = atk.Button3d(self.frame_add_clientes, text="ADD \naparelho", command=self.tela_entrada_saida_aparelhos, bg="#1EAAF1")
        self.bot_add.place(relx=0.76, rely=0.85, relwidth=0.20, relheight=0.10)

        #adiconando labels  clientes
        self.lb_cpf = Label(self.frame_add_clientes,text="CPF do cliente",fg="white" ,bg="#006675", font=("candara", "22", "bold italic"))
        self.lb_cpf.place(relx=0.02, rely=0.50, relwidth=0.30, relheight=0.10)
        # codigo de entrada cpf
        self.entrada_cpf = Entry(self.frame_add_clientes)
        self.entrada_cpf.place(relx=0.35, rely=0.50, relwidth=0.40, relheight=0.10)

        #label nome
        self.lb_nome = Label(self.frame_add_clientes, text="Nome",fg="white" ,bg="#006675", font=("candara", "22", "bold italic"))
        self.lb_nome.place(relx=0.02, rely=0.10, relwidth=0.30, relheight=0.10)
        # codigo de entrada nome
        self.entrada_nome = Entry(self.frame_add_clientes)
        self.entrada_nome.place(relx=0.35, rely=0.10, relwidth=0.40, relheight=0.10)

        #label telefone
        self.lb_telefone = Label(self.frame_add_clientes, text="Telefone",fg="white" ,bg="#006675", font=("candara", "22", "bold italic"))
        self.lb_telefone.place(relx=0.02, rely=0.30, relwidth=0.30, relheight=0.10)
        # codigo de entrada telefone
        self.entrada_telefone = Entry(self.frame_add_clientes)
        self.entrada_telefone.place(relx=0.35, rely=0.30, relwidth=0.40, relheight=0.10)


        #adiconando dadod no db
    def adicione_cliente(self):
        self.cpf = self.entrada_cpf.get()
        self.nome = self.entrada_nome.get()
        self.telefone = self.entrada_telefone.get()
        self.conecta_BD(); print("conectando")
        #self.monta_tables()
        self.cursor.execute( """ INSERT INTO dbo.clientes (nome, telefone, cpf, data_registro)
        VALUES (?,?,?,getdate())""", (self.nome,self.telefone,self.cpf))
        
        self.cursor.commit()
        self.desconecta_bd()
        self.select()
        self.limpa_tela()
    def tela_consultar_db(self):
        tela3 = Tk()
        tela3.title("CenTEC")
        tela3.config(background="#006669")
        tela3.geometry("700x500")
        tela3.resizable(True,True)
        tela3.maxsize(width=1000,height=700)
        tela3.minsize(width=100,height=70)

        #frame da tela 3
        self.frame_consultar = Frame(bd=2, bg='#006675', highlightbackground="#006670", highlightthickness=4)
        self.frame_consultar.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.2)
        self.frame_consultar2 = Frame(bd=2, bg="#006670", highlightbackground="#006670", highlightthickness=4)
        self.frame_consultar2.place(relx=0.01, rely=0.21, relwidth=0.98, relheight=0.78)

        # botoes da tela 3
        self.bot_excluir = atk.Button3d(self.frame_consultar,bg="#1EAAF1", text="excluir",fg="white", command=self.tela_inicial)
        self.bot_excluir.place(relx=0.02, rely=0.20, relwidth=0.30, relheight=0.60)

        self.bot_dell = atk.Button3d(self.frame_consultar, bg="#1EAAF1", text="editar clientes", command=self.tela_editar_clientes)
        self.bot_dell.place(relx=0.35, rely=0.20, relwidth=0.30, relheight=0.60)

        self.bot_add_cliente = atk.Button3d(self.frame_consultar,bg="#1EAAF1" ,text="ADD Clientes",command=self.tela_add_clientes)
        self.bot_add_cliente.place(relx=0.68,rely=0.20,relwidth=0.30,relheight=0.60)


        #tabela do banco de dados da tela 3
        self.tabela_bd = ttk.Treeview(self.frame_consultar2,height=4,
                                   columns=("coluna0", "coluna1", "coluna2", "coluna3","coluna4"))
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
        #select da tabela
        self.tabela_bd.delete(*self.tabela_bd.get_children())
        self.conecta_BD()
        lista = self.cursor.execute(""" SELECT id_cliente, nome, telefone, convert(char,data_registro,3)  FROM clientes
        ORDER BY nome ASC; """)
        for (id,nome,telefone,data) in lista:
            self.tabela_bd.insert("", "end", values=(id,nome,telefone,data))
    def tela_garantia(self):
        tela4=Tk()
        tela4.title("CenTEC")
        tela4.config(background="#006666")
        tela4.geometry("700x500")
        tela4.resizable(True,True)
        tela4.maxsize(width=1000,height=700)
        tela4.minsize(width=100,height=70)

        self.lb_descricao = Label(tela4, text="GARANTIA ATIVA", fg="white", bg="#006669",
                                  font=("candara", "20", "bold italic"))
        self.lb_descricao.place(relx=0.325, rely=0.02, relwidth=0.40, relheight=0.10)

        #tabela da garantia
        self.tabela_garantia = ttk.Treeview(tela4,height=4,
                                   columns=("coluna0", "coluna1", "coluna2", "coluna3", "coluna4","coluna5","coluna6","coluna7"))
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
        #select da tabela
        self.tabela_garantia.delete(*self.tabela_garantia.get_children())
        self.conecta_BD()
        #lista = self.cursor.execute(""" SELECT id_cliente, nome, telefone, convert(char,data_registro,3)  FROM clientes
        #ORDER BY nome ASC; """)
        lista = self.cursor.execute(""" SELECT NOME,telefone,Marca,modelo,id_smart,convert(char,data_sai,3),descricao FROM clientes 
        INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
        where data_sai >= dateadd(MONTH, -3, getdate())
        ORDER BY nome ASC; """)

        for (nome,telefone,marca,modelo,id_smart,data,descricao) in lista:
            self.tabela_garantia.insert("", "end", values=(nome,telefone,marca,modelo,id_smart,data,descricao))

    def tela_entrada_saida_aparelhos(self):
        tela5=Tk()
        tela5.title("CenTEC")
        tela5.config(background="#006666")
        tela5.geometry("700x500")
        tela5.resizable(True,True)
        tela5.maxsize(width=1000,height=700)
        tela5.minsize(width=100,height=70)

        self.frame_entrada = Frame(bd=0.02, bg='#006675', highlightbackground="#006670", highlightthickness=0.04)
        self.frame_entrada.place(relx=0.015, rely=0.02, relwidth=0.97, relheight=0.96)

        #botoes
        self.bot_entrada = atk.Button3d(self.frame_entrada, text="ADD", command=self.adiciona_smart, bg="#1EAAF1")
        self.bot_entrada.place(relx=0.7, rely=0.46, relwidth=0.15, relheight=0.1)
        self.bot_saida = atk.Button3d(self.frame_entrada, text="dar baixa", command=self.dar_baixa, bg="#1EAAF1")
        self.bot_saida.place(relx=0.35, rely=0.70, relwidth=0.20, relheight=0.10)

        # label id cliente
        self.lb_id_cliente = Label(self.frame_entrada, text="ID CLIENTE",fg="white" ,bg="#006675", font=("candara", "10", "bold italic"))
        self.lb_id_cliente.place(relx=0.66, rely=0.24, relwidth=0.10, relheight=0.05)
        # codigo de entrada ID DO cliente
        self.entrada_id_cliente = Entry(self.frame_entrada)
        self.entrada_id_cliente.place(relx=0.85, rely=0.24, relwidth=0.10, relheight=0.05)

        #label id do funcionario
        self.lb_id_funcionario = Label(self.frame_entrada, text="ID FUNCIONÁRIO",fg="white" ,bg="#006675", font=("candara", "10", "bold italic"))
        self.lb_id_funcionario.place(relx=0.66, rely=0.36, relwidth=0.15, relheight=0.05)
        # codigo de entrad id do funcionario
        self.entrada_id_funcionario = Entry(self.frame_entrada)
        self.entrada_id_funcionario.place(relx=0.85, rely=0.36, relwidth=0.10, relheight=0.05)



        #id do aparelho para dar baixa
        self.lb_id_smartphone = Label(self.frame_entrada, text="ID Aparelho",fg="white" ,bg="#006675", font=("candara", "10", "bold italic"))
        self.lb_id_smartphone.place(relx=0.02, rely=0.72, relwidth=0.15, relheight=0.05)
        self.entrada_id_smartphone = Entry(self.frame_entrada)
        self.entrada_id_smartphone.place(relx=0.21, rely=0.72, relwidth=0.10, relheight=0.05)

        # codigo de entrada marca
        self.lb_marca = Label(self.frame_entrada, text="Marca",fg="white" ,bg="#006675", font=("candara", "22", "bold italic"))
        self.lb_marca.place(relx=0.02, rely=0.10, relwidth=0.30, relheight=0.10)
        # codigo de entrda marca
        self.entrada_marca = Entry(self.frame_entrada)
        self.entrada_marca.place(relx=0.35, rely=0.10, relwidth=0.30, relheight=0.10)

        # entrada do modelo do aparelho
        self.lb_model = Label(self.frame_entrada, text="Modelo",fg="white" ,bg="#006675", font=("candara", "22", "bold italic"))
        self.lb_model.place(relx=0.02, rely=0.22, relwidth=0.30, relheight=0.10)
        # codigo de entrada modelo do aparelho
        self.entrada_model = Entry(self.frame_entrada)
        self.entrada_model.place(relx=0.35, rely=0.22, relwidth=0.30, relheight=0.10)


        # entrada do modelo do aparelho
        self.lb_orcamento = Label(self.frame_entrada, text="Orcamento",fg="white" ,bg="#006675", font=("candara", "22", "bold italic"))
        self.lb_orcamento.place(relx=0.02, rely=0.34, relwidth=0.30, relheight=0.10)
        # codigo de entrada modelo do aparelho
        self.entrada_orcamento = Entry(self.frame_entrada)
        self.entrada_orcamento.place(relx=0.35, rely=0.34, relwidth=0.30, relheight=0.10)

     # adiconando labels  descriçao
        self.lb_descricao = Label(self.frame_entrada, text="Descrição",fg="white" ,bg="#006675", font=("candara", "22", "bold italic"))
        self.lb_descricao.place(relx=0.02, rely=0.46, relwidth=0.30, relheight=0.10)
        # codigo de entrada descriçao
        self.entrada_descricao = Entry(self.frame_entrada)
        self.entrada_descricao.place(relx=0.35, rely=0.46, relwidth=0.30, relheight=0.10)
    def tela_aparelhos(self):

          tela3 = Tk()
          tela3.title("CenTEC")
          tela3.config(background="#006669")
          tela3.geometry("800x500")
          tela3.resizable(True,True)
          tela3.maxsize(width=1000, height=700)
          tela3.minsize(width=100, height=70)

          #label
          self.lb_descricao = Label(tela3, text="APARELHOS",fg="white" ,bg="#006669", font=("candara", "20", "bold italic"))
          self.lb_descricao.place(relx=0.4, rely=0.02, relwidth=0.20, relheight=0.10)

          # frame da tela

          self.frame_aparelhos2 = Frame(tela3, bd=2, bg="#006675", highlightbackground="#006675",
                                        highlightthickness=4)
          self.frame_aparelhos2.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.88)



          #
          self.tabela_aparelhos = ttk.Treeview(self.frame_aparelhos2, height=4,
                                               columns=("coluna0", "coluna1", "coluna2", "coluna3", "colun4","coluna5",
                                                        "coluna6","coluna7","coluna8"))
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
          lista = self.cursor.execute("""SELECT NOME,telefone,Marca,modelo,id_smart,orcamento,descricao,STATOS AS Status FROM clientes 
            INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
            ORDER BY nome ASC;""")

          for (id,cod,marca, modelo,orcamento,data,descricao,status) in lista:
              self.tabela_aparelhos.insert("", "end", values=(id,cod,marca,modelo,orcamento,data,descricao,status))

    ##codigo para adiconar o aparelho bo bd
    def adiciona_smart(self):
        self.codigo = self.entrada_id_cliente.get()
        self.marca= self.entrada_marca.get()
        self.modelo = self.entrada_model.get()
        self.orcamento = self.entrada_orcamento.get()
        self.descricao = self.entrada_descricao.get()
        self.id_smart = self.entrada_id_smartphone.get()
        self.id_funcionario = self.entrada_id_funcionario.get()

        self.conecta_BD()
        print("conectando")
        # self.monta_tables()
        self.cursor.execute(""" INSERT INTO dbo.smartphone ( marca, modelo, orcamento,
         data_entrada,descricao,cod_cliente,cod_loja,cod_fun)
               VALUES (?,?,?,getdate(),?,?,2,?)""", (self.marca, self.modelo, self.orcamento,
                                                                    self.descricao,self.codigo, self.id_funcionario))
        self.cursor.commit()
        self.desconecta_bd()
        self.select()
        #self.limpa_tela()
        # insere data de saida ao aparelho
    def dar_baixa(self):
        self.id_smart = self.entrada_id_smartphone.get()
        self.conecta_BD()
        self.cursor.execute(""" UPDATE smartphone SET data_sai = GETDATE(), statos = 1  WHERE id_smart =""" + self.id_smart)

        self.cursor.commit()
        self.desconecta_bd()
    def tela_editar_clientes(self):
        tela4 = Tk()
        tela4.title("CenTE")
        tela4.config(background="#006666")
        tela4.geometry("700x500")
        tela4.resizable(True, True)
        tela4.maxsize(width=1000, height=700)
        tela4.minsize(width=100, height=70)


#tela 1
class aplication(funcs,tela_nivel_2):


    def __init__(self):
        self.root = root
        self.tela_inicial()
        self.frame_da_tela_inicial()
        self.botoes_frame1()
        self.tabela_frame_2()
        #self.monta_tables()
        self.select()
        root.mainloop()

    def tela_inicial(self):
        self.root.title("CenTEC")
        self.root.config(background="#006669")
        self.root.geometry("700x500")
        self.root.resizable(True,True)
        self.root.maxsize(width=1000,height=700)
        self.root.minsize(width=100,height=70)

    def frame_da_tela_inicial(self):
        self.frame_1 = Frame(bd=2,bg="#006675", highlightbackground="#006670",highlightthickness=4)
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight=0.48)
        self.frame_2 = Frame(bd=2,bg="#006670", highlightbackground="#006670",highlightthickness=4)
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight=0.48)

    def botoes_frame1(self):
        #criaçao dos botoes
        self.bot_add = atk.Button3d(self.frame_1,bg="#1EAAF1",text="ADD CLIENTE",command=self.tela_add_clientes)
        self.bot_add.place(relx=0.02,rely=0.05,relwidth=0.40,relheight=0.20)

        self.bot_mostra = atk.Button3d(self.frame_1,bg="#1EAAF1",text="CONSULTAR BD", command= self.tela_consultar_db)
        self.bot_mostra.place(relx=0.02, rely=0.31, relwidth=0.40, relheight=0.20)

        self.bot_mostra = atk.Button3d(self.frame_1, bg="#1EAAF1", text="GARANTIA", command=self.tela_garantia)
        self.bot_mostra.place(relx=0.29, rely=0.56, relwidth=0.40, relheight=0.20)

        self.bot_aparelhos = atk.Button3d(self.frame_1, bg="#1EAAF1", text="ENTRADA E SAÍDA DE APARELHOS",
                                          command=self.tela_entrada_saida_aparelhos)
        self.bot_aparelhos.place(relx=0.58, rely=0.05, relwidth=0.40, relheight=0.20)

        self.bot_aparelhos = atk.Button3d(self.frame_1, bg="#1EAAF1", text="APARELHOS",
                                    command=self.tela_aparelhos)
        self.bot_aparelhos.place(relx=0.58, rely=0.31, relwidth=0.40, relheight=0.20)

        self.bot_limpar = atk.Button3d(self.frame_1,bg="#1EAAF1",text="limpar",command= self.limpa_tela_inicial)
        self.bot_limpar.place(relx=0.75, rely=0.80, relwidth=0.10, relheight=0.20)

        self.bot_buscar =atk.Button3d(self.frame_1,bg="#1EAAF1", text="Buscar",fg="black")
        self.bot_buscar.place(relx=0.89, rely=0.80, relwidth=0.10, relheight=0.20)

        self.bot_saida = atk.Button3d(self.frame_1, text="dar baixa", command=self.dar_baixa, bg="#1EAAF1")
        self.bot_saida.place(relx=0.30, rely=0.80, relwidth=0.12, relheight=0.20)

        self.lb_id_smartphone = Label(self.frame_1, text="ID Aparelho", fg="white", bg="#006675",
                                      font=("candara", "10", "bold italic"))
        self.lb_id_smartphone.place(relx=0.0, rely=0.87, relwidth=0.15, relheight=0.05)

        self.entrada_id_smartphone = Entry(self.frame_1)
        self.entrada_id_smartphone.place(relx=0.15, rely=0.85, relwidth=0.12, relheight=0.10)
        #criaçao das label DO NOME
        self.lb_nome = Label(self.frame_1,text= "Nome \ndo cliente",fg="white" ,bg="#006675", font=("candara", "10", "bold italic"))
        self.lb_nome.place(relx=0.50,rely=0.79,relwidth=0.10,relheight=0.20)
        #codigo de entrada DO NOME
        self.entrada_nome_i = Entry(self.frame_1)
        self.entrada_nome_i.place(relx=0.6,rely=0.85,relwidth=0.12,relheight=0.10)

    def tabela_frame_2(self):
        self.tabela= ttk.Treeview(self.frame_2, height=4, columns=("coluna1","coluna2","coluna3","coluna4","coluna5"))

        self.tabela.heading("#1",text="id")
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
        #barra de rolagem
        self.scrool = Scrollbar(self.frame_2,orient="vertical")
        self.tabela.configure(xscrollcommand=self.scrool.set)
        self.scrool.place(relx=0.96,rely=0.05,relwidth=0.02,relheight=0.89 )
    def select(self):
        self.tabela.delete(*self.tabela.get_children())
        self.conecta_BD()
        dados = self.cursor.execute(""" SELECT id_cliente,NOME,telefone,id_smart FROM clientes 
        INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
        order by id_cliente; """)


        for (id,nome,telefone,id_smart) in dados:
             self.tabela.insert("","end", values=(id,nome,telefone,id_smart))



        self.desconecta_bd()








aplication()

#http://localhost/phpmyadmin/index.php?route=/sql&db=dbcentral&table=pessoas&pos=0
#cor verde escuro(#006666)
#cor azul escuro(#003366)
#site de cores (http://webcalc.com.br/Utilitarios/form/rgb_hex)
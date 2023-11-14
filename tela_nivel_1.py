from modulos import *
from tela_nivel_2 import *

from funçoes import *
root = Tk()


class tela_1 ():
    def tela_inicial(self):
        self.root.title("CenTEC--v 2.0")
        self.root.config(background="#006669")
        self.root.geometry("1000x650")
        self.root.resizable(True, True)

        self.frames()
        self.chek_box()
        self.botoes()
        self.tabela_inicial()
        self.setor_de_busca()


        self.label()





    def frames(self):
# criação dos frames
        self.frame_1 = Frame(bd=2, bg="#006678", highlightbackground="#006670", highlightthickness=4)
        self.frame_1.place(relx=0.00, rely=0.0, relwidth=1, relheight=0.46)

        self.frame_2 = Frame(bd=0, bg="#006670", highlightbackground="#006670")
        self.frame_2.place(relx=0, rely=0.45, relwidth=1, relheight=0.56)


    def chek_box(self):

        self.marcas = StringVar()
        self.marcas.set("Marca")
        self.seleciona_marca = ["Motorola G","Samsung A","Samsung S","Samsung J","Xiaomi","Iphone","Lg",
                                "Asus", "Blu", "Multilaser", "Nokia", "Sony", "Huawei", "Lenovo", "Alcatel", "ZTE","Positivo"]

        self.popupMenu = OptionMenu(self.frame_1, self.marcas, *self.seleciona_marca,command=self.seleciona_modelo)
        self.popupMenu.place(relx=0.15, rely=0.4, relwidth=0.12, relheight=0.1)


        self.escolha_problema = IntVar()
        self.outros_problemas = StringVar()
        self.Tipos = ["Bateria ", "Conector ", "Tela ", "Tampa Traseira ", "Umidade ", "Desbloqueio ", "Sistema ",
                      "Formatação ", "Não Liga ", "Botões ", "Placa ", "Câmera ", "Microfone ", "Alto-Falante ", "Slot-Chip ",
                      "Sensor Proximidade ","Salvar Dados"]
        self.outros_problemas.set("Selecione")
        self.Menu_problemas = OptionMenu(self.frame_1, self.outros_problemas, *self.Tipos, command=self.concatena_problemas)
        self.Menu_problemas.place(relx=0.15, rely=0.52, relwidth=0.12, relheight=0.1)







    def botoes(self):

        self.bot_limpar = atk.Button3d(self.frame_1, bg="#006698", text="Limpar", command=self.limpa_tela)
        self.bot_limpar.place(relx=0.3, rely=0.63, relwidth=0.10, relheight=0.12)
# ADD CLIENTE
        self.bot_add = atk.Button3d(self.frame_1 ,text="  ADD Cliente", command=self.adicione_cliente,bg="#004675")
        self.bot_add.place(relx=0.41, rely=0.14, relwidth=0.1, relheight=0.12)
# CONSULTAR CLIENTE
        self.bot_consultar_clientes = atk.Button3d(self.frame_1, bg="#006675", text="Clientes",
                                                   command=self.tela_consultar_db)
        self.bot_consultar_clientes.place(relx=0.6,rely=0.01, relwidth=0.09, relheight=0.12)

        self.bot_buscar_add = atk.Button3d(self.frame_1, bg="#006675", text="Verificar", fg="white",
                                       command=self.busca_clientes_add)
        self.bot_buscar_add.place(relx=0.42, rely=0.01, relwidth=0.08, relheight=0.12)
#GARANTIA
        self.bot_garantia = atk.Button3d(self.frame_1, bg="#006675", text="Garantia",
                                         command=self.tela_garantia)
        self.bot_garantia.place(relx=0.9, rely=0.01, relwidth=0.09, relheight=0.12)
#ENTRADA DE AAPARELHO
        self.bot_entrada_aparelhos = atk.Button3d(self.frame_1, bg="#004675", text="ADD Aparelho",
                                                  command=self.adiciona_smart)
        self.bot_entrada_aparelhos.place(relx=0.15, rely=0.63, relwidth=0.11, relheight=0.12)
# APARELHOS QUE ESTAO NA LOJA
        self.bot_aparelhos = atk.Button3d(self.frame_1, bg="#006675", text="Aparelhos",
                                          command=self.tela_aparelhos)
        self.bot_aparelhos.place(relx=0.80, rely=0.01, relwidth=0.09, relheight=0.12)
# botao orçamento
        self.bot_orcamento = atk.Button3d(self.frame_1, bg="#006675", text="Orçamento",
                                          command=self.tela_orcamento)
        self.bot_orcamento.place(relx=0.9, rely=0.27, relwidth=0.09, relheight=0.12)

#BOTAO informaçoes
        self.bot_info = atk.Button3d(self.frame_1, text="Info", command=self.tela_opcoes, bg="#006675")
        self.bot_info.place(relx=0.84, rely=0.27, relwidth=0.05, relheight=0.12)
#botao telas
        self.bot_telas = atk.Button3d(self.frame_1, text="Telas", command=self.telas, bg="#006675")
        self.bot_telas.place(relx=0.7, rely=0.01, relwidth=0.09, relheight=0.12)



#criaçao dos labels
        self.lb_id_smartphone = Label(self.frame_1, text="ID \nAparelho", fg="black", bg="#006675",
                                      font=("candara", "15", "bold italic"))
        self.lb_id_smartphone.place(relx=0.51, rely=0.25, relwidth=0.14, relheight=0.15)

        self.entrada_id_smartphone = Entry(self.frame_1)
        self.entrada_id_smartphone.place(relx=0.65, rely=0.28, relwidth=0.17, relheight=0.10)


    def setor_de_busca(self):

# criaçao das label DO NOME de pesquisa
        self.lb_nome = Label(self.frame_1, text="Buscar", fg="black", bg="#006675",
                             font=("candara", "15", "bold italic"))
        self.lb_nome.place(relx=0.53, rely=0.5, relwidth=0.10, relheight=0.20)



# setor de busca
        # codigo de entrada DO NOME
        self.entrada_nome_i = Entry(self.frame_1)
        self.entrada_nome_i.place(relx=0.65, rely=0.55, relwidth=0.17, relheight=0.10)

        # LIMPAR BUSCA

        self.bot_limpar_BUSCA = atk.Button3d(self.frame_1, bg="#006698", text="Limpar", command=self.limpa_tela_inicial)
        self.bot_limpar_BUSCA.place(relx=0.85, rely=0.54, relwidth=0.08, relheight=0.12)

        self.bot_entregue = atk.Button3d(self.frame_1, bg="#007880", text="Arrumar", command=self.select_arrumar)
        self.bot_entregue.place(relx=0.42, rely=0.88, relwidth=0.10, relheight=0.12)

        self.bot_prontos = atk.Button3d(self.frame_1, bg="#007880", text="Prontos", command=self.select_prontos)
        self.bot_prontos.place(relx=0.0, rely=0.88, relwidth=0.10, relheight=0.12)

        self.bot_orcamento = atk.Button3d(self.frame_1, bg="#007880", text="Orçamento", command=self.select_orcamento)
        self.bot_orcamento.place(relx=0.79, rely=0.88, relwidth=0.10, relheight=0.12)

        self.bot_entregue = atk.Button3d(self.frame_1, bg="#007880", text="Pedidos", command=self.select_pedidos)
        self.bot_entregue.place(relx=0.9, rely=0.88, relwidth=0.10, relheight=0.12)

        self.bot_desistentes = atk.Button3d(self.frame_1, bg="#007880", text="Desistentes", command=self.select_desistentes)
        self.bot_desistentes.place(relx=0.11, rely=0.88, relwidth=0.10, relheight=0.12)

        self.bot_desistentes = atk.Button3d(self.frame_1, bg="#007880", text="Voltou", command=self.select_voltou)
        self.bot_desistentes.place(relx=0.22, rely=0.88, relwidth=0.10, relheight=0.12)

        self.bot_devedores = atk.Button3d(self.frame_1, bg="#007880", text="Devedores", command=self.select_devedores)
        self.bot_devedores.place(relx=0.68, rely=0.88, relwidth=0.10, relheight=0.12)

        # BOTAO BUSCAR nome
        self.bot_buscar = atk.Button3d(self.frame_1, bg="#006675", text="Nome", fg="white",
                                       command=self.busca_clientes)
        self.bot_buscar.place(relx=0.65, rely=0.7, relwidth=0.08, relheight=0.12)







        # botao busca modelo
        self.bot_buscar_m = atk.Button3d(self.frame_1, bg="#006675", text="Modelo", fg="white",
                               command=self.busca_modelo)
        self.bot_buscar_m.place(relx=0.74, rely=0.7, relwidth=0.08, relheight=0.12)
    def label(self):
# label nome entrada para cadastro de clientes
        self.lb_nome = Label(text="     Nome", fg="black", bg="#006675",
                             font=("candara", "15", "bold italic"))
        self.lb_nome.place(relx=0.01, rely=0.00, relwidth=0.10, relheight=0.09)
# codigo de entrada nome
        self.entrada_nome = Entry(self.frame_1)
        self.entrada_nome.place(relx=0.15, rely=0.02, relwidth=0.25, relheight=0.10)

# label telefone
        self.lb_telefone = Label(text="Telefone", fg="black", bg="#006675",
                                 font=("candara", "15", "bold italic"))
        self.lb_telefone.place(relx=0.01, rely=0.07, relwidth=0.12, relheight=0.05)
# codigo de entrada telefone
        self.entrada_telefone = Entry(self.frame_1)
        self.entrada_telefone.place(relx=0.15, rely=0.15, relwidth=0.25, relheight=0.10)

#marca
        #self.lb_marca = Label(self.frame_1,text=" Marca", fg="black", bg="#006675",
                              #font=("candara", "15", "bold italic"))
        #self.lb_marca.place(relx=0.01, rely=0.43, relwidth=0.10, relheight=0.05)

#MODELO
        self.lb_model = Label(self.frame_1, text="  Modelo", fg="black", bg="#006675",
                              font=("candara", "15", "bold italic"))
        self.lb_model.place(relx=0.01, rely=0.430, relwidth=0.10, relheight=0.05)

        #self.entrada_model = Entry(self.frame_1)
        #self.entrada_model.place(relx=0.15, rely=0.52, relwidth=0.08, relheight=0.10)


 # DESCRIÇÃO
        self.lb_descricao = Label(self.frame_1,text="Problema", fg="black", bg="#006675",
                                  font=("candara", "15", "bold italic"))
        self.lb_descricao.place(relx=0.01, rely=0.55 , relwidth=0.11, relheight=0.05)
        self.entrada_descricao_1 = Entry(self.frame_1)
        self.entrada_descricao_1.place(relx=0.28, rely=0.52, relwidth=0.12, relheight=0.10)


# ID DO CLIENTE PARA ADICIONAR O APARELHO
        self.lb_id_cliente = Label(self.frame_1, text="   ID Cliente", fg="black", bg="#006675",font=("candara", "15", "bold italic"))
        self.lb_id_cliente.place(relx=0.13, rely=0.28, relwidth=0.12, relheight=0.10)

        self.entrada_id_cliente = Entry(self.frame_1)
        self.entrada_id_cliente.place(relx=0.25, rely=0.28, relwidth=0.15, relheight=0.1)
    def tabela_inicial(self):
        # criaçao da tabela
        self.tabela = ttk.Treeview(self.frame_2, height=4, columns=("coluna1", "coluna2", "coluna3", "coluna4",
                                                                    "coluna5","coluna6","coluna7","coluna8"))

        self.tabela.heading("#1", text="Problema")
        self.tabela.heading("#2", text="Cliente")
        self.tabela.heading("#3", text="Modelo")
        self.tabela.heading("#4", text="ID aparelho")
        self.tabela.heading("#5", text="Status")
        self.tabela.heading("#6", text="Orçamento")
        self.tabela.heading("#7", text="Dívida")
        self.tabela.heading("#8", text="Observação")

        self.tabela.column("#0", width=00, minwidth=50, stretch=NO)
        self.tabela.column("#1", width=120, minwidth=50, stretch=NO)
        self.tabela.column("#2", width=150, minwidth=50, stretch=NO)
        self.tabela.column("#3", width=150, minwidth=50, stretch=NO)
        self.tabela.column("#4", width=80, minwidth=50, stretch=NO)
        self.tabela.column("#5", width=110, minwidth=50, stretch=NO)
        self.tabela.column("#6", width=80, minwidth=50, stretch=NO)
        self.tabela.column("#7", width=80, minwidth=50, stretch=NO)
        self.tabela.column("#8", width=340, minwidth=50, stretch=NO)

        self.tabela.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.95)

# duplo clique
        self.tabela.bind("<Double-1>",self.duplo_tela_inicial)















class aplicacao (funcs,nivel_2,tela_1):

    def __init__(self):
        self.root = root
        self.tela_inicial()
        self.select_arrumar()




        root.mainloop()
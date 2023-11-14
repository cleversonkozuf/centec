
from modulos import *


class funcs():




    def limpa_tela(self):
        self.entrada_nome.delete(0, END)
        self.entrada_telefone.delete(0,END)
        self.entrada_id_cliente.delete(0,END)
        self.entrada_descricao_1.delete(0,END)
        #self.entrada_model.delete(0, END)

#limpa a busca da tela inicial e chama a funçao que faz o select depois da busca
    def limpa_tela_inicial(self):
        self.entrada_nome_i.delete(0, END)
        self.entrada_id_smartphone.delete(0, END)
        self.select_arrumar()

    def limpa_tela_telas(self):
        self.entrada_modelo.delete(0,END)
        self.entrada_descricao.delete(0,END)
        self.entrada_fornecedor.delete(0,END)
        self.entrada_excluir_tela.delete(0, END)
        self.entrada_valor.delete(0,END)
    def limpa_tela_fornecedor(self):
        self.entrada_nome_fornecedor.delete(0,END)
        self.entrada_telefone_fornecedor.delete(0,END)
        self.fornecedor.delete(0,END)
    def limpa_tela_edita_clientes(self):
        self.mostra_id.delete(0,END)
        self.entrada_edita_nome.delete(0,END)
        self.entrada_edita_telefone.delete(0,END)
    def limpa_tela_observacao(self):
        self.entrada_observacao.delete(0,END)
    def limpa_tela_observacao_divida(self):
        self.entrada_observacao_divida.delete(0,END)
    def limpa_tela_ops(self):
        self.entrada_valor_peca.delete(0,END)
        self.entrada_cgarantia.delete(0,END)
        self.entrada_sgarantia.delete(0,END)


    def duplo_tela_inicial(self,event):
        self.entrada_id_smartphone.delete(0, END)
        self.tabela.selection()

        for i in self.tabela.selection():
            col1,col2,col3,col4,col5,col6,col7,col8 = self.tabela.item(i ,'values')
            self.entrada_id_smartphone.insert(END,col4)
        self.tela_opcoes()

    def duplo_telas(self,event):
        self.entrada_excluir_tela.delete(0, END)
        self.tabela_telas.selection()

        for i in self.tabela_telas.selection():
            col1,col2,col3,col4,col5,col6,col7 = self.tabela_telas.item(i,'values')
            self.entrada_excluir_tela.insert(END,col1)

    def duplo_tela_clientes(self,event):
        self.id_edita = Entry(self.frame_editar)
        self.tabela_bd.selection()


        for i in self.tabela_bd.selection():

            col1,col2,col3,col4 = self.tabela_bd.item(i,'values')

            self.entrada_nome.delete(0,END)
            self.entrada_nome.insert(END,col2)

            self.entrada_id_cliente.delete(0,END)
            self.entrada_id_cliente.insert(END,col1)
            self.id_edita.delete(0,END)
            self.id_edita.insert(END,col1)
        self.limpa_tela_edita_clientes()
        self.preenche_dados_editar()






        # BANCO DE DADOS
#funçao que conecta ao banco de dados
    def conecta_BD(self):
        #conn = pyodbc.connect(DRIVER="SQL Server",host='CLEVERSON\DB_CENTRAL',database='central_teste')
        #PARA SERVIDOR
        conn = pyodbc.connect(DRIVER="SQL Server",host='SERVIDOR\SQLEXPRESS',database='central_tec')
        #PARA COMPUTADORES NA REDE
        #conn = pyodbc.connect(DRIVER="SQL Server",host='192.168.3.214\\SQLEXPRESS', database='central_tec',User = 'appcentraltec',Password = 'central')


        self.cursor = conn.cursor()
#função que desconecta o banco de dados
    def desconecta_bd(self):
        self.cursor.close()

# CLIENTES
#função que faz a busca do nome na tela inicial
    def busca_clientes (self):
        self.conecta_BD()
        self.tabela.delete(*self.tabela.get_children())
        self.entrada_nome_i.insert(END, "%")
        nome = self.entrada_nome_i.get()
        self.cursor.execute("""SELECT id_cliente,NOME,telefone,id_smart,situacao,orcamento,observacao FROM clientes 
        INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
        WHERE nome LIKE '%s' ORDER BY NOME ASC""" % nome)
        resultado_busca = self.cursor.fetchall()

        for (id, nome, telefone,id_smart,situacao,orcamento,obs) in resultado_busca:
            self.tabela.insert("", "end", values=(id, nome, telefone,id_smart,situacao,orcamento,obs))
        self.cursor.commit()
        self.desconecta_bd()

    def busca_clientes_add (self):
        self.conecta_BD()
        self.tabela.delete(*self.tabela.get_children())
        self.entrada_nome.insert(END, "%")
        nome = self.entrada_nome.get()

        self.cursor.execute("""SELECT id_cliente,NOME,telefone,id_smart,situacao,orcamento,descricao,observacao FROM clientes 
                                        INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
                                        WHERE nome LIKE '%s' ORDER BY NOME DESC""" % nome)
        resultado = self.cursor.fetchall()

        for (id, nome, telefone, id_smart, situacao, orcamento,descricao, obs) in resultado:
            self.tabela.insert("", "end", values=(id, nome, telefone, id_smart, situacao, orcamento,descricao, obs))

        self.desconecta_bd()
        self.limpa_tela()
        self.entrada_nome.insert(0, nome)
        self.entrada_id_cliente.insert(0,id)






    def busca_modelo(self):
        self.conecta_BD()
        self.tabela.delete(*self.tabela.get_children())
        self.entrada_nome_i.insert(END, "%")
        nome = self.entrada_nome_i.get()
        self.cursor.execute("""SELECT id_cliente,NOME,modelo,id_smart,situacao,orcamento,observacao FROM clientes 
               INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
               WHERE modelo LIKE '%s' ORDER BY NOME ASC""" % nome)
        resultado_busca = self.cursor.fetchall()

        for (id, nome, telefone, id_smart, situacao, orcamento,observacao) in resultado_busca:
            self.tabela.insert("", "end", values=(id, nome, telefone, id_smart, situacao, orcamento,observacao))
        self.cursor.commit()
        self.desconecta_bd()


# adiciona o cliente
    def adicione_cliente(self):
        self.nome = self.entrada_nome.get()
        self.telefone = self.entrada_telefone.get()
        try:
            self.conecta_BD();
            self.cursor.execute(""" INSERT INTO dbo.clientes (nome, telefone, data_registro)
        VALUES (?,?,getdate())""", (self.nome, self.telefone))
            self.cursor.commit()
            self.desconecta_bd()
        except AttributeError:
            messagebox.showinfo(title='Centec', message="preencha os dados")

        self.select()
        self.limpa_tela()
        self.preenche()
# deleta cliente
    def delete_cliente(self):
        self.id_delete = self.mostra_id.get()
        self.conecta_BD()
        self.cursor.execute("""DELETE clientes
                            WHERE id_cliente =""" + self.id_delete)
        self.cursor.commit()
        self.desconecta_bd()
        messagebox.showinfo(title='Aviso', message='Cliente removido \n do banco de dados')
        self.select_tela_consultar_clientes()
        self.select()
        self.limpa_tela_edita_clientes()
# chama os botoes de editar



# preeenche os dados nos entry`s para editar os dados dos clientes
    def preenche_dados_editar(self):
        self.id_edita = self.id_edita.get()
        self.conecta_BD()
        self.cursor.execute("""SELECT id_cliente FROM clientes
                 WHERE id_cliente = """ + self.id_edita)
        resultado = self.cursor.fetchall()
        resultado = [list(rows) for rows in resultado]
        self.mostra_id.insert(END, resultado)

        self.cursor.execute("""SELECT nome FROM clientes
                         WHERE id_cliente = """ + self.id_edita)
        nome = self.cursor.fetchall()
        nome = [list(rows) for rows in nome]
        self.entrada_edita_nome.insert(END, nome)

        self.cursor.execute("""SELECT telefone FROM clientes
                                WHERE id_cliente = """ + self.id_edita)
        telefone = self.cursor.fetchall()
        telefone = [list(rows) for rows in telefone]
        self.entrada_edita_telefone.insert(END, telefone)

        self.cursor.commit()
        self.desconecta_bd()

    # edita cliente
    def edita_cliente(self):
        self.telefone_editado = self.entrada_edita_telefone.get()
        self.nome_editado = self.entrada_edita_nome.get()
        self.id_cliente = self.mostra_id.get()
        self.conecta_BD()
        self.cursor.execute("""UPDATE dbo.clientes SET  telefone = """ + self.telefone_editado +
                                                  """,data_registro = GETDATE(),
                                                   nome = ? 
                                                   WHERE id_cliente = """ + self.id_cliente,(self.nome_editado))
        self.cursor.commit()

        self.desconecta_bd()

        self.select_tela_consultar_clientes()
        self.limpa_tela_edita_clientes()



    # ADICIONA SMARTPHONE
# funçao que adiciona o smart
    def adiciona_smart(self):
        self.chek_box_s()
        self.chek_p()
        self.codigo = self.entrada_id_cliente.get()
        self.modelo = self.modelos.get()
        #self.descricao = self.entrada_descricao_1.get()
        self.id_smart = self.entrada_id_smartphone.get()

        self.conecta_BD()

        self.cursor.execute(""" INSERT INTO dbo.smartphone ( marca, modelo,
         data_entrada,cod_cliente,situacao,problema)
               VALUES (?,?,getdate(),?,'Fazer Orçamento',?)""", (self.marca, self.modelo
                                                , self.codigo,self.problema))
        self.cursor.commit()
        self.desconecta_bd()

        self.preenche_novo_id()
        self.tela_opcoes()



        self.limpa_tela()
# da baixa no smartphone
    def dar_baixa(self):
        self.id_smart = self.entrada_id_smartphone.get()
        self.conecta_BD()
        self.cursor.execute(
            """ UPDATE smartphone SET data_sai = GETDATE(),
                                      statos = 1 
                                      WHERE id_smart =""" + self.id_smart)
        self.cursor.execute(""" UPDATE smartphone SET data_mudanca_status = GETDATE(),
                                                      situacao = 'Entregue'
                                                      WHERE id_smart = """ + self.id_smart)

        self.cursor.commit()
        self.desconecta_bd()



    def select(self):
        self.tabela.delete(*self.tabela.get_children())
        self.conecta_BD()
        dados = self.cursor.execute(""" SELECT id_cliente,NOME,telefone,id_smart,situacao,orcamento,descricao,observacao FROM clientes 
          INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
          order by id_cliente; """)

        for (id, nome, telefone, id_smart,situacao,orcamento,descricao,observacao) in dados:
            self.tabela.insert("", "end", values=(id, nome, telefone,id_smart, situacao,orcamento,descricao,observacao))

        self.cursor.commit()
        self.desconecta_bd()
    def select_prontos(self):
        self.tabela.delete(*self.tabela.get_children())
        self.conecta_BD()
        dados = self.cursor.execute(""" SELECT problema,NOME,modelo,id_smart,situacao,orcamento,descricao,observacao FROM clientes 
                  INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
                  where situacao = 'Pronto'
                  order by id_smart DESC; """)

        for (problema, nome, modelo, id_smart, situacao, orcamento,descricao,observacao) in dados:
            self.tabela.insert("", "end", values=(problema, nome, modelo, id_smart, situacao, orcamento,descricao,observacao))
        self.cursor.commit()
        self.desconecta_bd()
    def select_orcamento(self):
        self.tabela.delete(*self.tabela.get_children())
        self.conecta_BD()
        dados = self.cursor.execute(""" SELECT problema,NOME,modelo,id_smart,situacao,orcamento,descricao,observacao FROM clientes 
                          INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
                          where situacao = 'Fazer Orçamento'
                          order by id_smart DESC; """)

        for (problema, nome, modelo, id_smart, situacao, orcamento,descricao,observacao) in dados:
            self.tabela.insert("", "end", values=(problema, nome, modelo, id_smart, situacao, orcamento,descricao,observacao))
        self.cursor.commit()
        self.desconecta_bd()
    def select_pedidos(self):
        self.tabela.delete(*self.tabela.get_children())
        self.conecta_BD()
        dados = self.cursor.execute(""" SELECT problema,NOME,modelo,id_smart,situacao,orcamento,descricao,observacao FROM clientes 
                                  INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
                                  where pedido = '1'
                                  order by id_cliente; """)

        for (problema, nome, modelo, id_smart, situacao, orcamento,descricao,observacao) in dados:
            self.tabela.insert("", "end", values=(problema, nome, modelo, id_smart, situacao, orcamento,descricao,observacao))
        self.cursor.commit()
        self.desconecta_bd()
    def select_arrumar(self):
        self.tabela.delete(*self.tabela.get_children())
        self.conecta_BD()
        dados = self.cursor.execute(""" SELECT problema,NOME,modelo,id_smart,situacao,orcamento,descricao,observacao FROM clientes 
                                          INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
                                          where situacao = 'Orçamento feito' OR situacao = 'Pedido feito'
                                          order by id_smart DESC; """)

        for (problema, nome, modelo, id_smart, situacao, orcamento,descricao,observacao) in dados:
            self.tabela.insert("", "end", values=(problema, nome, modelo, id_smart, situacao, orcamento,descricao,observacao))
        self.cursor.commit()
        self.desconecta_bd()
    def select_desistentes(self):
        self.tabela.delete(*self.tabela.get_children())
        self.conecta_BD()
        dados = self.cursor.execute(""" SELECT problema,NOME,modelo,id_smart,situacao,orcamento,descricao,observacao FROM clientes 
                                          INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
                                          where situacao = 'Desistiu'
                                          order by id_smart DESC; """)

        for (problema, nome, modelo, id_smart, situacao, orcamento,descricao,observacao) in dados:
            self.tabela.insert("", "end", values=(problema, nome, modelo, id_smart, situacao, orcamento,descricao,observacao))
        self.cursor.commit()
        self.desconecta_bd()

    def select_voltou(self):
        self.tabela.delete(*self.tabela.get_children())
        self.conecta_BD()
        dados = self.cursor.execute(""" SELECT problema,NOME,modelo,id_smart,situacao,orcamento,descricao,observacao FROM clientes 
                                          INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
                                          where situacao = 'Voltou'
                                          order by id_smart DESC; """)

        for (problema, nome, modelo, id_smart, situacao, orcamento,descricao,observacao) in dados:
            self.tabela.insert("", "end", values=(problema, nome, modelo, id_smart, situacao,descricao, orcamento,observacao))
        self.cursor.commit()
        self.desconecta_bd()

    def select_devedores(self):

        self.tabela.delete(*self.tabela.get_children())
        self.conecta_BD()
        dados = self.cursor.execute(""" SELECT problema,NOME,modelo,id_smart,situacao,orcamento,descricao,observacao FROM clientes 
                                          INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
                                          where situacao = 'Devendo'
                                          order by id_smart DESC; """)

        for (problema, nome, modelo, id_smart, situacao, orcamento,descricao,observacao) in dados:
            self.tabela.insert("", "end", values=(problema, nome, modelo, id_smart, situacao, orcamento,descricao,observacao))
        self.cursor.commit()
        self.desconecta_bd()
#select tela aparelhos
    def select_aparelhos(self):
        # select da tabela
        self.tabela_aparelhos.delete(*self.tabela_aparelhos.get_children())
        self.conecta_BD()
        lista = self.cursor.execute("""SELECT NOME,telefone,Marca,modelo,id_smart,orcamento,descricao,situacao,observacao AS Status FROM clientes 
               INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
               ORDER BY nome ASC;""")

        for (id, cod, marca, modelo, orcamento, data, descricao, status,observacao) in lista:
            self.tabela_aparelhos.insert("", "end", values=(id, cod, marca, modelo, orcamento, data, descricao, status,observacao))
        self.cursor.commit()
        self.desconecta_bd()
#select informaçoes
    def select_informaçoes(self):
        # pega o id digitado na tela inicial e faz o select
        self.id = self.entrada_id_smartphone.get()
        self.conecta_BD()
#tabela 1
        lista = self.cursor.execute("""SELECT id_cliente,NOME,telefone,Marca,modelo,id_smart
                                            AS Status FROM clientes 
                                            INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
                                            WHERE id_smart = """ + self.id)
        for (id_cli,nome, cod, marca, modelo,id) in lista:
            self.tabela_aparelhos.insert("", "end", values=(
            id_cli,nome, cod, marca, modelo,id))
#tabela 2
        lista2 = self.cursor.execute("""SELECT  problema,orcamento,orcamento_sem,situacao,descricao,observacao
                                                    AS Status FROM clientes 
                                                    INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
                                                    WHERE id_smart = """ + self.id)

        for ( problema, orcamento, orcamento_sem,situacao, descricao,obs) in lista2:
            self.tabela_aparelhos2.insert("", "end", values=(
                problema, orcamento, orcamento_sem,situacao, descricao,obs))
#tabela3
        lista3 = self.cursor.execute("""SELECT convert(char,data_entrada,3),convert(char,data_mudanca_status,3),convert(char,data_sai,3)
                                                    AS Status FROM clientes 
                                                    INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
                                                    WHERE id_smart = """ + self.id)
        for ( data_entrada,data_volta,data_saida) in lista3:
            self.tabela_aparelhos3.insert("", "end", values=(
               data_entrada,data_volta,data_saida))

        self.cursor.commit()
        self.desconecta_bd()
#select da tela clientes
    def select_tela_consultar_clientes(self):
        # select da tabela
        self.tabela_bd.delete(*self.tabela_bd.get_children())
        self.conecta_BD()
        lista = self.cursor.execute(""" SELECT id_cliente, nome, telefone, convert(char,data_registro,3)  FROM clientes
        ORDER BY nome ASC; """)
        for (id, nome, telefone, data) in lista:
            self.tabela_bd.insert("", "end", values=(id, nome, telefone, data))
        self.cursor.commit()
        self.desconecta_bd()
# preenche o id do cliente para adicionar aparelho
    def preenche(self):
        self.conecta_BD()
        self.cursor.execute("""SELECT id_cliente FROM clientes
        WHERE data_registro <= getdate()
        ORDER BY id_cliente DESC""")
        resultado = self.cursor.fetchall()
#converte em lista
        resultado= [list(rows) for rows in resultado]
#pega o maior da lista
        id_maior = max(resultado, key=list)
#removendo [ do numero
        ex2 = "[,]"
        for letra in ex2:
            if letra in id_maior:
                id_maior = id_maior.replace(letra, '')

        self.entrada_id_cliente.insert(END, id_maior)
        self.cursor.commit()
        self.desconecta_bd()
# preenche novo id do smarthphone
    def preenche_novo_id (self):
        self.conecta_BD()
        self.cursor.execute("""SELECT id_smart FROM smartphone
        WHERE data_entrada <= getdate()""")
        resultado = self.cursor.fetchall()
        resultado = [list(rows) for rows in resultado]
        #pega o id maior
        id_maior = max(resultado, key=list)
        # tira os simbolos [
        ex2 = "[,]"
        for letra in ex2:
            if letra in id_maior:
                id_maior = id_maior.replace(letra, '')
        self.cursor.commit()
        self.desconecta_bd()
        self.limpa_tela_inicial()

        self.entrada_id_smartphone.insert(END,id_maior)
        messagebox.showinfo(title=id_maior, message="Aparelho Adicionado")


        self.entrada_model.delete(0, END)
# Deleta smart
    def delete_smart (self):
        self.id_delete = self.entrada_id_delete.get()
        self.conecta_BD()
        self.cursor.execute("""DELETE smartphone
                                WHERE id_smart ="""+self.id_delete)
        self.cursor.commit()
        self.desconecta_bd()
        self.select_aparelhos()
        messagebox.showinfo(title='Aviso', message='Aparelho removido \n do banco de dados')
        self.entrada_id_delete.delete(0,END)



# CAIXAS DE SELEÇÃO
    # checagem da marca escolhida nas caixas
    def chek_box_s (self):
        self.marca = self.marcas.get()
# checagem do problema tela,bateria ou conector
    def chek_p (self):

        self.problema = self.entrada_descricao_1.get()

    def seleciona_modelo(self, marcas):
        self.escolha = self.marcas.get()

        if self.escolha== "Motorola G":
            modelos=["Digitar",'G3','G4','G4 Play','G4 Plus', 'G5', 'G5 Plus', 'G5S', 'G5S Plus', 'G6', 'G6 Plus',
                     'G6 Play', 'G7', 'G7 Plus', 'G7 Power', 'G7 Play', 'G8', 'G8 Plus', 'G8 Play', 'G8 Power', 'G9', 'G9 Play', 'G9 Plus', 'G9 Power', 'G10', 'G10 Power','G20', 'G30', 'G40 Fusion', 'G60', 'G100']

        if self.escolha == "Samsung S":
            modelos = ["Digitar", "S6", "S6 Edge", "S6 Edge+", "S7", "S7 Edge", "S8", "S8+", "S9", "S9+",
                       "S10", "S10+", "S10e", "S20", "S20+", "S20 Ultra", "S21", "S21+", "S21 Ultra"]

        if self.escolha == "Samsung A":
            modelos = ["Digitar","A01","A01 CORE","A02","A03","A03 CORE","A10", "A20", "A30", "A40", "A50", "A60", "A70",
                       "A02s","A03s","A10s", "A20s", "A30s", "A40s","A50s",
                       "A11", "A21", "A31", "A41","A51", "A51 5G","A71", "A71 5G", "A21s", "A31s", "A51s", "A71s", "A02s",
                       "A12", "A32", "A42 5G", "A52", "A72", "A82",
                       "A22", "A52 5G", "A72 5G", "A22 5G", "A13", "A23", "A33", "A43", "A53", "A13s",
                       "A23s", "A33s", "A53s",
                       "A14"]

        if self.escolha == "Samsung J":
            modelos = ["Digitar","J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J1 Ace", "J2 Prime", "J3 Pro", "J5 Prime",
                       "J7 Prime","J7 Pro"]
        if self.escolha == "Xiaomi":
            modelos  = ["Digitar","Mi 11","Mi 11 Ultra","Mi 11 Lite","Mi 10","Mi 10 Pro","Mi 10T","Mi 10T Pro","Mi 10 Lite",
                        "Redmi Note 10","Redmi Note 10 Pro","Redmi Note 10S","Redmi Note 9","Redmi Note 9 Pro","Redmi Note 9S",
                        "Redmi 9","Redmi 9A","Redmi 9C","Poco X3","Poco X3 Pro","Poco F3","Mi A3","Mi 9","Mi 9T","Mi 9T Pro","Mi Mix 3","Mi Note 10","Mi Note 10 Pro"]
        if self.escolha == "Iphone":
            modelos  = ["Digitar","6","6 Plus","6S","6S Plus","SE","7","7 Plus","8","8 Plus","X","XS","XS Max","XR","11","11 Pro","11 Pro Max",
                        "SE (2ª geração)","12 mini","12","12 Pro","12 Pro Max","13 mini","13","13 Pro","13 Pro Max"]
        if self.escolha == "Lg":
            modelos  = ["Digitar"]
        if self.escolha == "Asus":
            modelos  = ["Digitar"]
        if self.escolha == "Blu":
            modelos  = ["Digitar"]
        if self.escolha == "Multilaser":
            modelos  = ["Digitar"]
        if self.escolha == "Nokia":
            modelos  = ["Digitar"]
        if self.escolha == "Sony":
            modelos  = ["Digitar"]
        if self.escolha == "Huawei":
            modelos  = ["Digitar"]
        if self.escolha == "Lenovo":
            modelos  = ["Digitar"]
        if self.escolha == "Alcatel":
            modelos  = ["Digitar"]
        if self.escolha == "ZTE":
            modelos  = ["Digitar"]
        if self.escolha == "Positivo":
            modelos  = ["Digitar"]

        self.modelos = StringVar()
        self.modelos.set("Modelo")
        self.Menu_modelos = OptionMenu(self.frame_1, self.modelos, *modelos,command=self.outro_modelo)
        self.Menu_modelos.place(relx=0.28, rely=0.4, relwidth=0.12, relheight=0.1)


    def outro_modelo(self, escolha):
        self.escolha_modelo = self.modelos.get()

        if self.escolha_modelo == "Digitar":

            self.entrada_model = Entry(self.frame_1)
            self.entrada_model.place(relx=0.41, rely=0.399, relwidth=0.10, relheight=0.10)
            self.modelos = self.entrada_model


    def concatena_problemas(self,problema):
        ok = self.outros_problemas.get()
        self.entrada_descricao_1.insert(END,ok)
        self.entrada_descricao_1.get()

    def passa_orcamento_tela_duploclik(self):

        self.orcament = self.entrada_cgarantia.get()
        self.orcamento_sem = self.entrada_sgarantia.get()
        self.conecta_BD()
        self.id = self.entrada_id_smartphone.get()
        self.cursor.execute("""UPDATE smartphone SET orcamento = """ + self.orcament +
                            """,orcamento_sem = """ + self.orcamento_sem +
                            """,situacao = 'Orçamento feito'"""
                            """ WHERE id_smart = """ + self.id)
        self.cursor.commit()
        self.desconecta_bd()


    def chek_fazer_pedido(self):
        self.pedido = self.pedir.get()
        if self.pedido == 1:
            self.pedir = '1'
            self.orcament = self.entrada_cgarantia.get()
            self.orcamento_sem = self.entrada_sgarantia.get()
            self.conecta_BD()
            self.id = self.entrada_id_smartphone.get()
            self.cursor.execute("""UPDATE smartphone SET orcamento = """ + self.orcament +
                                    """,orcamento_sem = """ + self.orcamento_sem +
                                    """,pedido = """ + self.pedir +
                                    """,situacao = 'Fazer pedido'"""
                                    """ WHERE id_smart = """ + self.id)
            self.cursor.commit()
            self.desconecta_bd()
            self.passar_orcamento()
            self.select()
        elif self.pedido == 0 :
            self.pedir = '0'
            self.orcament = self.entrada_cgarantia.get()
            self.orcamento_sem = self.entrada_sgarantia.get()
            self.conecta_BD()
            self.id = self.entrada_id_smartphone.get()
            self.cursor.execute("""UPDATE smartphone SET orcamento = """ + self.orcament +
                                """,orcamento_sem = """ + self.orcamento_sem +
                                """,pedido = """ + self.pedir +
                                """,situacao = 'Orçamento feito'"""
                                """ WHERE id_smart = """ + self.id)
            self.cursor.commit()
            self.desconecta_bd()
            self.passar_orcamento()
            self.select()

    def fazer_pedido(self):
        self.id = self.entrada_id_smartphone.get()
        self.conecta_BD()
        self.cursor.execute("""UPDATE smartphone SET pedido = '1', situacao = 'Fazer pedido'
                                       WHERE id_smart =""" + self.id)
        self.cursor.commit()
        self.desconecta_bd()


    def pedido_feito(self):

        self.id = self.entrada_id_smartphone.get()
        self.conecta_BD()
        self.cursor.execute("""UPDATE smartphone SET pedido = '0', situacao = 'Pedido feito'
                                WHERE id_smart =""" + self.id)
        self.cursor.commit()
        self.desconecta_bd()




    def add_observacao(self):

        self.id_smart = self.entrada_id_smartphone.get()
        self.observacao = self.entrada_observacao.get()
        self.conecta_BD()
        self.cursor.execute(""" UPDATE dbo.smartphone SET  observacao = ?
                                                     WHERE id_smart = """ + self.id_smart,(self.observacao))
        self.cursor.commit()
        self.desconecta_bd()
        self.limpa_tela_observacao()
        self.atualiza_obs()
    def add_observacao_divida(self):

        self.id_smart = self.entrada_id_smartphone.get()
        self.observacao = self.entrada_observacao_divida.get()
        self.conecta_BD()
        self.cursor.execute(""" UPDATE dbo.smartphone SET  descricao = ?
                                                     WHERE id_smart = """ + self.id_smart,(self.observacao))
        self.cursor.commit()
        self.desconecta_bd()
        self.limpa_tela_observacao_divida()
        self.atualiza_obs()
    def pago(self):

        self.id_smart = self.entrada_id_smartphone.get()
        self.observacao = "Pago"
        self.conecta_BD()
        self.cursor.execute(""" UPDATE dbo.smartphone SET  descricao = ?
                                                     WHERE id_smart = """ + self.id_smart,(self.observacao))
        self.cursor.commit()
        self.desconecta_bd()

        self.atualiza_obs()

# funçao que muda o status do aparelho para pronto
    def pronto (self):
        self.id_smart = self.entrada_id_smartphone.get()
        self.situacao = self.status.get()
        self.conecta_BD()

        self.cursor.execute(""" UPDATE smartphone SET data_mudanca_status = GETDATE(), situacao = 'Pronto'
                WHERE id_smart = """ + self.id_smart)
        self.cursor.commit()
        self.desconecta_bd()



    def desistiu(self):
        self.id_smart = self.entrada_id_smartphone.get()
        self.situacao = self.status.get()
        self.conecta_BD()

        self.cursor.execute(""" UPDATE smartphone SET data_mudanca_status = GETDATE(), situacao = 'Desistiu'
                 WHERE id_smart = """ + self.id_smart)
        self.cursor.commit()
        self.desconecta_bd()


    def voltou(self):
        self.id_smart = self.entrada_id_smartphone.get()
        self.situacao = self.status.get()
        self.conecta_BD()

        self.cursor.execute(""" UPDATE smartphone SET data_mudanca_status = GETDATE(),
                                                        situacao = 'Voltou'
                                                        WHERE id_smart = """ + self.id_smart)


        self.cursor.commit()
        self.desconecta_bd()

    def devedores(self):
        self.id_smart = self.entrada_id_smartphone.get()
        self.situacao = self.status.get()
        self.conecta_BD()

        self.cursor.execute(""" UPDATE smartphone SET data_mudanca_status = GETDATE(),
                                                        situacao = 'Devendo'
                                                        WHERE id_smart = """ + self.id_smart)


        self.cursor.commit()
        self.desconecta_bd()




    # orçamento
#funçao que atualiza o orçamento
    def passar_orcamento(self):

#pega o id digitado na tela inicial e faz o select
        self.id = self.entrada_id_smartphone.get()
        self.conecta_BD()
        lista = self.cursor.execute("""SELECT NOME,telefone,Marca,modelo,id_smart,problema,orcamento,orcamento_sem,descricao,situacao AS Status FROM clientes 
                 INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
                 WHERE id_smart = """ + self.id)
        for (id, cod, marca, modelo,problema, orcamento,orcamento_sem, data, descricao, status) in lista:
            self.tabela_aparelhos.insert("", "end", values=(id, cod, marca, modelo,problema, orcamento,orcamento_sem, data, descricao, status))


        self.cursor.commit()
        self.desconecta_bd()
# funçao que caucula e preeenche o orçamento
    def faz_orcamento(self):
        self.valor = self.entrada_valor_peca.get()
        self.valor = float(self.valor)
        self.valorcom = self.valor * 2 + 40
        self.valors = self.valorcom  * (15 / 100)
        self.valorsem = self.valorcom - self.valors
        self.entrada_cgarantia.insert(END,self.valorcom)
        self.entrada_sgarantia.insert(END,self.valorsem)

# FUNÇOES DA TELA 'TELAS'
#mostra os botoes para adicionar fornecedor
    def bot_add_fornecedor(self):
        #botoes
        self.bot_adicionar = atk.Button3d(self.frame_telas, text="Adicionar", command=self.adiciona_fornecedor,
                                           bg="#006675")
        self.bot_adicionar.place(relx=0.82, rely=0.5, relwidth=0.15, relheight=0.15)

        self.bot_editar_fornecedor = atk.Button3d(self.frame_telas, text="Editar Fornecedor", command=self.preeche_edita_fornecedor,
                                          bg="#006675")
        self.bot_editar_fornecedor.place(relx=0.63, rely=0.70, relwidth=0.15, relheight=0.15)

        self.bot_excluir = atk.Button3d(self.frame_telas, text="excluir", command=self.exclui_fornecedor,
                                          bg="#006675")
        self.bot_excluir.place(relx=0.9, rely=0.70, relwidth=0.10, relheight=0.15)


        #entrys
        self.entrada_nome_fornecedor = Entry(self.frame_telas)
        self.entrada_nome_fornecedor.place(relx=0.79, rely=0.2, relwidth=0.2, relheight=0.10)

        self.entrada_telefone_fornecedor = Entry(self.frame_telas)
        self.entrada_telefone_fornecedor.place(relx=0.79, rely=0.40, relwidth=0.2, relheight=0.10)

        self.fornecedor = Entry(self.frame_telas)
        self.fornecedor.place(relx=0.79, rely=0.72, relwidth=0.1, relheight=0.10)

        #labels
        self.nome = Label(self.frame_telas, text="Nome", fg="black", bg="#006675",
                            font=("candara", "15", "bold italic"))
        self.nome.place(relx=0.65, rely=0.2, relwidth=0.10, relheight=0.09)

        self.telefone = Label(self.frame_telas, text="Telefone", fg="black", bg="#006675",
                            font=("candara", "15", "bold italic"))
        self.telefone.place(relx=0.65, rely=0.40, relwidth=0.10, relheight=0.09)

        self.chama_tabela_fornecedor()
    def chama_tabela_fornecedor(self):
    #tabela de fornecedores
        self.tabela_fornecedor = ttk.Treeview(self.frame_telas2, height=4,
                                      columns=("coluna0", "coluna1", "coluna2", "coluna3", "coluna4"))
        self.tabela_fornecedor.heading("#1", text="id")
        self.tabela_fornecedor.heading("#2", text="nome")
        self.tabela_fornecedor.heading("#3", text="telefone")
        self.tabela_fornecedor.heading("#4", text="Data de registro")
        self.tabela_fornecedor.column("#0", width=00, minwidth=50, stretch=NO)
        self.tabela_fornecedor.column("#1", width=60, minwidth=50, stretch=NO)
        self.tabela_fornecedor.column("#2", width=150, minwidth=50, stretch=NO)
        self.tabela_fornecedor.column("#3", width=200, minwidth=50, stretch=NO)
        self.tabela_fornecedor.column("#4", width=200, minwidth=50, stretch=NO)
        self.tabela_fornecedor.place(relx=0.01, rely=0.04, relwidth=0.98,relheight=0.86)

        self.tabela_fornecedor.delete(*self.tabela_fornecedor.get_children())

        self.conecta_BD()
        lista = self.cursor.execute(""" SELECT id_fornecedor, nome, telefone, convert(char,data_registro,3)  FROM fornecedor
                ORDER BY nome ASC; """)
        for (id, nome, telefone,data) in lista:
            self.tabela_fornecedor.insert("", "end", values=(id, nome, telefone,data))

        self.desconecta_bd()
# adiciona o fornecedor no banco de dados
    def adiciona_fornecedor(self):
        self.nome = self.entrada_nome_fornecedor.get()
        self.telefone = self.entrada_telefone_fornecedor.get()
        self.conecta_BD();
        self.cursor.execute(""" INSERT INTO dbo.fornecedor (nome, telefone, data_registro)
                VALUES (?,?,getdate())""", (self.nome, self.telefone))
        self.cursor.commit()
        self.desconecta_bd()
        self.bot_add_fornecedor()
    def preeche_edita_fornecedor(self):
        self.id_para_editar = self.fornecedor.get()
        self.conecta_BD()
        self.cursor.execute(""" SELECT nome FROM fornecedor
                                WHERE id_fornecedor = """+ self.id_para_editar)
        nome_fornecedor = self.cursor.fetchall()
        nome_fornecedor = [list(rows) for rows in nome_fornecedor]
        self.entrada_nome_fornecedor.insert(END, nome_fornecedor)

        self.cursor.execute(""" SELECT telefone FROM fornecedor
                                        WHERE id_fornecedor = """ + self.id_para_editar)
        telefone_fornecedor= self.cursor.fetchall()
        telefone_fornecedor = [list(rows)for rows in telefone_fornecedor]
        self.entrada_telefone_fornecedor.insert(END,telefone_fornecedor)
        self.cursor.commit()
        self.desconecta_bd()

        self.bot_ok = atk.Button3d(self.frame_telas, text="OK", command=self.edita_fornecedor,
                                          bg="#006675")
        self.bot_ok.place(relx=0.82, rely=0.5, relwidth=0.15, relheight=0.15)
    def edita_fornecedor(self):
        self.id_para_editar = self.fornecedor.get()
        self.telefone_editado = self.entrada_telefone_fornecedor.get()
        self.nome_editado = self.entrada_nome_fornecedor.get()
        self.conecta_BD()
        self.cursor.execute("""UPDATE dbo.fornecedor SET  telefone = """ + self.telefone_editado +
                            """,data_registro = GETDATE(),
                             nome = ? 
                             WHERE id_fornecedor = """ + self.id_para_editar,(self.nome_editado))
        self.cursor.commit()
        self.desconecta_bd()

        self.chama_tabela_fornecedor()
        self.limpa_tela_fornecedor()
    # exclui o fornecedor do banco de dados
    def exclui_fornecedor(self):
        self.id_delete = self.fornecedor.get()
        self.conecta_BD()
        self.cursor.execute("""DELETE fornecedor
                                            WHERE id_fornecedor =""" + self.id_delete)
        self.cursor.commit()
        self.desconecta_bd()
        self.bot_add_fornecedor()
        self.limpa_tela_telas()
# pega os chek box e seleciona a marca
    def seleciona_marca_tela(self):
        self.escolhas = self.marca_tela.get()
        self.escolha_condicoes = self.condicao.get()
        if self.escolhas == 1:
            self.marcas = 'Motorola'
        if self.escolhas == 2:
            self.marcas = 'Samsung'
        if self.escolhas == 3:
            self.marcas = 'Xiaomi'
        if self.escolhas == 4:
            self.marcas = 'Lg'
        if self.escolhas == 5:
            self.marcas = 'Asus'
        if self.escolhas == 6:
            self.marcas = 'Iphone'

        if self.escolha_condicoes == 1:
            self.condicoes = 'Nova'
        if self.escolha_condicoes == 2:
            self.condicoes = 'Usada'

        elif self.escolhas == 0:
            messagebox.showerror(title='Aviso', message='Selecione a Marca da tela')
# adiciona a marca
    def adiciona_tela(self):
        self.modelo = self.entrada_modelo.get()
        self.descricao = self.entrada_descricao.get()
        self.fornecedor = self.entrada_fornecedor.get()
        self.valor = self.entrada_valor.get()

        self.conecta_BD();
        self.cursor.execute(""" INSERT INTO dbo.telas (marca, modelo, condicoes,descricao, data_registro,cod_fornecedor,valor)
                VALUES (?,?,?,?,getdate(),?,?)""", (self.marcas, self.modelo,self.condicoes,self.descricao,self.fornecedor,self.valor))
        self.cursor.commit()
        self.desconecta_bd()


        self.select_todas_marcas()
        self.limpa_tela_telas()
# exclui a tela
    def exclui_tela(self):
        self.id_delete = self.entrada_excluir_tela .get()
        self.conecta_BD()
        self.cursor.execute("""DELETE telas
                                    WHERE id_tela =""" + self.id_delete)
        self.cursor.commit()
        self.desconecta_bd()
        self.select_todas_marcas()
        self.limpa_tela()

        self.limpa_tela_telas()
#tabela telas
    def select_tabela_telas(self):

        self.tabela_telas = ttk.Treeview(self.frame_telas2, height=4,
                                  columns=("coluna0", "coluna1", "coluna2", "coluna3", "coluna4","coluna5","coluna6","coluna7"))
        self.tabela_telas.heading("#1", text="id")
        self.tabela_telas.heading("#2", text="Marca")
        self.tabela_telas.heading("#3", text="Modelo")
        self.tabela_telas.heading("#4", text="Condiçoes")
        self.tabela_telas.heading("#5", text="Fornecedor")
        self.tabela_telas.heading("#6", text="Valor")
        self.tabela_telas.heading("#7", text="Descrição")
        self.tabela_telas.column("#0", width=00, minwidth=50, stretch=NO)
        self.tabela_telas.column("#1", width=60, minwidth=50, stretch=NO)
        self.tabela_telas.column("#2", width=100, minwidth=50, stretch=NO)
        self.tabela_telas.column("#3", width=100, minwidth=50, stretch=NO)
        self.tabela_telas.column("#4", width=100, minwidth=50, stretch=NO)
        self.tabela_telas.column("#5", width=200, minwidth=50, stretch=NO)
        self.tabela_telas.column("#6", width=100, minwidth=50, stretch=NO)
        self.tabela_telas.column("#7", width=300, minwidth=50, stretch=NO)
        self.tabela_telas.place(relx=0.01, rely=0.04, relwidth=0.98, relheight=0.86)

# chama o duploclique
        self.tabela_telas.bind("<Double-1>",self.duplo_telas)

    def select_todas_marcas(self):
        # select da tabela
        self.select_tabela_telas()
        self.tabela_telas.delete(*self.tabela_telas.get_children())
        self.conecta_BD()
        lista = self.cursor.execute(""" SELECT id_tela, marca, modelo,condicoes,nome,valor, descricao  FROM telas
                INNER JOIN fornecedor ON id_fornecedor = telas.cod_fornecedor
                ORDER BY id_tela ASC; """)

        for (id, marca, modelo, condicoes,nome,valor,descricao) in lista:
            self.tabela_telas.insert("", "end", values=(id, marca, modelo, condicoes,nome,valor,descricao))
        self.cursor.commit()
        self.desconecta_bd()



# select das telas
    def select_telas_samsung(self):
        self.select_marca = 'Samsung'
        self.select_marcas()
    def select_telas_xiaomi(self):
        self.select_marca = 'Xiaomi'
        self.select_marcas()
    def select_telas_motorola(self):
        self.select_marca = 'Motorola'
        self.select_marcas()
    def select_telas_iphone(self):
        self.select_marca = 'Iphone'
        self.select_marcas()
    def select_telas_lg(self):
        self.select_marca = 'LG'
        self.select_marcas()
    def select_telas_asus(self):
        self.select_marca = 'Asus'
        self.select_marcas()

    def select_marcas(self):
            self.select_tabela_telas()
            self.tabela_telas.delete(*self.tabela_telas.get_children())
            self.conecta_BD()
            lista = self.cursor.execute(""" SELECT id_tela, marca, modelo,condicoes,nome,valor,descricao   FROM telas
                           INNER JOIN fornecedor ON id_fornecedor = telas.cod_fornecedor
                           WHERE marca = ? """
                                        """ORDER BY id_tela ASC """, (self.select_marca))

            for (id, marca, modelo, condicoes, nome, valor, descricao) in lista:
                self.tabela_telas.insert("", "end", values=(id, marca, modelo, condicoes, nome, valor, descricao))
            self.cursor.commit()
            self.desconecta_bd()


# FUNÇOES DA TELA OPÇOES

    def pronto_2(self):
        self.pronto()
        self.tabela_aparelhos2.delete(*self.tabela_aparelhos2.get_children())
        self.select_informaçoes()
        self.select_arrumar()
    def dar_baixa_2(self):
        self.dar_baixa()
        self.tabela_aparelhos2.delete(*self.tabela_aparelhos2.get_children())
        self.tabela_aparelhos3.delete(*self.tabela_aparelhos3.get_children())
        self.select_prontos()
        self.select_informaçoes()
    def desistiu_2(self):
        self.desistiu()
        self.tabela_aparelhos2.delete(*self.tabela_aparelhos2.get_children())
        self.select_informaçoes()
    def voltou_2(self):
        self.voltou()
        self.tabela_aparelhos2.delete(*self.tabela_aparelhos2.get_children())
        self.tabela_aparelhos3.delete(*self.tabela_aparelhos3.get_children())
        self.select_informaçoes()
    def devedores_2(self):
        self.devedores()
        self.tabela_aparelhos2.delete(*self.tabela_aparelhos2.get_children())
        self.tabela_aparelhos3.delete(*self.tabela_aparelhos3.get_children())
        self.select_informaçoes()
        self.tela_obs_devedor()
    def pago_2(self):
        self.pago()
        self.tabela_aparelhos2.delete(*self.tabela_aparelhos2.get_children())
        self.tabela_aparelhos3.delete(*self.tabela_aparelhos3.get_children())
        self.select_informaçoes()

    def fazer_pedido_2(self):
        self.fazer_pedido()
        self.tabela_aparelhos2.delete(*self.tabela_aparelhos2.get_children())
        self.select_informaçoes()
        self.select_pedidos()
    def pedido_feito_2(self):
        self.pedido_feito()
        self.tabela_aparelhos2.delete(*self.tabela_aparelhos2.get_children())
        self.select_informaçoes()
        self.select_pedidos()
    def atualiza_obs(self):
        self.tabela_aparelhos2.delete(*self.tabela_aparelhos2.get_children())
        self.select_informaçoes()
    def atualiza_orcamento(self):
        self.passa_orcamento_tela_duploclik()
        self.tabela_aparelhos2.delete(*self.tabela_aparelhos2.get_children())
        self.select_informaçoes()
        self.select_orcamento()
        self.limpa_tela_ops()








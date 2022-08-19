
from modulos import *


class funcs():
    def limpa_tela(self):
        self.entrada_nome.delete(0, END)
        self.entrada_telefone.delete(0,END)
        self.entrada_id_cliente.delete(0,END)
        self.entrada_model.delete(0,END)
        self.entrada_descricao.delete(0,END)


#limpa a busca da tela inicial e chama a funçao que faz o select depois da busca
    def limpa_tela_inicial(self):
        self.entrada_nome_i.delete(0, END)
        self.entrada_id_smartphone.delete(0, END)
        self.select()
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


# BANCO DE DADOS
#funçao que conecta ao banco de dados
    def conecta_BD(self):
        conn = pyodbc.connect(DRIVER="SQL Server",host='CLEVERSON\DB_CENTRAL',database='central_teste')

        #conn = pyodbc.connect(DRIVER="SQL Server",host='192.168.3.10\\SQLEXPRESS',database='central_tec',User = 'appcentraltec',Password = 'central')

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
        self.cursor.execute("""SELECT id_cliente,NOME,telefone,id_smart,situacao,orcamento FROM clientes 
        INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
        WHERE nome LIKE '%s' ORDER BY NOME ASC""" % nome)
        resultado_busca = self.cursor.fetchall()

        for (id, nome, telefone,id_smart,situacao,orcamento) in resultado_busca:
            self.tabela.insert("", "end", values=(id, nome, telefone,id_smart,situacao,orcamento))
        self.desconecta_bd()

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
        self.id_delete = self.entrada_idcli_delete.get()
        self.conecta_BD()
        self.cursor.execute("""DELETE clientes
                            WHERE id_cliente =""" + self.id_delete)
        self.cursor.commit()
        self.desconecta_bd()
        messagebox.showinfo(title='Aviso', message='Cliente removido \n do banco de dados')
        self.select_tela_consultar_clientes()
        self.select()
# chama os botoes de editar
    def botoes_editar_cliente(self):
    #botao salvar
        self.bot_salvar = atk.Button3d(self.frame_editar, bg="#1EAAF1", text="SALVAR",
                                       command=self.edita_cliente)
        self.bot_salvar.place(relx=0.55, rely=0.0, relwidth=0.20, relheight=0.35)
    # botao excluir
        self.bot_excluir = atk.Button3d(self.frame_editar, text="Excluir Cliente",
                                        command=self.delete_cliente)
        self.bot_excluir.place(relx=0.15, rely=0.55, relwidth=0.20, relheight=0.35)
    # entry mostra id
        self.mostra_id= Entry(self.frame_editar)
        self.mostra_id.place(relx=0.01, rely=0.07, relwidth=0.08, relheight=0.2)
    #entry edita nome
        self.entrada_edita_nome = Entry(self.frame_editar)
        self.entrada_edita_nome.place(relx=0.1, rely=0.07, relwidth=0.20 ,relheight=0.2)
    #entry edita telefone
        self.entrada_edita_telefone = Entry(self.frame_editar)
        self.entrada_edita_telefone.place(relx=0.31, rely=0.07, relwidth=0.2, relheight=0.2)
    # entri delete
        self.entrada_idcli_delete = Entry(self.frame_editar)
        self.entrada_idcli_delete.place(relx=0.01, rely=0.65, relwidth=0.1, relheight=0.20)

        self.preenche_dados_editar()
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
        self.codigo = self.entrada_id_cliente.get()
        self.modelo = self.entrada_model.get()
        self.descricao = self.entrada_descricao.get()
        self.id_smart = self.entrada_id_smartphone.get()



        self.conecta_BD()
        print("conectando")
        # self.monta_tables()
        self.cursor.execute(""" INSERT INTO dbo.smartphone ( marca, modelo,
         data_entrada,descricao,cod_cliente,situacao,problema)
               VALUES (?,?,getdate(),?,?,'Fazer Orçamento',?)""", (self.marca, self.modelo,
                                                     self.descricao, self.codigo,self.problema))
        self.cursor.commit()
        self.desconecta_bd()
        self.select()
        self.preenche_novo_id()
        messagebox.showinfo(title='Centec', message="aparelho adicionado")
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
        self.limpa_tela_inicial()
#select da tela inicial
    def select(self):
        self.tabela.delete(*self.tabela.get_children())
        self.conecta_BD()
        dados = self.cursor.execute(""" SELECT id_cliente,NOME,telefone,id_smart,situacao,orcamento,observacao FROM clientes 
          INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
          order by id_cliente; """)

        for (id, nome, telefone, id_smart,situacao,orcamento,observacao) in dados:
            self.tabela.insert("", "end", values=(id, nome, telefone,id_smart, situacao,orcamento,observacao))

        self.desconecta_bd()
    def select_prontos(self):
        self.tabela.delete(*self.tabela.get_children())
        self.conecta_BD()
        dados = self.cursor.execute(""" SELECT id_cliente,NOME,telefone,id_smart,situacao,orcamento,observacao FROM clientes 
                  INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
                  where situacao = 'Pronto'
                  order by id_cliente; """)

        for (id, nome, telefone, id_smart, situacao, orcamento,observacao) in dados:
            self.tabela.insert("", "end", values=(id, nome, telefone, id_smart, situacao, orcamento,observacao))
        self.desconecta_bd()
    def select_orcamento(self):
        self.tabela.delete(*self.tabela.get_children())
        self.conecta_BD()
        dados = self.cursor.execute(""" SELECT id_cliente,NOME,telefone,id_smart,situacao,orcamento,observacao FROM clientes 
                          INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
                          where situacao = 'Fazer Orçamento'
                          order by id_cliente; """)

        for (id, nome, telefone, id_smart, situacao, orcamento,observacao) in dados:
            self.tabela.insert("", "end", values=(id, nome, telefone, id_smart, situacao, orcamento,observacao))
        self.desconecta_bd()
    def select_pedidos(self):
        self.tabela.delete(*self.tabela.get_children())
        self.conecta_BD()
        dados = self.cursor.execute(""" SELECT id_cliente,NOME,telefone,id_smart,situacao,orcamento,observacao FROM clientes 
                                  INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
                                  where pedido = '1'
                                  order by id_cliente; """)

        for (id, nome, telefone, id_smart, situacao, orcamento,observacao) in dados:
            self.tabela.insert("", "end", values=(id, nome, telefone, id_smart, situacao, orcamento,observacao))
        self.desconecta_bd()
    def select_arrumar(self):
        self.tabela.delete(*self.tabela.get_children())
        self.conecta_BD()
        dados = self.cursor.execute(""" SELECT id_cliente,NOME,modelo,id_smart,situacao,orcamento,observacao FROM clientes 
                                          INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
                                          where situacao = 'Orçamento feito' OR situacao = 'Pedido feito'
                                          order by id_cliente; """)

        for (id, nome, modelo, id_smart, situacao, orcamento,observacao) in dados:
            self.tabela.insert("", "end", values=(id, nome, modelo, id_smart, situacao, orcamento,observacao))
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
        lista3 = self.cursor.execute("""SELECT convert(char,data_entrada,3),convert(char,data_sai,3)
                                                    AS Status FROM clientes 
                                                    INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
                                                    WHERE id_smart = """ + self.id)
        for ( data_entrada,data_saida) in lista3:
            self.tabela_aparelhos3.insert("", "end", values=(
               data_entrada,data_saida))


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
        #self.novo_id_smartphone.insert(END,id_maior)
        self.desconecta_bd()
        messagebox.showinfo(title="ID do novo aparelho",message= id_maior)
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
        self.escolha = self.escolha_marca.get()

        if self.escolha == 1:
            self.marca = 'Motorola'
        if self.escolha == 2:
            self.marca = 'Samsung'
        if self.escolha == 3:
            self.marca = 'Xiaomi'
        if self.escolha == 4:
            self.marca = 'Lg'
        if self.escolha == 5:
            self.marca = 'Asus'
        if self.escolha == 6:
            self.marca = 'Iphone'
        elif self.escolha == 0 :
            self.marca = 'Outros'
# checagem do problema tela,bateria ou conector
    def chek_p (self):
        self.escolha_p = self.escolha_problema.get()

        if self.escolha_p == 1:
            self.problema = 'Tela'

        if self.escolha_p == 2:
            self.problema = 'Conector'

        if self.escolha_p == 3:
            self.problema = 'Bateria'

        if self.escolha_p == 4:
            self.problema = 'Desbloqueio'

        if self.escolha_p == 5:
            self.problema = 'Botões'

        if self.escolha_p == 6:
            self.problema = 'Outros'

        elif self.escolha_p == 0 :
              self.problema = 'Não Definido'

    def chek_muda_status(self):
        self.muda_status =  self.status.get()
        if self.muda_status == 1:
            self.pronto()
        if self.muda_status == 2:
            self.dar_baixa()
        if self.muda_status == 3:
            self.tela_observacoes()
        if self.muda_status == 4:
            self.pedido_feito()
        if self.muda_status == 5:
            self.fazer_pedido()
        else :
            print(self.muda_status)

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
        self.limpa_tela_inicial()

    def pedido_feito(self):

        self.id = self.entrada_id_smartphone.get()
        self.conecta_BD()
        self.cursor.execute("""UPDATE smartphone SET pedido = '0', situacao = 'Pedido feito'
                                WHERE id_smart =""" + self.id)
        self.cursor.commit()
        self.desconecta_bd()
        self.limpa_tela_inicial()



    def add_observacao(self):

        self.id_smart = self.entrada_id_smartphone.get()
        self.observacao = self.entrada_observacao.get()
        self.conecta_BD()
        self.cursor.execute(""" UPDATE dbo.smartphone SET  observacao = ?
                                                     WHERE id_smart = """ + self.id_smart,(self.observacao))
        self.cursor.commit()
        self.desconecta_bd()
        self.limpa_tela_observacao()

# funçao que muda o status do aparelho para pronto
    def pronto (self):
        self.id_smart = self.entrada_id_smartphone.get()
        self.situacao = self.status.get()
        self.conecta_BD()

        self.cursor.execute(""" UPDATE smartphone SET data_mudanca_status = GETDATE(), situacao = 'Pronto'
                WHERE id_smart = """ + self.id_smart)
        self.cursor.commit()
        self.desconecta_bd()
        self.limpa_tela_inicial()

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
        self.desconecta_bd()
# funçao que caucula e preeenche o orçamento
    def faz_orcamento(self):
        self.valor = self.entrada_valor_peca.get()
        self.valor = int(self.valor)
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
            self.desconecta_bd()





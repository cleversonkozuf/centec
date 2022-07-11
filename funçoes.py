
from modulos import *


class funcs():
    def limpa_tela(self):
        #self.entrada_cpf.delete(0,END)
        self.entrada_nome.delete(0, END)
        self.entrada_telefone.delete(0,END)
        self.entrada_id_cliente.delete(0,END)
        self.entrada_model.delete(0,END)
        self.entrada_marca.delete(0,END)
        self.entrada_orcamento.delete(0,END)
        self.entrada_descricao.delete(0,END)
        self.novo_id_smartphone.delete(0,END)

#limpa a busca da tela inicial e chama a funçao que faz o select depois da busca
    def limpa_tela_inicial(self):
        self.entrada_nome_i.delete(0, END)
        self.entrada_id_smartphone.delete(0, END)
        self.select_2()

#funçao que conecta ao banco de dados
    def conecta_BD(self):
        conn = pyodbc.connect(DRIVER="SQL Server",
                                 Server='CLEVERSON\DB_CENTRAL',
                                 database='bd_central')
        print("conexao feita")
        self.cursor = conn.cursor()

#função que desconecta o banco de dados
    def desconecta_bd(self):
        self.cursor.close();print("Desconectando ao banco de dados BD_Central_tec")

#função que faz a busca do nome na tela inicial
    def busca_clientes (self):
        self.conecta_BD()
        self.tabela.delete(*self.tabela.get_children())
        self.entrada_nome_i.insert(END, "%")
        nome = self.entrada_nome_i.get()
        self.cursor.execute("""SELECT id_cliente,NOME,telefone,id_smart FROM clientes 
        INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
        WHERE nome LIKE '%s' ORDER BY NOME ASC""" % nome)
        resultado_busca = self.cursor.fetchall()

        for (id, nome, telefone,id_smart) in resultado_busca:
            self.tabela.insert("", "end", values=(id, nome, telefone,id_smart))
        self.desconecta_bd()


#função que faz o select depois da busca
    def select_2 (self):
        self.tabela.delete(*self.tabela.get_children())
        self.conecta_BD()
        dados = self.cursor.execute(""" SELECT id_cliente,NOME,telefone,id_smart FROM clientes 
                INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
                order by id_cliente; """)

        for (id, nome, telefone, id_smart) in dados:
            self.tabela.insert("", "end", values=(id, nome, telefone, id_smart))

    def adicione_cliente(self):
        # self.cpf = self.entrada_cpf.get()
        self.nome = self.entrada_nome.get()
        self.telefone = self.entrada_telefone.get()
        self.conecta_BD();
        self.cursor.execute(""" INSERT INTO dbo.clientes (nome, telefone, data_registro)
        VALUES (?,?,getdate())""", (self.nome, self.telefone))

        self.cursor.commit()
        self.desconecta_bd()
        self.select()
        self.limpa_tela()
        self.preenche()

    def adiciona_smart(self):
        self.codigo = self.entrada_id_cliente.get()
        self.marca = self.entrada_marca.get()
        self.modelo = self.entrada_model.get()
        self.orcamento = self.entrada_orcamento.get()
        self.descricao = self.entrada_descricao.get()
        self.id_smart = self.entrada_id_smartphone.get()
        self.limpa_tela()


        self.conecta_BD()
        print("conectando")
        # self.monta_tables()
        self.cursor.execute(""" INSERT INTO dbo.smartphone ( marca, modelo, orcamento,
         data_entrada,descricao,cod_cliente,cod_loja,cod_fun)
               VALUES (?,?,?,getdate(),?,?,2,2)""", (self.marca, self.modelo, self.orcamento,
                                                     self.descricao, self.codigo,))
        self.cursor.commit()
        self.desconecta_bd()
        self.select()
        self.preenche_novo_id()
        # self.limpa_tela()
        # insere data de saida ao aparelho

    def dar_baixa(self):
        self.id_smart = self.entrada_id_smartphone.get()
        self.conecta_BD()
        self.cursor.execute(
            """ UPDATE smartphone SET data_sai = GETDATE(), statos = 1  WHERE id_smart =""" + self.id_smart)

        self.cursor.commit()
        self.desconecta_bd()
        self.limpa_tela_inicial()

    def select(self):
        self.tabela.delete(*self.tabela.get_children())
        self.conecta_BD()
        dados = self.cursor.execute(""" SELECT id_cliente,NOME,telefone,id_smart FROM clientes 
          INNER JOIN smartphone ON id_cliente = smartphone.cod_cliente
          order by id_cliente; """)

        for (id, nome, telefone, id_smart) in dados:
            self.tabela.insert("", "end", values=(id, nome, telefone, id_smart))

        self.desconecta_bd()

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
        self.novo_id_smartphone.insert(END,id_maior)
        self.desconecta_bd()



    def chek_box_s (self):
        print(self.samsung)

    def chek_box_m(self):
        print(self.motorola)

    def situacao (self):
        self.id_smart = self.entrada_id_smartphone.get()
        self.conecta_BD()
        if self.samsung == '1':
            self.cursor.execute(""" UPDATE smartphone SET data_mudanca_status = GETDATE(), situacao = 'Pt'
                WHERE id_smart = """ + self.id_smart)
        elif self.motorola == '2':
            self.cursor.execute(""" UPDATE smartphone SET data_mudanca_status = GETDATE(), situacao = 'aguardando'
                       WHERE id_smart = """ + self.id_smart)
        else :
            print("ta dando")
        self.cursor.commit()
        self.desconecta_bd()




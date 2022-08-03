create database central_tec

CREATE TABLE clientes
(
	id_cliente INT PRIMARY KEY IDENTITY NOT null,
	nome VARCHAR (30) ,
	telefone NUMERIC (11),
	data_registro DATETIME,

	cod_smart INT ,
	
);
CREATE TABLE smartphone
(
	id_smart INT PRIMARY KEY IDENTITY not null,
	marca VARCHAR (15) ,
	modelo VARCHAR (15) ,
	orcamento NUMERIC (6,2),        
	data_entrada DATETIME ,
	data_sai DATETIME,          
	descricao VARCHAR (200),
	statos bit,
	data_mudanca_status DATETIME,
	situacao VARCHAR (15),
	orcamento_sem VARCHAR (15),
	problema VARCHAR (15),

	cod_cliente INT,
	
);
CREATE TABLE fornecedor
(
	id_fornecedor INT PRIMARY KEY IDENTITY NOT null,
	nome VARCHAR (30) ,
	telefone NUMERIC (11),
	data_registro DATETIME,

	cod_tela INT ,
	
);
CREATE TABLE telas
(
	id_tela INT PRIMARY KEY IDENTITY not null,
	marca VARCHAR (15) ,
	modelo VARCHAR (15) ,
	condicoes VARCHAR (15) ,
	descricao VARCHAR (200),
	data_registro DATETIME ,

	cod_fornecedor INT,
);




	
	
	ALTER TABLE clientes ADD CONSTRAINT fk_cod_smart FOREIGN KEY (cod_smart) REFERENCES smartphone (id_smart);
	ALTER TABLE smartphone ADD CONSTRAINT fk_cod_cliente FOREIGN KEY (cod_cliente) REFERENCES clientes (id_cliente);
    ALTER TABLE telas ADD CONSTRAINT fk_cod_fornecedor FOREIGN KEY (cod_fornecedor) REFERENCES fornecedor (id_fornecedor);
    ALTER TABLE fornecedor ADD CONSTRAINT fk_cod_tela FOREIGN KEY (cod_tela) REFERENCES telas (id_tela);



 select * from clientes
 select * from smartphone
 select * from telas
 select * from fornecedor



USE ans_dados;


LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Relatorio_cadop.txt'
INTO TABLE empresas_saude
FIELDS TERMINATED BY ';'      -- Campo separado por ponto e vírgula
ENCLOSED BY '"'               -- Valores estão entre aspas
LINES TERMINATED BY '\n'      -- Cada linha termina com quebra de linha
IGNORE 1 LINES               -- Ignora o cabeçalho
(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, regiao_comercializacao, data_registro_ans);

select * from empresas_saude;

TRUNCATE TABLE empresas_saude;

DESCRIBE empresas_saude;






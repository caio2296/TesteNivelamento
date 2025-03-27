describe contabilidade;
select * from contabilidade;
#os arquivos tbm inserido: 2023/1T2023.txt, 2023/2T2023.txt,2023/3T2023.txt

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/data/2024/4T2024.txt'
INTO TABLE contabilidade
FIELDS TERMINATED BY ';'  
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES  
(@data, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET 
    data = STR_TO_DATE(@data, '%Y-%m-%d'),
    vl_saldo_inicial = IF(@vl_saldo_inicial = '', 0.00, REPLACE(@vl_saldo_inicial, ',', '.')),
    vl_saldo_final = IF(@vl_saldo_final = '', 0.00, REPLACE(@vl_saldo_final, ',', '.'));
    

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/data/2023/4T2023.txt'
INTO TABLE contabilidade
FIELDS TERMINATED BY ';'  
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES  
(@data, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET 
    data = STR_TO_DATE(@data, '%d/%m/%Y'),
    vl_saldo_inicial = IF(@vl_saldo_inicial = '', 0.00, REPLACE(@vl_saldo_inicial, ',', '.')),
    vl_saldo_final = IF(@vl_saldo_final = '', 0.00, REPLACE(@vl_saldo_final, ',', '.'));